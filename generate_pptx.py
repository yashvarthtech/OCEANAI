import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # Set 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette - Deep Ocean Tech
    BG_DARK = RGBColor(7, 18, 36)        # Deep marine navy #071224
    CARD_BG = RGBColor(14, 30, 58)       # Elevated ocean card #0e1e3a
    CARD_BORDER = RGBColor(28, 58, 102)  # Card border #1c3a66
    CYAN_ACCENT = RGBColor(0, 229, 255)  # Bioluminescent cyan #00e5ff
    EMERALD_ACCENT = RGBColor(16, 185, 129) # Marine green #10b981
    AMBER_ACCENT = RGBColor(245, 158, 11)   # Warning amber #f59e0b
    WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(160, 185, 215) # Soft blue-grey
    TEXT_DIM = RGBColor(105, 130, 160)

    blank_layout = prs.slide_layouts[6] # Blank slide layout

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background() # No line
        return bg

    def add_header(slide, tag, title, subtitle=None):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf = tag_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.65))
        tf2 = title_box.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = WHITE

        if subtitle:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.4))
            tf3 = sub_box.text_frame
            tf3.word_wrap = True
            p3 = tf3.paragraphs[0]
            p3.text = subtitle
            p3.font.size = Pt(13)
            p3.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    # ==================== SLIDE 1: Title Slide ====================
    slide1 = prs.slides.add_slide(blank_layout)
    add_background(slide1)

    # Decorative banner card
    add_card(slide1, 1.2, 1.2, 10.933, 5.1, RGBColor(11, 24, 48), RGBColor(0, 229, 255))
    
    # SDG 14 Pill
    sdg_pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.8), Inches(1.6), Inches(3.6), Inches(0.45))
    sdg_pill.fill.solid()
    sdg_pill.fill.fore_color.rgb = RGBColor(0, 119, 182)
    sdg_pill.line.fill.background()
    p = sdg_pill.text_frame.paragraphs[0]
    p.text = "✦ UN SDG 14: LIFE BELOW WATER"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Project Title
    tb = slide1.shapes.add_textbox(Inches(1.8), Inches(2.2), Inches(9.8), Inches(1.4))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "OCEANGUARD AI"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p2 = tf.add_paragraph()
    p2.text = "Intelligent Ocean Protection & Sustainable Fishing Platform"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = WHITE

    # Tagline
    tb_tag = slide1.shapes.add_textbox(Inches(1.8), Inches(3.7), Inches(9.8), Inches(0.8))
    tf_tag = tb_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = "“Protect Our Oceans. Empower Our Fishers. Restore Our Future.”"
    p_tag.font.size = Pt(16)
    p_tag.font.italic = True
    p_tag.font.color.rgb = EMERALD_ACCENT

    # Pitch Summary
    tb_desc = slide1.shapes.add_textbox(Inches(1.8), Inches(4.4), Inches(9.8), Inches(1.2))
    tf_desc = tb_desc.text_frame
    tf_desc.word_wrap = True
    p_desc = tf_desc.paragraphs[0]
    p_desc.text = "An AI-powered, community-driven marine ecosystem uniting fishers, coastal communities, marine scientists, and authorities to monitor ocean health, detect illegal fishing in real-time, safeguard artisanal livelihoods, and guarantee verifiable seafood traceability."
    p_desc.font.size = Pt(13)
    p_desc.font.color.rgb = TEXT_MUTED

    # Bottom Meta Badges
    badges = [
        ("AI Anomaly Engine", CYAN_ACCENT),
        ("IoT & AIS Radar Watch", EMERALD_ACCENT),
        ("Blockchain Seafood Trace", AMBER_ACCENT),
        ("Fisher Voice Assistance", WHITE)
    ]
    for i, (b_text, col) in enumerate(badges):
        badge_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.8 + i * 2.45), Inches(5.6), Inches(2.3), Inches(0.45))
        badge_box.fill.solid()
        badge_box.fill.fore_color.rgb = RGBColor(18, 38, 70)
        badge_box.line.color.rgb = col
        badge_box.line.width = Pt(1)
        bp = badge_box.text_frame.paragraphs[0]
        bp.text = b_text
        bp.alignment = PP_ALIGN.CENTER
        bp.font.size = Pt(10)
        bp.font.bold = True
        bp.font.color.rgb = col

    # ==================== SLIDE 2: Vision & Mission ====================
    slide2 = prs.slides.add_slide(blank_layout)
    add_background(slide2)
    add_header(slide2, "Section 1 · Strategic Foundation", "Project Vision & Grand Mission", "Beyond mere monitoring: an active, incentivized restoration ecosystem")

    # Left Card: Vision
    add_card(slide2, 0.8, 1.8, 5.7, 5.0)
    vb = slide2.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.1), Inches(4.5))
    vtf = vb.text_frame
    vtf.word_wrap = True
    vp1 = vtf.paragraphs[0]
    vp1.text = "OUR VISION"
    vp1.font.size = Pt(18)
    vp1.font.bold = True
    vp1.font.color.rgb = CYAN_ACCENT

    vp2 = vtf.add_paragraph()
    vp2.text = "Create healthier oceans, sustainable fisheries, and economically resilient coastal communities through intelligent edge technology and collective action."
    vp2.font.size = Pt(14)
    vp2.font.color.rgb = WHITE
    vp2.space_before = Pt(10)

    v_points = [
        "Eliminate data blackouts across vulnerable coastal boundaries",
        "Empower artisanal fishers as verified ocean stewards, not violators",
        "Enable predictive conservation prior to catastrophic ecological collapse",
        "Foster economic circularity via direct fair-price seafood access"
    ]
    for pt in v_points:
        p = vtf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(8)

    # Right Card: Mission
    add_card(slide2, 6.8, 1.8, 5.7, 5.0)
    mb = slide2.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    mtf = mb.text_frame
    mtf.word_wrap = True
    mp1 = mtf.paragraphs[0]
    mp1.text = "OUR MISSION"
    mp1.font.size = Pt(18)
    mp1.font.bold = True
    mp1.font.color.rgb = EMERALD_ACCENT

    mp2 = mtf.add_paragraph()
    mp2.text = "Protect marine biodiversity, prevent illegal & unregulated fishing, and build a regenerative economic paradigm for small-scale fishing communities."
    mp2.font.size = Pt(14)
    mp2.font.color.rgb = WHITE
    mp2.space_before = Pt(10)

    m_points = [
        "Autonomous Early Warning: Real-time sensor & satellite alert loops",
        "Smart Livelihood Navigation: Micro-climate weather & safe species maps",
        "Ecosystem Restoration Ledger: Auditable mangrove & coral nurseries",
        "Consumer Trust Verification: Tamper-evident ocean-to-fork catch QR"
    ]
    for pt in m_points:
        p = mtf.add_paragraph()
        p.text = f"✔ {pt}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_MUTED
        p.space_before = Pt(8)

    # ==================== SLIDE 3: The Ocean Crisis ====================
    slide3 = prs.slides.add_slide(blank_layout)
    add_background(slide3)
    add_header(slide3, "Problem Context · UN SDG 14 Urgency", "The Critical Challenges Facing Life Below Water", "Fragmented governance, ecological degradation, and marginalized fishers")

    crises = [
        ("90%", "Predatory Fish Depleted", "Severe overfishing and illegal, unreported, unregulated (IUU) vessels encroaching onto protected breeding habitats without deterrence.", AMBER_ACCENT),
        ("11M Tons", "Annual Marine Plastic & Toxins", "Runoffs, industrial chemical dumping, oil spills, and acidification devastating fragile coral reefs and mangrove ecosystems.", CYAN_ACCENT),
        ("1 in 5", "Seafood Batches Illegally Harvested", "Opaque supply chains, counterfeit origins, and zero consumer transparency leaving honest small-scale fishers underpaid.", RGBColor(239, 68, 68)),
        ("3.3B+", "Humans Rely on Seafood Protein", "Coastal families face economic destitution when fish stocks collapse, yet top-down regulations criminalize them rather than collaborate.", EMERALD_ACCENT)
    ]

    for i, (stat, title, desc, col) in enumerate(crises):
        col_idx = i % 2
        row_idx = i // 2
        l = 0.8 + col_idx * 5.95
        t = 1.8 + row_idx * 2.5
        add_card(slide3, l, t, 5.75, 2.3)

        tb = slide3.shapes.add_textbox(Inches(l + 0.25), Inches(t + 0.15), Inches(5.25), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        
        sp = tf.paragraphs[0]
        sp.text = stat
        sp.font.size = Pt(28)
        sp.font.bold = True
        sp.font.color.rgb = col

        tp = tf.add_paragraph()
        tp.text = title
        tp.font.size = Pt(14)
        tp.font.bold = True
        tp.font.color.rgb = WHITE

        dp = tf.add_paragraph()
        dp.text = desc
        dp.font.size = Pt(11)
        dp.font.color.rgb = TEXT_MUTED
        dp.space_before = Pt(4)

    # ==================== SLIDE 4: The 6 Core Modules Overview ====================
    slide4 = prs.slides.add_slide(blank_layout)
    add_background(slide4)
    add_header(slide4, "Section 2 · Architectural Core", "The Six Powerful Core Modules of OCEANGUARD AI", "A holistic technological stack harmonizing detection, livelihoods, and conservation")

    modules = [
        ("M1", "AI Ocean Health Monitoring", "Multi-sensor IoT + satellite monitoring of pH, DO, turbidity, temperature & early warning for oil spills & plastic.", CYAN_ACCENT),
        ("M2", "Smart Illegal Fishing Detection", "AIS vessel pattern analysis, marine sanctuary geofencing, anomaly tracking, and crowdsourced community incident reports.", RGBColor(239, 68, 68)),
        ("M3", "Sustainable Fishing Assistant", "Hyper-local marine forecasts, sustainable quota advisories, restriction zone alerts, and vernacular voice guidance.", EMERALD_ACCENT),
        ("M4", "Marine Ecosystem Restoration", "Auditable records for mangrove plantings, coral micro-fragmentation reefs, seagrass acreage, and verified community cleanup drives.", CYAN_ACCENT),
        ("M5", "Blockchain Catch Traceability", "Unique QR codes for every catch batch, recording fisher ID, GPS landing coordinate, species, and cold-chain integrity.", AMBER_ACCENT),
        ("M6", "Community Rewards & Marketplace", "Tokenized conservation points, peer-to-peer fair-trade seafood marketplace, and economic rewards for ocean protection.", EMERALD_ACCENT)
    ]

    for i, (code, title, desc, col) in enumerate(modules):
        c = i % 3
        r = i // 3
        l = 0.8 + c * 3.97
        t = 1.8 + r * 2.55
        add_card(slide4, l, t, 3.8, 2.35)

        tb = slide4.shapes.add_textbox(Inches(l + 0.2), Inches(t + 0.15), Inches(3.4), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"{code} · {title}"
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(6)

    # ==================== SLIDE 5: Module 1 & 2 Deep Dive ====================
    slide5 = prs.slides.add_slide(blank_layout)
    add_background(slide5)
    add_header(slide5, "Deep Dive · Modules 1 & 2", "Autonomous Marine Health & Illegal Fishing Surveillance", "Detecting invisible pollutions and predatory vessels with edge intelligence")

    # Module 1 Card
    add_card(slide5, 0.8, 1.8, 5.7, 5.0)
    tb1 = slide5.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "MODULE 1: AI OCEAN HEALTH MONITORING"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    m1_items = [
        ("Sensor Telemetry", "Continuous tracking of temperature, pH, dissolved oxygen (DO), turbidity, and salinity via buoy-mounted ESP32 edge nodes."),
        ("Satellite Ingestion", "Harmonized Landsat/Sentinel earth observation data detecting surface oil sheens, red tides, and plastic accumulations."),
        ("AI Anomaly Scoring", "Isolation Forest & LSTM autoencoders flag statistical anomalies against baseline seasonal water profiles."),
        ("Community Incident Dispatch", "Instant automated SMS and voice alerts dispatched to maritime authorities and local panchayats.")
    ]
    for sub, desc in m1_items:
        p_sub = tf1.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    # Module 2 Card
    add_card(slide5, 6.8, 1.8, 5.7, 5.0)
    tb2 = slide5.shapes.add_textbox(Inches(7.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "MODULE 2: SMART ILLEGAL FISHING DETECTION"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)

    m2_items = [
        ("AIS Stream Analysis", "Live ingestion of public vessel Automatic Identification System (AIS) trajectories to track real-time craft movements."),
        ("Sanctuary Geofencing", "Dynamic virtual perimeters around Marine Protected Areas (MPAs) with zero-tolerance loitering alerts."),
        ("Heuristic Trawler Detection", "AI recognizes erratic speed shifts, nocturnal gear-trawling maneuvers, and sudden AIS transponder shutoffs."),
        ("Verified Community Tip-Offs", "Small-scale fishers report unregistered rogue vessels via one-touch geotagged photo uploads for priority review.")
    ]
    for sub, desc in m2_items:
        p_sub = tf2.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    # ==================== SLIDE 6: Module 3 & 4 Deep Dive ====================
    slide6 = prs.slides.add_slide(blank_layout)
    add_background(slide6)
    add_header(slide6, "Deep Dive · Modules 3 & 4", "Empowering Fishermen & Measuring Ecosystem Restoration", "Transitioning from punitive restrictions to regenerative, dignified livelihoods")

    add_card(slide6, 0.8, 1.8, 5.7, 5.0)
    tb3 = slide6.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "MODULE 3: SMART SUSTAINABLE FISHING ASSISTANT"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT

    m3_items = [
        ("Hyperlocal Weather & Sea State", "Real-time wave height, swell, wind direction, and squall warnings customized for small coastal catamarans."),
        ("Safe Fishery Advisory", "Recommends abundant, non-endangered pelagic species while signaling seasonal breeding closures."),
        ("Protected Species Visual AI", "On-device image classification helps fishers identify inadvertently netted endangered turtles and dolphins for safe release."),
        ("Vernacular Voice AI", "Voice-first conversational assistant in Tamil, Malayalam, Bengali, etc., ensuring zero literacy barrier.")
    ]
    for sub, desc in m3_items:
        p_sub = tf3.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    add_card(slide6, 6.8, 1.8, 5.7, 5.0)
    tb4 = slide6.shapes.add_textbox(Inches(7.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf4 = tb4.text_frame
    tf4.word_wrap = True
    p = tf4.paragraphs[0]
    p.text = "MODULE 4: MARINE ECOSYSTEM RESTORATION"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    m4_items = [
        ("Mangrove Afforestation Ledger", "GPS-polygon mapping of replanted Rhizophora saplings with canopy growth tracking."),
        ("Coral Reef Nursery Records", "Monitoring micro-fragmentation tile survival rates, temperature stress, and bleaching recoveries."),
        ("Seagrass Bed Protection", "Tracking carbon-sequestering seagrass meadows to prevent destructive bottom-trawling damage."),
        ("Verified Cleanup Missions", "Photo-verified beach and ghost-net retrieval campaigns rewarding volunteer fishers with tangible credentials.")
    ]
    for sub, desc in m4_items:
        p_sub = tf4.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    # ==================== SLIDE 7: Module 5 & 6 Deep Dive ====================
    slide7 = prs.slides.add_slide(blank_layout)
    add_background(slide7)
    add_header(slide7, "Deep Dive · Modules 5 & 6", "Cryptographic Seafood Traceability & Economic Marketplace", "Turning ocean conservation into direct household prosperity for coastal families")

    add_card(slide7, 0.8, 1.8, 5.7, 5.0)
    tb5 = slide7.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf5 = tb5.text_frame
    tf5.word_wrap = True
    p = tf5.paragraphs[0]
    p.text = "MODULE 5: BLOCKCHAIN SEAFOOD TRACEABILITY"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = AMBER_ACCENT

    m5_items = [
        ("Immutable Batch QR Codes", "Each landing batch receives a tamper-evident hash binding catch time, vessel ID, and landing dock."),
        ("Sustainable Method Verification", "Attestation certifying compliant gear (e.g. handline / selective gillnet) rather than destructive bottom trawls."),
        ("Cold Chain Logging", "Records temperature profiles between harbor auction, transit, and retail distribution counters."),
        ("Consumer Transparency Portal", "Diners and supermarkets scan QR codes on packaging to see the exact fisher, photo, and conservation credentials.")
    ]
    for sub, desc in m5_items:
        p_sub = tf5.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    add_card(slide7, 6.8, 1.8, 5.7, 5.0)
    tb6 = slide7.shapes.add_textbox(Inches(7.05), Inches(2.0), Inches(5.2), Inches(4.6))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "MODULE 6: COMMUNITY REWARDS & MARKETPLACE"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = EMERALD_ACCENT

    m6_items = [
        ("Conservation Credit Points", "Fishers earn digital tokens for reporting pollution, releasing bycatch, and participating in reef planting."),
        ("Direct Fisher-to-Buyer Market", "Bypasses predatory middlemen, enabling artisanal cooperatives to sell verified sustainable catches at premium margins (+25-40%)."),
        ("Live Fair-Price Index", "Transparent auction prices across major landing centers prevent exploitation of returning fishing vessels."),
        ("Welfare & Gear Subsidies", "Redeem earned credits for solar navigation lamps, biodegradable nets, life vests, and children's education stipends.")
    ]
    for sub, desc in m6_items:
        p_sub = tf6.add_paragraph()
        p_sub.text = f"• {sub}: {desc}"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_before = Pt(8)

    # ==================== SLIDE 8: System Workflow ====================
    slide8 = prs.slides.add_slide(blank_layout)
    add_background(slide8)
    add_header(slide8, "Section 3 · Execution Pipeline", "End-to-End System Workflow: From Wave to Consumer", "Closed-loop intelligence bridging sensor streams, AI analysis, and community action")

    steps = [
        ("STEP 1", "DATA INGESTION", "Buoy IoT Sensors\nCopernicus Satellites\nAIS Vessel Tracks\nFisher Voice/Photos", CYAN_ACCENT),
        ("STEP 2", "AI ENGINE", "Anomaly Detection\nIllegal Vessel Triage\nWater Quality Forecast\nSpecies Recognition", RGBColor(147, 51, 234)),
        ("STEP 3", "SMART DISPATCH", "Instant Coastal Alerts\nMarine Police Dashboard\nVernacular Fisher SMS\nRestoration Target Map", AMBER_ACCENT),
        ("STEP 4", "IMPACT & TRUST", "Rogue Vessel Interception\nRestoration Rewards\nFair Marketplace Sales\nConsumer QR Verification", EMERALD_ACCENT)
    ]

    for i, (num, title, desc, col) in enumerate(steps):
        l = 0.8 + i * 2.98
        add_card(slide8, l, 2.0, 2.8, 4.6)

        # Step indicator
        pill = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l + 0.2), Inches(2.2), Inches(1.3), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = col
        pill.line.fill.background()
        p = pill.text_frame.paragraphs[0]
        p.text = num
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = BG_DARK

        tb = slide8.shapes.add_textbox(Inches(l + 0.2), Inches(2.7), Inches(2.4), Inches(3.6))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(14)
        p1.font.bold = True
        p1.font.color.rgb = WHITE

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(12)

    # ==================== SLIDE 9: Real-World Tamil Nadu Scenario ====================
    slide9 = prs.slides.add_slide(blank_layout)
    add_background(slide9)
    add_header(slide9, "Operational Validation", "Real-World Deployment Scenario: Cuddalore Harbour, Tamil Nadu", "Step-by-step chronology of an anomaly detection and community response loop")

    timeline = [
        ("04:30 AM", "Offshore Telemetry Spike", "Buoy sensor #TN-04 reports sharp pH plunge (8.1 -> 6.8) and turbidity spike at 3 nautical miles offshore.", CYAN_ACCENT),
        ("04:32 AM", "AI Engine Anomaly Flag", "OCEANGUARD AI correlates satellite slick data and AIS tracking, tagging potential illegal chemical ballast discharge.", RGBColor(239, 68, 68)),
        ("04:35 AM", "Multilingual Community Alert", "Fishers receive audio notifications in Tamil: 'Avoid Sector 4 waters; proceed to Sector 7 for safe sardine harvesting.'", EMERALD_ACCENT),
        ("05:15 AM", "Crowdsourced Visual Verification", "Returning catamaran fishers submit geotagged photos confirming surface oil film; earn +50 conservation credits.", AMBER_ACCENT),
        ("06:00 AM", "Maritime Authority Action", "Coast Guard dispatches containment vessel to exact GPS polygon. Offender vessel flagged via historical AIS footprint.", CYAN_ACCENT),
        ("08:30 AM", "Direct Catch Auction & QR Trace", "Fishers land catch safely in uncontaminated waters, generating verified QR codes sold directly to buyers at 30% premium.", EMERALD_ACCENT)
    ]

    for i, (time, title, desc, col) in enumerate(timeline):
        c = i % 2
        r = i // 2
        l = 0.8 + c * 5.95
        t = 1.8 + r * 1.7
        add_card(slide9, l, t, 5.75, 1.55)

        tb = slide9.shapes.add_textbox(Inches(l + 0.2), Inches(t + 0.1), Inches(5.35), Inches(1.35))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"{time} — {title}"
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(3)

    # ==================== SLIDE 10: Tech Stack ====================
    slide10 = prs.slides.add_slide(blank_layout)
    add_background(slide10)
    add_header(slide10, "Section 4 · Engineering & AI", "Production Technology Stack & AI Architecture", "Robust, low-cost edge hardware, modern web stack, and resilient data models")

    # Table of Tech Stack
    rows = [
        ("Frontend & Presentation", "HTML5, CSS3, Modern Animated UI (inspomcp design system tokens), Chart.js", "Sub-second responsive dashboard, glassmorphism, responsive mobile portal"),
        ("Backend Services", "Python FastAPI / Flask REST Services, WebSockets", "High-throughput telemetry ingestion, JWT auth, realtime pub/sub alerts"),
        ("AI / ML Engine", "Scikit-Learn, PyTorch, Isolation Forest, LSTM, OpenCV", "Water quality anomaly scoring, AIS trajectory classification, marine species visual AI"),
        ("Data & Storage", "PostgreSQL (PostGIS), Firebase Realtime DB, Supabase", "Geospatial vector mapping, historical telemetry logs, immutable batch hashes"),
        ("Edge & IoT", "ESP32 microcontrollers, pH, DO, Turbidity, Temp Probes", "Ultra-low-power buoys solar-charged with LoRaWAN & GSM cellular backhaul"),
        ("Public Data Streams", "Copernicus Sentinel Satellites, Global Fishing Watch AIS", "Earth observation imagery, publicly available vessel identification feeds"),
        ("Cloud & Deployment", "Docker, Render, Google Cloud Run, Cloudflare CDN", "Scalable containerized deployment with edge caching and zero cold start")
    ]

    # Create Table Shape
    table_shape = slide10.shapes.add_table(len(rows) + 1, 3, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9))
    table = table_shape.table
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(4.3)
    table.columns[2].width = Inches(4.833)

    headers = ["Layer", "Technology", "Role & Hackathon Implementation"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(18, 38, 70)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CYAN_ACCENT

    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = CARD_BG if i % 2 == 0 else RGBColor(10, 22, 44)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = WHITE if j == 0 else TEXT_MUTED

    # ==================== SLIDE 11: Competitive Differentiators ====================
    slide11 = prs.slides.add_slide(blank_layout)
    add_background(slide11)
    add_header(slide11, "Section 5 · Strategic Advantage", "Competitive Differentiation: Why OCEANGUARD AI Wins", "Transforming ocean governance from siloed monitoring to an integrated human ecosystem")

    diffs = [
        ("Traditional Approaches", "OCEANGUARD AI Innovation", CYAN_ACCENT),
        ("Siloed, fragmented ocean sensors with no public action", "Single unified dashboard fusing IoT, satellites, AIS & community", EMERALD_ACCENT),
        ("Manual complaints hours after illegal fishing has occurred", "Autonomous AI anomaly triage flags rogue vessels in real time", CYAN_ACCENT),
        ("Top-down punitive regulations that alienate artisanal fishers", "Multilingual sustainable fishing assistant that guides & protects", EMERALD_ACCENT),
        ("Infrequent, unmeasured volunteer restoration events", "Continuous, GPS-verified restoration tracking ledger (mangroves/coral)", CYAN_ACCENT),
        ("Zero consumer catch transparency & rampant seafood mislabeling", "Verifiable QR code binding catch date, dock GPS & sustainable method", AMBER_ACCENT),
        ("Conservation acts as an unpaid economic penalty on fishers", "Tokenized rewards & direct-to-consumer marketplace with +30% margins", EMERALD_ACCENT)
    ]

    table_shape2 = slide11.shapes.add_table(len(diffs), 2, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    table2 = table_shape2.table
    table2.columns[0].width = Inches(5.8)
    table2.columns[1].width = Inches(5.933)

    for i, (left_text, right_text, col) in enumerate(diffs):
        cell_l = table2.cell(i, 0)
        cell_r = table2.cell(i, 1)

        if i == 0:
            cell_l.fill.solid()
            cell_l.fill.fore_color.rgb = RGBColor(18, 38, 70)
            cell_r.fill.solid()
            cell_r.fill.fore_color.rgb = RGBColor(18, 38, 70)
            p_l = cell_l.text_frame.paragraphs[0]
            p_l.text = left_text
            p_l.font.size = Pt(12)
            p_l.font.bold = True
            p_l.font.color.rgb = RGBColor(239, 68, 68)

            p_r = cell_r.text_frame.paragraphs[0]
            p_r.text = right_text
            p_r.font.size = Pt(12)
            p_r.font.bold = True
            p_r.font.color.rgb = CYAN_ACCENT
        else:
            cell_l.fill.solid()
            cell_l.fill.fore_color.rgb = CARD_BG if i % 2 == 1 else RGBColor(10, 22, 44)
            cell_r.fill.solid()
            cell_r.fill.fore_color.rgb = CARD_BG if i % 2 == 1 else RGBColor(10, 22, 44)

            p_l = cell_l.text_frame.paragraphs[0]
            p_l.text = f"✕ {left_text}"
            p_l.font.size = Pt(10)
            p_l.font.color.rgb = TEXT_MUTED

            p_r = cell_r.text_frame.paragraphs[0]
            p_r.text = f"✔ {right_text}"
            p_r.font.size = Pt(10)
            p_r.font.bold = True
            p_r.font.color.rgb = col

    # ==================== SLIDE 12: Impact & 6-Month Pilot ====================
    slide12 = prs.slides.add_slide(blank_layout)
    add_background(slide12)
    add_header(slide12, "Section 6 · Measurable Outcomes", "Expected Impact & 6-Month Field Pilot Targets", "Concrete milestones designed for rapid validation, stakeholder trust, and measurable ecology")

    # Left: 4 pillars
    pillars = [
        ("Ocean Health", "Improved water-quality tracking & rapid toxic spill response", CYAN_ACCENT),
        ("Fish Populations", "Safeguarded juvenile breeding zones & reduced bycatch mortality", EMERALD_ACCENT),
        ("Communities", "Fair market margins, vernacular safety alerts & digital literacy", AMBER_ACCENT),
        ("Ecosystems", "Restored mangrove canopies, coral micro-reefs & clean shorelines", CYAN_ACCENT)
    ]
    for i, (name, desc, col) in enumerate(pillars):
        t = 1.8 + i * 1.25
        add_card(slide12, 0.8, t, 5.7, 1.1)
        tb = slide12.shapes.add_textbox(Inches(1.0), Inches(t + 0.1), Inches(5.3), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = name
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = col
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED

    # Right: Measurable Pilot Targets (6 Months)
    add_card(slide12, 6.8, 1.8, 5.7, 5.0)
    tb_pilot = slide12.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
    tf_p = tb_pilot.text_frame
    tf_p.word_wrap = True
    p = tf_p.paragraphs[0]
    p.text = "SUGGESTED 6-MONTH PILOT TARGETS"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    targets = [
        ("100 Small-Scale Fishers", "Active onboarding across pilot harbor cluster with mobile app access."),
        ("5 Coastal Observation Zones", "Continuous water sensor array deployed along high-traffic estuaries."),
        ("10 Community Restoration Drives", "Measured mangrove plantings & coral micro-nurseries logged in system."),
        ("500 Verified Catch Batches", "Traceable QR codes scanned and authenticated by consumers & chefs."),
        ("5 Local Fisher Groups Trained", "Workshops on sustainable gear, safety apps, and digital auction pricing."),
        ("< 15 Min Incident Response", "Median time from sensor anomaly to community & authority notification.")
    ]
    for metric, detail in targets:
        p_m = tf_p.add_paragraph()
        p_m.text = f"🎯 {metric} — {detail}"
        p_m.font.size = Pt(11)
        p_m.font.color.rgb = TEXT_MUTED
        p_m.space_before = Pt(8)

    # ==================== SLIDE 13: Hackathon MVP Architecture ====================
    slide13 = prs.slides.add_slide(blank_layout)
    add_background(slide13)
    add_header(slide13, "Section 7 · Working Prototype", "The 5 Core Hackathon MVP Screens", "A complete, functional demonstration proving real-world viability on stage")

    screens = [
        ("Screen 1", "Auth & Role Selector", "Dual interface tailored for artisanal fishers, marine authorities, marine scientists, and seafood diners.", CYAN_ACCENT),
        ("Screen 2", "Ocean Health Monitor", "Real-time interactive dashboard displaying simulated live sensor telemetries (pH, DO, Turbidity, Temp) with risk heatmaps.", EMERALD_ACCENT),
        ("Screen 3", "AI Alert & Triage Center", "Pulsating radar map showcasing Marine Protected Area boundaries, vessel AIS tracks, and suspicious trawling alerts.", RGBColor(239, 68, 68)),
        ("Screen 4", "Fisher Community Portal", "Mobile-first vernacular guidance: local wave forecasts, sustainable fishing hotspots, species advisory, and token wallet.", AMBER_ACCENT),
        ("Screen 5", "Seafood QR Verification", "Public-facing consumer verification page decoding vessel ID, harvest GPS, and sustainability certificate.", CYAN_ACCENT)
    ]

    for i, (sc, title, desc, col) in enumerate(screens):
        t = 1.8 + i * 1.0
        add_card(slide13, 0.8, t, 11.733, 0.88)
        tb = slide13.shapes.add_textbox(Inches(1.0), Inches(t + 0.08), Inches(11.3), Inches(0.72))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"{sc.upper()} · {title}: "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col

        run = p.add_run()
        run.text = desc
        run.font.size = Pt(11)
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED

    # ==================== SLIDE 14: Final Pitch ====================
    slide14 = prs.slides.add_slide(blank_layout)
    add_background(slide14)

    add_card(slide14, 1.2, 1.0, 10.933, 5.5, RGBColor(11, 24, 48), CYAN_ACCENT)
    
    tb = slide14.shapes.add_textbox(Inches(1.6), Inches(1.3), Inches(10.1), Inches(4.9))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "SECTION 10 · THE WINNING HACKATHON PITCH"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN_ACCENT

    p1 = tf.add_paragraph()
    p1.text = "“Imagine a world where our oceans are protected, fish populations can recover, and fishermen can earn a sustainable living.”"
    p1.font.size = Pt(18)
    p1.font.italic = True
    p1.font.color.rgb = WHITE
    p1.space_before = Pt(10)

    p2 = tf.add_paragraph()
    p2.text = "Today our oceans face unprecedented threats: rampant illegal fishing, plastic accumulation, and habitat loss. Traditional solutions rely on punitive top-down rules that hurt vulnerable fishing families without solving the crisis."
    p2.font.size = Pt(12)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Our breakthrough is OCEANGUARD AI. By fusing AI anomaly detection, satellite & IoT telemetry, blockchain traceability, and community incentives, we transform coastal fishers from passive subjects into active ocean protectors."
    p3.font.size = Pt(12)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(8)

    p4 = tf.add_paragraph()
    p4.text = "Protect the Ocean. Empower the People. Secure the Future."
    p4.font.size = Pt(24)
    p4.font.bold = True
    p4.font.color.rgb = EMERALD_ACCENT
    p4.space_before = Pt(16)

    output_path = os.path.join(os.getcwd(), "OCEANGUARD_AI_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()
