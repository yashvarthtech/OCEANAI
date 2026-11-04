import os
import json
import logging
from flask import Flask, request, jsonify, send_from_directory
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

app = Flask(__name__, static_folder='.', static_url_path='')

# Load environment variables if available
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')

# Attempt to load from .env file if it exists
if os.path.exists('.env'):
    try:
        with open('.env', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    k, v = k.strip(), v.strip().strip('"').strip("'")
                    if k == 'OPENAI_API_KEY' and not OPENAI_API_KEY:
                        OPENAI_API_KEY = v
                    elif k == 'GEMINI_API_KEY' and not GEMINI_API_KEY:
                        GEMINI_API_KEY = v
                    elif k == 'ANTHROPIC_API_KEY' and not ANTHROPIC_API_KEY:
                        ANTHROPIC_API_KEY = v
    except Exception as e:
        logging.warning(f"Could not load .env file: {e}")

DEFAULT_SYSTEM_PROMPT = """You are OCEANGUARD AI, an intelligent marine conservation and sustainable fishing assistant aligned with UN SDG 14: Life Below Water.
You provide expert assistance to artisanal fishers, marine scientists, maritime authorities (Coast Guard), and seafood consumers.
You understand oceanography, IoT buoy telemetry (pH, dissolved oxygen, turbidity, sea temperature), AIS vessel trajectory tracking, Marine Protected Area (MPA) rules, sustainable non-destructive fishing gear, mangrove & coral reef restoration, and blockchain seafood provenance.
Respond clearly, constructively, and empathetically. When providing fisher advisories, support local coastal languages (such as Tamil, Malayalam, or English) if requested."""

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, x-api-key, anthropic-version'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    return response

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/presentation')
def serve_presentation():
    return send_from_directory('.', 'presentation.html')

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "online",
        "service": "OCEANGUARD AI Multi-Model Gateway",
        "providers_configured": {
            "chatgpt": bool(OPENAI_API_KEY),
            "gemini": bool(GEMINI_API_KEY),
            "claude": bool(ANTHROPIC_API_KEY)
        }
    })

# ============================================================
# UNIFIED AI CHAT & REASONING ENDPOINT
# ============================================================
@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"})

    data = request.get_json(force=True, silent=True) or {}
    provider = data.get('provider', 'gemini').lower() # 'chatgpt' | 'gemini' | 'claude'
    prompt = data.get('prompt', '')
    system_prompt = data.get('system_prompt', DEFAULT_SYSTEM_PROMPT)
    api_key = data.get('api_key', '').strip()
    model = data.get('model', '').strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        if provider in ['chatgpt', 'openai']:
            return call_openai(prompt, system_prompt, api_key, model)
        elif provider in ['gemini', 'google']:
            return call_gemini(prompt, system_prompt, api_key, model)
        elif provider in ['claude', 'anthropic']:
            return call_claude(prompt, system_prompt, api_key, model)
        else:
            return jsonify({"error": f"Unknown provider: {provider}. Choose 'chatgpt', 'gemini', or 'claude'."}), 400
    except Exception as e:
        logging.error(f"Error calling {provider}: {e}", exc_info=True)
        return jsonify({"error": str(e), "provider": provider}), 500

# ----------------- 1. OpenAI ChatGPT -----------------
def call_openai(prompt, system_prompt, user_key, user_model):
    key = user_key or OPENAI_API_KEY
    if not key:
        return jsonify({
            "error": "OpenAI API key missing. Please provide it in the UI or set OPENAI_API_KEY in .env.",
            "requires_key": True,
            "provider": "chatgpt"
        }), 401

    model = user_model or "gpt-4o-mini"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1200
    }

    resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=45)
    if resp.status_code != 200:
        return jsonify({"error": resp.text, "status_code": resp.status_code, "provider": "chatgpt"}), resp.status_code

    result = resp.json()
    reply = result["choices"][0]["message"]["content"]
    return jsonify({
        "reply": reply,
        "provider": "chatgpt",
        "model": model,
        "usage": result.get("usage", {})
    })

# ----------------- 2. Google Gemini -----------------
def call_gemini(prompt, system_prompt, user_key, user_model):
    key = user_key or GEMINI_API_KEY
    if not key:
        return jsonify({
            "error": "Google Gemini API key missing. Please provide it in the UI or set GEMINI_API_KEY in .env.",
            "requires_key": True,
            "provider": "gemini"
        }), 401

    model = user_model or "gemini-1.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": prompt}]}
        ],
        "systemInstruction": {
            "parts": [{"text": system_prompt}]
        },
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1200
        }
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=45)
    if resp.status_code != 200:
        return jsonify({"error": resp.text, "status_code": resp.status_code, "provider": "gemini"}), resp.status_code

    result = resp.json()
    try:
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        reply = json.dumps(result)

    return jsonify({
        "reply": reply,
        "provider": "gemini",
        "model": model,
        "usageMetadata": result.get("usageMetadata", {})
    })

# ----------------- 3. Anthropic Claude -----------------
def call_claude(prompt, system_prompt, user_key, user_model):
    key = user_key or ANTHROPIC_API_KEY
    if not key:
        return jsonify({
            "error": "Anthropic Claude API key missing. Please provide it in the UI or set ANTHROPIC_API_KEY in .env.",
            "requires_key": True,
            "provider": "claude"
        }), 401

    model = user_model or "claude-3-5-sonnet-20241022"
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "max_tokens": 1200,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    resp = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload, timeout=45)
    if resp.status_code != 200:
        return jsonify({"error": resp.text, "status_code": resp.status_code, "provider": "claude"}), resp.status_code

    result = resp.json()
    reply = result["content"][0]["text"]
    return jsonify({
        "reply": reply,
        "provider": "claude",
        "model": model,
        "usage": result.get("usage", {})
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*60)
    print("🌊 OCEANGUARD AI Multi-Model Server Ready!")
    print(f"👉 Local Web App: http://localhost:{port}")
    print(f"👉 AI Providers Connected:")
    print(f"   • OpenAI ChatGPT: {'[Configured]' if OPENAI_API_KEY else '[Key needed]'}")
    print(f"   • Google Gemini:  {'[Configured]' if GEMINI_API_KEY else '[Key needed]'}")
    print(f"   • Anthropic Claude:{'[Configured]' if ANTHROPIC_API_KEY else '[Key needed]'}")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=port, debug=False)
