# OCEANGUARD AI — Pitch Presentation & Animated UI Suite
**Intelligent Ocean Protection & Sustainable Fishing Platform**  
*UN SDG 14: Life Below Water · Multi-Model AI Connected*

---

## 🌊 Overview of Deliverables

This workspace contains the complete presentation and working prototype suite for **OCEANGUARD AI**, fully integrated with **Google Gemini API**, **OpenAI ChatGPT API**, and **Anthropic Claude API**.

### 1. Multi-Model AI Copilot & Gateway
- **Three Leading AI Providers Supported:**
  - ✦ **Google Gemini API** (`gemini-1.5-flash`, `gemini-2.0-flash`)
  - ⚡ **OpenAI ChatGPT API** (`gpt-4o`, `gpt-4o-mini`)
  - 🧠 **Anthropic Claude API** (`claude-3-5-sonnet`, `claude-3-haiku`)
- **Key Management:**
  - Easily configure keys via the **"⚙️ Keys"** button in the AI Copilot drawer (stored locally in browser `localStorage`).
  - Or supply keys via a `.env` file for the Python backend.
- **Contextual One-Click AI Prompts in Slides:**
  - **Slide 5 (Ocean Health):** `🤖 AI Anomaly Diagnostic (Live LLM)` — sends live buoy parameters (pH, DO, Turbidity, Temp) to the AI to diagnose chemical ballast discharge.
  - **Slide 6 (Illegal Fishing Watch):** `🤖 AI Threat Assessment` — sends AIS radar trajectory of suspicious trawlers to the AI for naval triage.
  - **Slide 7 (Sustainable Fisher Assistant):** Real-time conversational assistant in **Tamil (தமிழ்)**, **Malayalam (മലയാളം)**, and **English** with text-to-speech audio playback.
  - **Slide 9 (Seafood QR Provenance):** `🤖 Audit Catch with AI` — cryptographically audits batch provenance and fair-trade standards.

### 2. Interactive Animated Web Presentation Deck (`index.html` & `presentation.html`)
- **17 Full-Screen Interactive Slides** covering the entire hackathon concept, vision, 6 core modules, tech stack, real-world scenario, and pitch.
- **Live Animated UI Widgets:** Real-time ticking sensor gauges, 360° rotating radar sweep, vernacular audio voice synthesizer, and interactive 5-screen MVP prototype.
- **Web Audio API Ocean Ambience:** Synthesized soothing ocean wave soundscape directly in browser.

### 3. Backend Proxy Server (`server.py`)
- High-performance Python Flask server supporting unified AI endpoints:
  - `POST /api/chat`: Routes requests to Gemini, ChatGPT, or Claude.
  - `GET /api/status`: Checks key availability and system health.
  - Static file serving for presentation and prototype.

### 4. Microsoft PowerPoint Presentation (`OCEANGUARD_AI_Presentation.pptx`)
- High-contrast 16:9 widescreen presentation deck formatted with dark oceanic themes for Microsoft PowerPoint, Google Slides, or Keynote.

---

## 🚀 How to Run

### Method 1: Python Server Mode (Recommended for Full API Proxy)
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your API keys:
   ```env
   GEMINI_API_KEY=AIzaSy...
   OPENAI_API_KEY=sk-proj-...
   ANTHROPIC_API_KEY=sk-ant-...
   PORT=5000
   ```
3. Start the server:
   ```bash
   python server.py
   ```
4. Open **`http://localhost:5000`** in any web browser!

---

### Method 2: Standalone Browser Direct Mode
You can also open [`index.html`](file:///d:/windows/ppt/index.html) or [`presentation.html`](file:///d:/windows/ppt/presentation.html) directly in any browser:
- Click **"🤖 AI Copilot (ChatGPT · Gemini · Claude)"** in the top navigation bar.
- Click **"⚙️ Keys"** and paste your API key for Google Gemini, OpenAI, or Claude.
- If no key is entered yet, the built-in Intelligent Simulation Mode provides detailed marine biology, Coast Guard triage, and vernacular Tamil advisories out-of-the-box!

---

## 🕹️ Presentation Controls
- **Next Slide:** Press `[→]` (Right Arrow), `[Spacebar]`, or click `>`.
- **Previous Slide:** Press `[←]` (Left Arrow) or click `<`.
- **Fullscreen Mode:** Press `[F]`.
- **AI Copilot Drawer:** Click the top-right button or press any contextual slide button (`🤖 AI Anomaly Diagnostic`, etc.).
- **Voice Playback:** Click `🔊 Read Aloud` on any AI response.
