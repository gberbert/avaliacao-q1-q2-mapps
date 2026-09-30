import os
import base64

# Read base64 logos
with open("/Users/gcostabe/dev/ACDC/assets/logo_mapfre.png", "rb") as f:
    b64_mapfre = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
with open("/Users/gcostabe/dev/ACDC/assets/logo_nttdata.png", "rb") as f:
    b64_ntt = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="docTitle">ACDC | Cockpit de Configuración Actuarial e IA — MAPFRE & NTT DATA</title>
  
  <!-- SEO & Meta Tags -->
  <meta name="description" content="Presentación Ejecutiva de la Plataforma ACDC (Automated Configuration & Definition Cockpit) para MAPFRE Seguros. Modernización de la capa MongoDB de Suscripción (DUP) y Tarifación (RTE Tronador) con Gobernanza PECA e IA Generativa Especializada.">
  <meta name="author" content="AS - MAPPS Brasil: Leandro Bruzzese, Gustavo Costa Berbert, Marcio Miguel">
  <link rel="icon" type="image/png" href="assets/logo_stacked.png">
  <link rel="apple-touch-icon" href="assets/logo_stacked.png">

  <!-- Open Graph / Rich Social Preview (Teams, WhatsApp, Slack, LinkedIn) -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://gberbert.github.io/mapps_br_acdc/">
  <meta property="og:title" content="ACDC Platform | Cockpit Actuarial e IA — MAPFRE & NTT DATA">
  <meta property="og:description" content="Presentación Ejecutiva de la Plataforma ACDC para MAPFRE Seguros. Modernización de la capa MongoDB de Suscripción (DUP) y Tarifación (RTE Tronador) con Gobernanza PECA e IA Generativa Especializada.">
  <meta property="og:image" content="https://gberbert.github.io/mapps_br_acdc/assets/og_preview.png">
  <meta property="og:image:secure_url" content="https://gberbert.github.io/mapps_br_acdc/assets/og_preview.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="NTT DATA & MAPFRE — ACDC Platform">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="ACDC Platform | Cockpit Actuarial e IA — MAPFRE & NTT DATA">
  <meta name="twitter:description" content="Presentación Ejecutiva de la Plataforma ACDC para MAPFRE Seguros.">
  <meta name="twitter:image" content="https://gberbert.github.io/mapps_br_acdc/assets/og_preview.png">
  <link rel="image_src" href="https://gberbert.github.io/mapps_br_acdc/assets/og_square.png">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- Chart.js via CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
    :root {{
      /* Dark Theme (Default) */
      --bg-primary: #070a13;
      --bg-surface: #0d1322;
      --bg-card: rgba(15, 23, 42, 0.78);
      --bg-card-hover: rgba(22, 34, 61, 0.88);
      --bg-glass: rgba(255, 255, 255, 0.035);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-highlight: rgba(0, 102, 255, 0.4);
      --border-subtle: rgba(255, 255, 255, 0.04);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      /* Brand Identity Colors */
      --ntt-blue: #0066ff;
      --ntt-blue-light: #38bdf8;
      --ntt-cyan: #00c0f3;
      --mapfre-red: #d31027;
      --mapfre-red-glow: rgba(211, 16, 39, 0.35);
      
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --purple: #8b5cf6;
      
      --shadow-lg: 0 20px 30px -10px rgba(0, 0, 0, 0.6), 0 8px 12px -6px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 25px rgba(0, 102, 255, 0.25);
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    [data-theme="light"] {{
      --bg-primary: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.94);
      --bg-card-hover: #ffffff;
      --bg-glass: rgba(0, 0, 0, 0.02);
      --border-color: rgba(0, 0, 0, 0.09);
      --border-highlight: rgba(0, 102, 255, 0.35);
      --border-subtle: rgba(0, 0, 0, 0.04);
      
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      
      --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.06), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --shadow-glow: 0 0 20px rgba(0, 102, 255, 0.12);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      transition: background-color 0.3s ease, color 0.3s ease;
      line-height: 1.5;
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Outfit', sans-serif;
      letter-spacing: -0.02em;
    }}

    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Top Navigation Bar - Single Line No Wrap */
    .topbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 68px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 1000;
      backdrop-filter: blur(14px);
      white-space: nowrap;
      gap: 16px;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 16px;
      flex-shrink: 0;
      white-space: nowrap;
      min-width: 0;
    }}

    /* Co-branded Logos Capsule: NTT DATA on top, MAPFRE on bottom */
    .brand-logos-capsule {{
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      background: #ffffff;
      padding: 4px 12px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.16);
      flex-shrink: 0;
      border: 1px solid rgba(255, 255, 255, 0.4);
      height: 50px;
      transition: var(--transition);
    }}

    .brand-logos-capsule:hover {{
      box-shadow: 0 4px 14px rgba(0, 102, 255, 0.25);
      transform: translateY(-1px);
    }}

    .header-logo-ntt {{
      height: 16px;
      width: auto;
      max-width: 88px;
      object-fit: contain;
      display: block;
    }}

    .logo-divider-v {{
      width: 48px;
      height: 1px;
      background: rgba(0, 0, 0, 0.18);
      flex-shrink: 0;
    }}

    .header-logo-mapfre {{
      height: 15px;
      width: auto;
      max-width: 88px;
      object-fit: contain;
      display: block;
    }}

    .brand-text-block {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      white-space: nowrap;
      flex-shrink: 0;
      line-height: 1.25;
    }}

    .brand-title-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .brand-title-main {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      white-space: nowrap;
      letter-spacing: -0.01em;
    }}

    .brand-title-divider {{
      color: var(--text-dim);
      font-size: 0.85rem;
      opacity: 0.5;
    }}

    .brand-title-tag {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      white-space: nowrap;
      letter-spacing: 0.01em;
    }}

    .brand-subtitle-line {{
      font-size: 0.76rem;
      color: var(--text-muted);
      white-space: nowrap;
      margin-top: 1px;
    }}

    @media (max-width: 1250px) {{
      .brand-subtitle-line {{ display: none; }}
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
      white-space: nowrap;
    }}

    .btn-nav {{
      white-space: nowrap !important;
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
      flex-shrink: 0;
      user-select: none;
    }}

    .btn-nav:hover {{
      background: var(--border-highlight);
      border-color: var(--ntt-blue-light);
      transform: translateY(-1px);
    }}

    .btn-nav:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }}

    .btn-primary-action {{
      background: var(--ntt-blue);
      color: white;
      border: none;
      font-weight: 600;
      box-shadow: 0 2px 10px rgba(0, 102, 255, 0.35);
    }}
    .btn-primary-action:hover {{
      background: #0052cc;
    }}

    .slide-counter {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 0.95rem;
      color: var(--ntt-cyan);
      min-width: 60px;
      text-align: center;
      background: var(--bg-glass);
      padding: 6px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      flex-shrink: 0;
      white-space: nowrap;
    }}

    /* Language Switcher */
    .lang-switcher {{
      display: flex;
      align-items: center;
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 2px;
      gap: 2px;
      flex-shrink: 0;
    }}

    .lang-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-family: 'Outfit', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 5px 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: var(--transition);
      line-height: 1;
    }}

    .lang-btn:hover {{
      color: var(--text-main);
    }}

    .lang-btn.active {{
      background: var(--ntt-blue);
      color: #ffffff;
      box-shadow: 0 1px 6px rgba(0, 102, 255, 0.4);
    }}

    /* Progress Bar */
    .progress-bar-container {{
      position: fixed;
      top: 68px;
      left: 0;
      right: 0;
      height: 4px;
      background: rgba(255, 255, 255, 0.05);
      z-index: 999;
    }}

    .progress-fill {{
      height: 100%;
      width: 10%;
      background: linear-gradient(90deg, var(--mapfre-red), var(--ntt-blue), var(--ntt-cyan));
      transition: width 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 0 10px rgba(0, 192, 243, 0.6);
    }}

    /* Deck Main Viewport */
    .deck-viewport {{
      margin-top: 72px;
      flex: 1;
      display: flex;
      position: relative;
      overflow: hidden;
      padding-bottom: 90px;
    }}

    .slide-container {{
      width: 100%;
      max-width: 1320px;
      margin: 0 auto;
      padding: 36px 32px 120px 32px;
      display: none;
      animation: slideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .slide-container.active {{
      display: block;
    }}

    @keyframes slideIn {{
      from {{ opacity: 0; transform: translateY(14px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Slide Typography */
    .slide-header {{
      margin-bottom: 28px;
    }}

    .slide-tag {{
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--ntt-cyan);
      margin-bottom: 8px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 192, 243, 0.1);
      border: 1px solid rgba(0, 192, 243, 0.25);
      padding: 4px 12px;
      border-radius: 999px;
    }}

    .slide-title {{
      font-size: 2.3rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.18;
      letter-spacing: -0.02em;
    }}

    .slide-subtitle {{
      font-size: 1.1rem;
      color: var(--text-muted);
      margin-top: 8px;
      max-width: 950px;
      line-height: 1.55;
    }}

    /* Hero Slide 1 Specifics */
    .hero-slide {{
      padding: 30px 0 20px 0;
    }}

    .hero-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, var(--ntt-blue), var(--ntt-cyan));
      color: white;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(0, 102, 255, 0.3);
    }}

    .mapfre-badge {{
      background: linear-gradient(135deg, #d31027, #b20d20);
      color: white;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}

    .hero-title {{
      font-size: 3.2rem;
      font-weight: 900;
      line-height: 1.1;
      letter-spacing: -0.03em;
      margin-bottom: 20px;
      background: linear-gradient(135deg, #ffffff 40%, var(--ntt-cyan) 85%, var(--ntt-blue) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    [data-theme="light"] .hero-title {{
      background: linear-gradient(135deg, #0f172a 40%, #0066ff 85%, #00c0f3 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-lead {{
      font-size: 1.25rem;
      color: var(--text-muted);
      max-width: 980px;
      margin-bottom: 34px;
      line-height: 1.6;
    }}

    /* Grids & Cards */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(440px, 1fr));
      gap: 24px;
      margin-bottom: 24px;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 22px;
      margin-bottom: 24px;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
      margin-bottom: 24px;
    }}

    .glass-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      backdrop-filter: blur(14px);
      transition: var(--transition);
    }}

    .glass-panel:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-3px);
      box-shadow: var(--shadow-glow);
    }}

    .panel-accent-bar {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--ntt-blue), var(--ntt-cyan));
    }}

    .panel-accent-red {{
      background: linear-gradient(90deg, var(--mapfre-red), #ff4d6d);
    }}

    .panel-accent-green {{
      background: linear-gradient(90deg, #10b981, #34d399);
    }}

    .panel-accent-purple {{
      background: linear-gradient(90deg, #8b5cf6, #c084fc);
    }}

    .panel-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }}

    .panel-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .panel-icon {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      background: rgba(0, 102, 255, 0.15);
      color: var(--ntt-cyan);
      border: 1px solid rgba(0, 102, 255, 0.3);
    }}

    .panel-icon.red {{
      background: rgba(211, 16, 39, 0.15);
      color: #ff4d6d;
      border-color: rgba(211, 16, 39, 0.3);
    }}

    .panel-icon.green {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.3);
    }}

    .panel-icon.purple {{
      background: rgba(139, 92, 246, 0.15);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.3);
    }}

    /* Metric Cards */
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 18px;
      margin-bottom: 26px;
    }}

    .metric-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 22px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      backdrop-filter: blur(12px);
      transition: var(--transition);
    }}

    .metric-card:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-3px);
    }}

    .metric-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--ntt-blue), var(--ntt-cyan));
    }}

    .metric-card.danger::before {{
      background: linear-gradient(90deg, var(--mapfre-red), #f43f5e);
    }}
    .metric-card.success::before {{
      background: linear-gradient(90deg, #10b981, #059669);
    }}
    .metric-card.purple::before {{
      background: linear-gradient(90deg, #8b5cf6, #a855f7);
    }}

    .metric-label {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}

    .metric-value {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.1;
      margin-bottom: 6px;
    }}

    .metric-sub {{
      font-size: 0.8rem;
      color: var(--text-dim);
    }}

    .metric-sub.positive {{
      color: var(--success);
      font-weight: 600;
    }}

    .metric-sub.warning {{
      color: var(--warning);
      font-weight: 600;
    }}

    /* Feature Lists */
    .feature-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .feature-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 0.925rem;
      color: var(--text-main);
      line-height: 1.5;
    }}

    .feature-bullet {{
      width: 20px;
      height: 20px;
      border-radius: 6px;
      background: rgba(0, 102, 255, 0.15);
      color: var(--ntt-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .feature-bullet.red {{
      background: rgba(211, 16, 39, 0.15);
      color: #ff4d6d;
    }}
    .feature-bullet.green {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
    }}

    /* Comparison Table / Box */
    .compare-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }}

    .compare-box {{
      border-radius: 14px;
      padding: 22px;
      border: 1px solid var(--border-color);
    }}

    .compare-box.before {{
      background: rgba(211, 16, 39, 0.05);
      border-color: rgba(211, 16, 39, 0.25);
    }}

    .compare-box.after {{
      background: rgba(16, 185, 129, 0.05);
      border-color: rgba(16, 185, 129, 0.3);
    }}

    .compare-header {{
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .compare-box.before .compare-header {{ color: #f43f5e; }}
    .compare-box.after .compare-header {{ color: #10b981; }}

    /* Code & Architecture Flow */
    .code-preview {{
      background: #040711;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      padding: 16px;
      font-size: 0.8rem;
      color: #38bdf8;
      overflow-x: auto;
      line-height: 1.6;
    }}

    .arch-flow-wrap {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 14px;
    }}

    .arch-node {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 18px;
      border-radius: 10px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      transition: var(--transition);
    }}

    .arch-node:hover {{
      border-color: var(--ntt-blue-light);
      background: var(--bg-card-hover);
    }}

    .arch-node-name {{
      font-weight: 700;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .arch-node-port {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      background: rgba(0, 102, 255, 0.15);
      color: var(--ntt-cyan);
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 600;
    }}

    /* Chart Containers */
    .chart-container {{
      position: relative;
      height: 280px;
      width: 100%;
      margin-top: 10px;
    }}

    /* Official Leadership Signature Card */
    .leadership-card {{
      margin-top: 28px;
      padding: 22px 28px;
      border-radius: 16px;
      background: linear-gradient(135deg, rgba(0, 102, 255, 0.07), rgba(0, 192, 243, 0.04));
      border: 1px solid var(--border-highlight);
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}

    .leadership-brand {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .leadership-pill {{
      background: linear-gradient(135deg, var(--ntt-blue), var(--ntt-cyan));
      color: white;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 8px;
      letter-spacing: 0.05em;
      box-shadow: 0 4px 12px rgba(0, 102, 255, 0.3);
    }}

    .leadership-members {{
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }}

    .leader-item {{
      display: flex;
      flex-direction: column;
    }}

    .leader-name {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text-main);
    }}

    .leader-role {{
      font-size: 0.8rem;
      color: var(--ntt-cyan);
    }}

    .leader-sep {{
      color: var(--border-color);
      font-size: 1.2rem;
      opacity: 0.5;
    }}

    /* Presenter Notes Bar (Collapsible Drawer at Bottom) */
    .presenter-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-color);
      z-index: 900;
      transform: translateY(calc(100% - 38px));
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 -10px 25px rgba(0, 0, 0, 0.35);
    }}

    .presenter-bar.open {{
      transform: translateY(0);
    }}

    .presenter-header {{
      height: 38px;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      background: var(--bg-card);
      user-select: none;
    }}

    .presenter-title {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .presenter-toggle-icon {{
      font-size: 0.75rem;
      color: var(--text-muted);
      transition: transform 0.2s ease;
    }}

    .presenter-bar.open .presenter-toggle-icon {{
      transform: rotate(180deg);
    }}

    .presenter-body {{
      padding: 18px 24px 24px 24px;
      max-height: 200px;
      overflow-y: auto;
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.6;
      border-top: 1px solid var(--border-subtle);
    }}

    
    /* Botón y Callout de Memoria de Cálculo */
    .calc-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(14, 165, 233, 0.15);
      border: 1px solid rgba(14, 165, 233, 0.45);
      color: #38bdf8;
      padding: 0.45rem 0.9rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.25s ease;
      box-shadow: 0 4px 12px rgba(14, 165, 233, 0.2);
    }}
    .calc-btn:hover {{
      background: rgba(14, 165, 233, 0.28);
      border-color: #38bdf8;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(14, 165, 233, 0.35);
    }}

    .calc-callout {{
      margin-top: 1rem;
      background: linear-gradient(90deg, rgba(14, 165, 233, 0.08), rgba(99, 102, 241, 0.08));
      border: 1px solid rgba(14, 165, 233, 0.25);
      border-radius: 12px;
      padding: 0.75rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .calc-callout:hover {{
      border-color: rgba(14, 165, 233, 0.5);
      background: linear-gradient(90deg, rgba(14, 165, 233, 0.14), rgba(99, 102, 241, 0.14));
    }}
    .calc-callout-link {{
      font-size: 0.78rem;
      font-weight: 600;
      color: #38bdf8;
      white-space: nowrap;
      margin-left: 1rem;
    }}

    .stat-calc-chip {{
      margin-top: 0.5rem;
      font-size: 0.68rem;
      padding: 2px 8px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      display: inline-block;
      transition: all 0.2s;
    }}
    .metric-card:hover .stat-calc-chip {{
      background: rgba(14, 165, 233, 0.2);
      border-color: rgba(14, 165, 233, 0.4);
      color: #38bdf8;
    }}

    /* Modal de Memoria de Cálculo */
    .calc-modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(10px);
      z-index: 2100;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}
    .calc-modal-overlay.open {{
      display: flex;
    }}
    .calc-modal-container {{
      width: 100%;
      max-width: 900px;
      max-height: 90vh;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0,0,0,0.85);
      animation: modalFadeIn 0.25s ease-out;
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .calc-modal-header {{
      padding: 1.25rem 1.75rem;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .calc-modal-tabs {{
      display: flex;
      background: rgba(0,0,0,0.25);
      border-bottom: 1px solid var(--border-color);
      padding: 0 1.5rem;
      overflow-x: auto;
      gap: 0.5rem;
    }}
    .calc-tab-btn {{
      padding: 0.85rem 1.1rem;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      border: none;
      background: none;
      cursor: pointer;
      border-bottom: 2px solid transparent;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .calc-tab-btn.active {{
      color: #38bdf8;
      border-bottom-color: #38bdf8;
    }}
    .calc-modal-body {{
      padding: 1.75rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .calc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.25rem;
    }}
    .calc-box-title {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--text-main);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .calc-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .calc-col {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      padding: 0.85rem 1rem;
      border-radius: 8px;
    }}
    .calc-col-label {{
      font-size: 0.72rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 0.35rem;
    }}
    .calc-col-val {{
      font-size: 0.85rem;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .calc-formula-banner {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.85rem 1.15rem;
      border-radius: 8px;
      font-family: monospace;
      font-size: 0.88rem;
      color: #6ee7b7;
      margin-bottom: 1rem;
    }}
    .calc-impact-box {{
      background: rgba(99, 102, 241, 0.08);
      border: 1px solid rgba(99, 102, 241, 0.25);
      padding: 0.85rem 1.15rem;
      border-radius: 8px;
      font-size: 0.84rem;
      color: #c7d2fe;
      line-height: 1.45;
    }}
    .modal-close-btn {{
      background: var(--mapfre-red);
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 700;
    }}

    /* Slide Navigation Modal / Drawer */
    .slide-drawer-modal {{
      display: none;
      position: fixed;
      top: 68px;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 2000;
      justify-content: flex-end;
    }}

    .slide-drawer-modal.open {{
      display: flex;
    }}

    .slide-drawer-panel {{
      width: 100%;
      max-width: 420px;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-color);
      height: 100%;
      padding: 24px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      animation: drawerSlide 0.25s ease-out;
    }}

    @keyframes drawerSlide {{
      from {{ transform: translateX(100%); }}
      to {{ transform: translateX(0); }}
    }}

    .drawer-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 14px;
      border-radius: 10px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      margin-bottom: 10px;
      cursor: pointer;
      transition: var(--transition);
    }}

    .drawer-item:hover, .drawer-item.active {{
      background: var(--border-highlight);
      border-color: var(--ntt-blue-light);
    }}

    .drawer-num {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      color: var(--ntt-cyan);
      font-size: 0.85rem;
      min-width: 32px;
    }}

    .drawer-label {{
      flex: 1;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-main);
      margin-left: 8px;
    }}

    /* Keyboard shortcuts helper bar */
    .shortcuts-bar {{
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 0.75rem;
      color: var(--text-dim);
      padding: 12px 0 0 0;
      flex-wrap: wrap;
    }}

    .key-badge {{
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-muted);
      font-size: 0.7rem;
    }}
  </style>
</head>
<body data-theme="dark">

  <!-- Top Navigation Bar -->
  <header class="topbar">
    <div class="brand-group">
      <!-- Official Co-branded Logos Capsule -->
      <div class="brand-logos-capsule" title="NTT DATA & MAPFRE">
        <img src="{b64_ntt}" alt="NTT DATA" class="header-logo-ntt">
        <div class="logo-divider-v"></div>
        <img src="{b64_mapfre}" alt="MAPFRE" class="header-logo-mapfre">
      </div>
      
      <div class="brand-text-block">
        <div class="brand-title-wrap">
          <span class="brand-title-main">ACDC Platform</span>
          <span class="brand-title-divider">|</span>
          <span class="brand-title-tag" data-i18n="topbar_title_tag">Cockpit Actuarial e IA</span>
        </div>
        <div class="brand-subtitle-line" data-i18n="topbar_subtitle">
          Modernización de la Capa MongoDB (DUP y RTE Tronador)
        </div>
      </div>
    </div>

    <div class="nav-actions">
      <!-- Language Switcher: ES (Default), EN, PTB -->
      <div class="lang-switcher" role="group" aria-label="Selector de idioma">
        <button class="lang-btn active" data-lang="es" onclick="setLanguage('es')" title="Español (Predeterminado)">ES</button>
        <button class="lang-btn" data-lang="en" onclick="setLanguage('en')" title="English">EN</button>
        <button class="lang-btn" data-lang="ptb" onclick="setLanguage('ptb')" title="Português do Brasil">PTB</button>
      </div>

      <button class="btn-nav" id="btnPrev" title="Slide Anterior (Seta Esquerda)"><span data-i18n="nav_prev">◀ Anterior</span></button>
      <div class="slide-counter" id="slideNumDisplay">01 / 10</div>
      <button class="btn-nav" id="btnNext" title="Próximo Slide (Seta Direita / Barra de Espaço)"><span data-i18n="nav_next">Siguiente ▶</span></button>
      
      <button class="btn-nav btn-primary-action" id="btnDrawer" title="Índice de Slides"><span data-i18n="nav_slides">📑 Diapositivas</span></button>
      <button class="btn-nav" id="btnNotes" title="Notas del Orador (Tecla N)"><span data-i18n="nav_notes">🎙️ Notas</span></button>
      <button class="btn-nav" id="btnFullscreen" title="Pantalla Completa (Tecla F)"><span data-i18n="nav_fullscreen">⛶ Pantalla Completa</span></button>
      <button class="btn-nav" id="btnTheme" title="Alternar Tema Claro/Oscuro (Tecla T)">☀️ / 🌙</button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div class="progress-fill" id="progress-fill"></div>
  </div>

  <!-- Deck Main Viewport -->
  <main class="deck-viewport">

    <!-- ==================== SLIDE 1: PORTADA EJECUTIVA ==================== -->
    <section class="slide-container active" data-slide="1">
      <div class="hero-slide">
        <div class="hero-badge-wrap">
          <span class="slide-tag" data-i18n="s1_tag">✨ Innovación & Gobernanza Actuarial • FY26</span>
          <span class="mapfre-badge">MAPFRE Seguros • BR-INT</span>
          <span class="brand-badge">Application Services — MAPPS Brasil</span>
        </div>
        
        <h1 class="hero-title" data-i18n="s1_title">
          ACDC: La Revolución en la Gestión de Configuraciones Actuariales
        </h1>
        
        <p class="hero-lead" data-i18n="s1_lead">
          De la capa MongoDB encapsulada y restrictiva al <strong>Cockpit Inteligente de Suscripción (DUP) y Tarifación (RTE Tronador)</strong> con estricta gobernanza, auditoría PECA lado a lado y auxilio de Inteligencia Artificial Generativa especializada.
        </p>

        <div class="metric-grid">
          <div class="metric-card success">
            <div class="metric-label" data-i18n="s1_m1_label">Time-to-Market de Nuevas Tarifas</div>
            <div class="metric-value" data-i18n="s1_m1_val">3 Horas</div>
            <div class="metric-sub positive" data-i18n="s1_m1_sub">▲ Reducción de 14 días a horas</div>
          </div>

          <div class="metric-card">
            <div class="metric-label" data-i18n="s1_m2_label">Prevención de Errores de Sintaxis</div>
            <div class="metric-value">98%</div>
            <div class="metric-sub positive" data-i18n="s1_m2_sub">Eliminación de fallos en producción</div>
          </div>

          <div class="metric-card danger">
            <div class="metric-label" data-i18n="s1_m3_label">Auditoría & Trazabilidad (PECA)</div>
            <div class="metric-value">100%</div>
            <div class="metric-sub positive" data-i18n="s1_m3_sub">Diff visual lado a lado pre-commit</div>
          </div>

          <div class="metric-card purple">
            <div class="metric-label" data-i18n="s1_m4_label">IA Actuarial Híbrida (Copilot)</div>
            <div class="metric-value">65% / 35%</div>
            <div class="metric-sub" data-i18n="s1_m4_sub">RAG Vectorial + Léxico Actuarial</div>
          </div>
        </div>

        <!-- Firma Oficial de Liderazgo -->
        <div class="leadership-card">
          <div class="leadership-brand">
            <div class="leadership-pill">AS - MAPPS BRASIL</div>
            <div>
              <div style="font-weight: 700; font-size: 0.95rem;" data-i18n="lead_box_title">Liderazgo & Gobernanza Ejecutiva</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);" data-i18n="lead_box_sub">Sponsorship Estratégico & Arquitectura de la Solución ACDC</div>
            </div>
          </div>

          <div class="leadership-members">
            <div class="leader-item">
              <span class="leader-name">Leandro Bruzzese</span>
              <span class="leader-role">Head MAPPS Brasil</span>
            </div>
            <span class="leader-sep">|</span>
            <div class="leader-item">
              <span class="leader-name">Gustavo Costa Berbert</span>
              <span class="leader-role" data-i18n="lead_role_gustavo">Director de MAPPS</span>
            </div>
            <span class="leader-sep">|</span>
            <div class="leader-item">
              <span class="leader-name">Marcio Miguel</span>
              <span class="leader-role" data-i18n="lead_role_marcio">Arquitecto IA MAPPS</span>
            </div>
          </div>
        </div>

        <div class="shortcuts-bar">
          <span data-i18n="shortcuts_title">Navegación:</span>
          <span><span class="key-badge">◀</span> / <span class="key-badge">▶</span> <span data-i18n="sc_arrows">Flechas</span></span>
          <span><span class="key-badge">Espacio</span> <span data-i18n="sc_space">Avanzar</span></span>
          <span><span class="key-badge">F</span> <span data-i18n="sc_fullscreen">Pantalla Completa</span></span>
          <span><span class="key-badge">N</span> <span data-i18n="sc_notes">Notas</span></span>
          <span><span class="key-badge">T</span> <span data-i18n="sc_theme">Tema</span></span>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 2: DIAGNÓSTICO ==================== -->
    <section class="slide-container" data-slide="2">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s2_tag">Diagnóstico Crítico</span>
        <h2 class="slide-title" data-i18n="s2_title">El Reto Estratégico: MongoDB como "Caja Negra"</h2>
        <p class="slide-subtitle" data-i18n="s2_subtitle">Cómo la ausencia de una capa frontend generaba lentitud, riesgos operacionales y sobrecostes técnicos en MAPFRE.</p>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-red"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon red">⚠️</div>
              <span data-i18n="s2_p1_title">El Escenario Pre-ACDC (Sin Interfaz)</span>
            </div>
          </div>
          <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 16px;" data-i18n="s2_p1_desc">
            MAPFRE adoptó MongoDB como capa unificada y encapsulada para persistir las definiciones del motor Tronador (RTE) y las reglas de suscripción (DUP). Sin embargo, <strong>no existía ninguna interfaz gráfica frontend</strong>.
          </p>
          <ul class="feature-list">
            <li class="feature-item">
              <span class="feature-bullet red">1</span>
              <div data-i18n="s2_bullet1">
                <strong>Ediciones Manuales vía Scripts o CLI:</strong> Cualquier ajuste de tarifa o constante exigía la intervención de DBAs o desarrolladores con scripts JSON crudos directamente en la base.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet red">2</span>
              <div data-i18n="s2_bullet2">
                <strong>Alto Riesgo de Caída en Producción:</strong> Errores de tipeo, comas ausentes o tipos incompatibles podían colapsar el pipeline de cotizaciones de seguros a nivel nacional.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet red">3</span>
              <div data-i18n="s2_bullet3">
                <strong>Time-to-Market Inviable:</strong> Lanzar o modificar un producto o paquete de coberturas demoraba semanas entre colas de TI, homologación e inyección manual.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet red">4</span>
              <div data-i18n="s2_bullet4">
                <strong>Apagón de Auditoría Visual:</strong> Imposible comparar el estado anterior y el nuevo formato JSON lado a lado antes de persistir la alteración final.
              </div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-green"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon green">🎯</div>
              <span data-i18n="s2_p2_title">La Oportunidad Transformadora</span>
            </div>
          </div>
          <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 16px;" data-i18n="s2_p2_desc">
            ACDC fue concebido como un <strong>Cockpit Empresarial de Alta Disponibilidad</strong> que desbloquea el valor de los datos sin comprometer la estricta seguridad de MAPFRE.
          </p>
          <div class="compare-container">
            <div class="compare-box before">
              <div class="compare-header" data-i18n="s2_before_head">❌ Antes (Legado Manual)</div>
              <ul style="font-size: 0.8rem; color: var(--text-muted); list-style: none; display: flex; flex-direction: column; gap: 8px;">
                <li data-i18n="s2_bef_1">• Cola de 10-15 días para TI</li>
                <li data-i18n="s2_bef_2">• Edición a ciegas de JSONs complejos</li>
                <li data-i18n="s2_bef_3">• Test manual post-inyección</li>
                <li data-i18n="s2_bef_4">• Dudas actuariales sin soporte guiado</li>
                <li data-i18n="s2_bef_5">• Auditoría fragmentada en logs de servidor</li>
              </ul>
            </div>
            <div class="compare-box after">
              <div class="compare-header" data-i18n="s2_after_head">✅ Después (Plataforma ACDC)</div>
              <ul style="font-size: 0.8rem; color: var(--text-muted); list-style: none; display: flex; flex-direction: column; gap: 8px;">
                <li data-i18n="s2_aft_1">• Autonomía en tiempo real (horas)</li>
                <li data-i18n="s2_aft_2">• Constructor visual dual-pane</li>
                <li data-i18n="s2_aft_3">• Validación sintáctica & IA instantánea</li>
                <li data-i18n="s2_aft_4">• ACDC Copilot con RAG Híbrido</li>
                <li data-i18n="s2_aft_5">• 100% Auditable (PECA Diff Modal)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 3: VISIÓN HOLÍSTICA ==================== -->
    <section class="slide-container" data-slide="3">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s3_tag">Visión de la Solución</span>
        <h2 class="slide-title" data-i18n="s3_title">Plataforma ACDC: El Cockpit Definitivo de MAPFRE</h2>
        <p class="slide-subtitle" data-i18n="s3_subtitle">Una experiencia moderna que unifica Actuaría, Suscripción de Riesgos y TI en una plataforma visual blindada.</p>
      </div>

      <div class="grid-3">
        <div class="glass-panel">
          <div class="panel-accent-bar"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">⚡</div>
              <span data-i18n="s3_c1_title">Motor RTE (Rating Engine)</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px;" data-i18n="s3_c1_desc">
            Editor visual dual-pane para el motor Tronador. Parametrización de <strong>fórmulas matemáticas</strong>, diccionario de variables (<code>VAR</code>), constantes (<code>CTE</code>), conceptos económicos y bases técnicas.
          </p>
          <div style="font-size: 0.78rem; background: var(--bg-surface); padding: 8px 12px; border-radius: 8px; border: 1px solid var(--border-color); color: var(--ntt-cyan);">
            Colecciones: FORMULA-DEFINITION, ECONOMIC-CONCEPTS, TECHNICAL-BASIS
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-purple"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon purple">🛡️</div>
              <span data-i18n="s3_c2_title">Motor DUP (Underwriting)</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px;" data-i18n="s3_c2_desc">
            Gestión inteligente de <strong>reglas de riesgo y suscripción dinámica</strong>. Control de Loss Ratio, límites de capital, triaje antifraude y vinculación a paquetes de coberturas comerciales.
          </p>
          <div style="font-size: 0.78rem; background: var(--bg-surface); padding: 8px 12px; border-radius: 8px; border: 1px solid var(--border-color); color: var(--purple);">
            Colecciones: RULES, RS-RULES, RS-RULES-ACTIONS-CONDITIONS, PRODUCTS
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-green"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon green">🤖</div>
              <span data-i18n="s3_c3_title">ACDC Copilot (IA RAG)</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 14px;" data-i18n="s3_c3_desc">
            Asistente cognitivo embebido entrenado en la <strong>ontología actuarial de MAPFRE</strong>. Responde dudas en lenguaje natural, analiza fórmulas y sugiere correcciones instantáneas vía RAG Híbrido.
          </p>
          <div style="font-size: 0.78rem; background: var(--bg-surface); padding: 8px 12px; border-radius: 8px; border: 1px solid var(--border-color); color: var(--success);">
            Gateway: :8766 (Python) • gpt-5.6-terra-high & text-embedding-3-small
          </div>
        </div>
      </div>

      <div class="glass-panel">
        <div class="panel-header">
          <div class="panel-title">
            <div class="panel-icon">🏛️</div>
            <span data-i18n="s3_gov_title">Gobernanza, Pista PECA & Multi-Ambiente</span>
          </div>
          <span style="font-size: 0.8rem; font-weight: 700; color: var(--ntt-cyan); background: rgba(0,192,243,0.1); padding: 4px 10px; border-radius: 6px;">COMPLIANCE REGULATORIO</span>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;" data-i18n="s3_gov_desc">
          Control de acceso granular basado en roles (<strong>ADMIN, ESCRITURA, LECTURA</strong>), integración nativa con <strong>Okta OIDC SSO corporativo</strong>, pista de auditoría <code>PECA</code> con visualizador de diff JSON lado a lado antes de guardar y <strong>alternancia dinámica de servidores MongoDB</strong> (Local Docker ⇄ Cluster Remoto MAPFRE) en tiempo de ejecución sin reiniciar la aplicación.
        </p>
      </div>
    </section>

    <!-- ==================== SLIDE 4: ARQUITECTURA TÉCNICA ==================== -->
    <section class="slide-container" data-slide="4">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s4_tag">Ingeniería de Software</span>
        <h2 class="slide-title" data-i18n="s4_title">Arquitectura Técnica de Grado Corporativo</h2>
        <p class="slide-subtitle" data-i18n="s4_subtitle">Aislamiento estricto de puertos, conectividad resiliente e integración segura con la infraestructura corporativa.</p>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">⚙️</div>
              <span data-i18n="s4_t1_title">Topología & Stack Tecnológico</span>
            </div>
          </div>
          
          <div class="arch-flow-wrap">
            <div class="arch-node">
              <div class="arch-node-name">
                <span>💻</span>
                <div>
                  <div data-i18n="s4_n1_title">Frontend Cockpit (SPA)</div>
                  <div style="font-size: 0.75rem; color: var(--text-dim);" data-i18n="s4_n1_sub">React 19 + Vite 8 • Vanilla Design NTT DATA</div>
                </div>
              </div>
              <div class="arch-node-port">Port 5173</div>
            </div>

            <div class="arch-node">
              <div class="arch-node-name">
                <span>🌐</span>
                <div>
                  <div data-i18n="s4_n2_title">Servidor de Aplicación Backend</div>
                  <div style="font-size: 0.75rem; color: var(--text-dim);" data-i18n="s4_n2_sub">Node.js 24 + Express • JWT & Pools Dinámicos</div>
                </div>
              </div>
              <div class="arch-node-port">Port 4000</div>
            </div>

            <div class="arch-node">
              <div class="arch-node-name">
                <span>🤖</span>
                <div>
                  <div data-i18n="s4_n3_title">Local AI Gateway (Python 3.11)</div>
                  <div style="font-size: 0.75rem; color: var(--text-dim);" data-i18n="s4_n3_sub">Reverse Proxy AXET • Okta OIDC SSO • gpt-5.6</div>
                </div>
              </div>
              <div class="arch-node-port">Port 8766</div>
            </div>

            <div class="arch-node">
              <div class="arch-node-name">
                <span>🍃</span>
                <div>
                  <div data-i18n="s4_n4_title">Cluster MongoDB 7.0</div>
                  <div style="font-size: 0.75rem; color: var(--text-dim);" data-i18n="s4_n4_sub">acdc_dup_br-int & acdc_rte_br-int</div>
                </div>
              </div>
              <div class="arch-node-port">Port 27017</div>
            </div>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon green">🔒</div>
              <span data-i18n="s4_t2_title">Pilares de Seguridad & Resiliencia</span>
            </div>
          </div>
          
          <ul class="feature-list">
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s4_sec_1">
                <strong>Zero-Downtime Environment Switch:</strong> El backend cuenta con un pool dinámico gestionado por <code>environmentService.js</code>, permitiendo alternar de base local a servidores remotos corporativos con prueba previa de latencia y sin reiniciar Node.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s4_sec_2">
                <strong>Fallback Seguro Automático:</strong> En caso de interrupción en la VPN o servidor corporativo remoto, el sistema realiza fallback automático al contenedor Docker local, manteniendo la plataforma 100% funcional.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s4_sec_3">
                <strong>Blindaje de Credenciales:</strong> Los tokens de autenticación Okta y cadenas de conexión MongoDB se aíslan fuera del control de versiones mediante un <code>.gitignore</code> estricto.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s4_sec_4">
                <strong>Instalación en 1 Clic:</strong> Scripts automatizados (<code>setup_mac.sh</code> e <code>instalar_windows.bat</code>) configuran dependencias y crean accesos directos en el escritorio para el uso diario sin fricción técnica.
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 5: MOTOR TRONADOR (RTE) ==================== -->
    <section class="slide-container" data-slide="5">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s5_tag">Módulo Central</span>
        <h2 class="slide-title" data-i18n="s5_title">Motor RTE: El Constructor Visual Dual-Pane</h2>
        <p class="slide-subtitle" data-i18n="s5_subtitle">Cómo transformamos la complejidad de fórmulas actuariales en una experiencia ágil y a prueba de fallos.</p>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">🧮</div>
              <span data-i18n="s5_t1_title">Funcionalidades del Editor Actuarial</span>
            </div>
          </div>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 14px;" data-i18n="s5_t1_desc">
            El componente <code>RatingEngineTab.jsx</code> fue desarrollado para eliminar por completo la necesidad de edición directa de JSONs en la colección <code>FORMULA-DEFINITION</code>.
          </p>
          <ul class="feature-list">
            <li class="feature-item">
              <span class="feature-bullet">1</span>
              <div data-i18n="s5_b1">
                <strong>Catálogo de Objetos Actuariales:</strong> Navegación ágil por Variables (<code>VAR</code>), Constantes Globales (<code>CTE</code>), Funciones Matemáticas (<code>FN</code>) y Operadores Lógicos.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">2</span>
              <div data-i18n="s5_b2">
                <strong>Montaje Visual por Arrastre o Clic:</strong> Los bloques actuariales se insertan directamente en el flujo de cálculo con resaltado de sintaxis según el tipo de dato.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">3</span>
              <div data-i18n="s5_b3">
                <strong>Validación Sintáctica Determinista:</strong> El motor valida paréntensis, balanceo, ámbito de variables y operadores antes de permitir la persistencia.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">4</span>
              <div data-i18n="s5_b4">
                <strong>Verificación de Sanidad Actuarial por IA:</strong> El Copilot analiza la fórmula y comprueba si los coeficientes están dentro de los rangos estadísticos esperados.
              </div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon purple">📊</div>
              <span data-i18n="s5_t2_title">Colecciones RTE Bajo Gobernanza Visual</span>
            </div>
          </div>
          <div class="code-preview" style="margin-bottom: 14px;">
// Objeto de Fórmula en ACDC (JSON Validado)
{{
  "formulaId": "FML_AUTO_CASCO_01",
  "name": "Prima Base - Seguro Automóvil Flotas",
  "branch": "BR-INT_AUTO",
  "expression": "VAR[IS_VALOR_VEHICULO] * CTE[TASA_BASE] * FN[FACTOR_BONUS(VAR[CLASE_BONUS])]",
  "status": "HOMOLOGADO",
  "audit": {{ "pecaId": "PEC-2026-9812", "author": "actuaria@mapfre.com" }}
}}
          </div>
          <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;" data-i18n="s5_t2_desc">
            Además de fórmulas, el sistema administra tablas de bases técnicas (<code>TECHNICAL-BASIS-TABLES</code>), conceptos económicos (<code>ECONOMIC-CONCEPTS</code>) y planes de pago (<code>PAYMENT-PLANS</code>).
          </p>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 6: SUSCRIPCIÓN DINÁMICA (DUP) ==================== -->
    <section class="slide-container" data-slide="6">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s6_tag">Suscripción & Productos</span>
        <h2 class="slide-title" data-i18n="s6_title">Módulo DUP: Suscripción Dinámica & Catálogo</h2>
        <p class="slide-subtitle" data-i18n="s6_subtitle">Flexibilidad comercial con control absoluto sobre reglas de riesgo y paquetes de coberturas.</p>
      </div>

      <div class="grid-3">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">⚖️</div>
              <span data-i18n="s6_c1_title">Reglas de Riesgo (RULES)</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;" data-i18n="s6_c1_desc">
            Editor especializado en <code>RiskRulesTab.jsx</code> para reglas de selección y exclusión (<code>RULES</code>, <code>RS-RULES</code>).
          </p>
          <ul style="font-size: 0.82rem; color: var(--text-dim); list-style: none; display: flex; flex-direction: column; gap: 6px;">
            <li data-i18n="s6_c1_i1">• Parametrización de Loss Ratio máximo</li>
            <li data-i18n="s6_c1_i2">• Límites de aceptación por código postal y flota</li>
            <li data-i18n="s6_c1_i3">• Reglas de recargo automático</li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon purple">📦</div>
              <span data-i18n="s6_c2_title">Paquetes de Coberturas</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;" data-i18n="s6_c2_desc">
            Estructuración de paquetes de pólizas mediante <code>CoveragePackagesTab.jsx</code>.
          </p>
          <ul style="font-size: 0.82rem; color: var(--text-dim); list-style: none; display: flex; flex-direction: column; gap: 6px;">
            <li data-i18n="s6_c2_i1">• Paquetes Básico, Intermedio y Óptimo</li>
            <li data-i18n="s6_c2_i2">• Vinculación directa a códigos de tarifación RTE</li>
            <li data-i18n="s6_c2_i3">• Activación instantánea para cotizaciones</li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon green">🔍</div>
              <span data-i18n="s6_c3_title">Triangulación Antifraude</span>
            </div>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 12px;" data-i18n="s6_c3_desc">
            Gobernanza de la colección <code>TRIANGULATION_KEYS</code> y mitigación de riesgo moral en la contratación.
          </p>
          <ul style="font-size: 0.82rem; color: var(--text-dim); list-style: none; display: flex; flex-direction: column; gap: 6px;">
            <li data-i18n="s6_c3_i1">• Cruce de siniestralidad histórica</li>
            <li data-i18n="s6_c3_i2">• Verificación de flotas duplicadas</li>
            <li data-i18n="s6_c3_i3">• Bloqueo preventivo de propuestas</li>
          </ul>
        </div>
      </div>

      <div class="glass-panel">
        <div class="panel-header">
          <div class="panel-title">
            <div class="panel-icon">🗺️</div>
            <span data-i18n="s6_sync_title">Sincronización Bidireccional con la Capa Relacional Oracle</span>
          </div>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.5;" data-i18n="s6_sync_desc">
          La pestaña <code>DataImportTab.jsx</code> y el pipeline de importación permiten la ingesta estructurada de metadatos relacionales directamente desde bases legadas Oracle de MAPFRE (ej: <code>BASE ORACLE REEF</code>), traduciendo tablas relacionales en documentos JSON optimizados para MongoDB sin intervención manual.
        </p>
      </div>
    </section>

    <!-- ==================== SLIDE 7: GOBERNANZA & AUDITORÍA PECA ==================== -->
    <section class="slide-container" data-slide="7">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s7_tag">Compliance & Auditoría</span>
        <h2 class="slide-title" data-i18n="s7_title">Gobernanza Innegociable: Pista PECA & Diff Visual</h2>
        <p class="slide-subtitle" data-i18n="s7_subtitle">Cómo ACDC garantiza 100% de conformidad regulatoria y trazabilidad absoluta de cada carácter modificado.</p>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon red">📜</div>
              <span data-i18n="s7_p1_title">El Estándar de Auditoría PECA</span>
            </div>
          </div>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 14px;" data-i18n="s7_p1_desc">
            La auditoría no es un log pasivo, sino un requisito mandatorio de sistema implementado en <code>AuditTab.jsx</code> y en la colección <code>PECA</code>.
          </p>
          <ul class="feature-list">
            <li class="feature-item">
              <span class="feature-bullet red">✓</span>
              <div data-i18n="s7_b1">
                <strong>Identidad Corporativa Registrada:</strong> Toda alteración lleva la firma Okta OIDC del usuario, rol funcional y timestamp UTC inviolable.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet red">✓</span>
              <div data-i18n="s7_b2">
                <strong>Side-by-Side Visual Diff:</strong> Antes de confirmar cualquier grabación, el usuario visualiza un modal con la comparación línea a línea del JSON (Verde = Añadido / Rojo = Eliminado).
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet red">✓</span>
              <div data-i18n="s7_b3">
                <strong>Histórico de Reversión (Rollback):</strong> Capacidad de restaurar versiones anteriores de fórmulas o reglas en 1 clic ante cualquier eventualidad operativa.
              </div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">👥</div>
              <span data-i18n="s7_p2_title">Matriz de Control de Acceso (RBAC)</span>
            </div>
          </div>
          <div style="overflow-x: auto; margin-top: 10px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem; color: var(--text-main);">
              <thead>
                <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                  <th style="padding: 10px 8px; color: var(--text-muted);" data-i18n="s7_th_role">Rol</th>
                  <th style="padding: 10px 8px; color: var(--text-muted);" data-i18n="s7_th_view">Visualización</th>
                  <th style="padding: 10px 8px; color: var(--text-muted);" data-i18n="s7_th_edit">Edición Fórmulas/Reglas</th>
                  <th style="padding: 10px 8px; color: var(--text-muted);" data-i18n="s7_th_admin">Gestión Entornos e IA</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 12px 8px; font-weight: 700; color: #10b981;" data-i18n="s7_r1_name">LECTURA</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r1_c1">✅ Catálogo & Explorador</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r1_c2">❌ Bloqueado</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r1_c3">❌ Bloqueado</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-color);">
                  <td style="padding: 12px 8px; font-weight: 700; color: #00c0f3;" data-i18n="s7_r2_name">ESCRITURA</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r2_c1">✅ Completo</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r2_c2">✅ Crear/Editar con Diff</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r2_c3">❌ Bloqueado</td>
                </tr>
                <tr>
                  <td style="padding: 12px 8px; font-weight: 700; color: #8b5cf6;" data-i18n="s7_r3_name">ADMIN</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r3_c1">✅ Irrestricto</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r3_c2">✅ Irrestricto</td>
                  <td style="padding: 12px 8px;" data-i18n="s7_r3_c3">✅ Conexiones, Usuarios, Okta</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div style="margin-top: 16px; font-size: 0.8rem; color: var(--text-dim); background: var(--bg-surface); padding: 10px; border-radius: 8px;" data-i18n="s7_admin_note">
            Las aprobaciones pendientes de nuevos usuarios se muestran con contador visual en el menú de Administración para acción inmediata del Master Admin.
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 8: ACDC COPILOT ==================== -->
    <section class="slide-container" data-slide="8">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s8_tag">Inteligencia Artificial</span>
        <h2 class="slide-title" data-i18n="s8_title">ACDC Copilot: IA Generativa con Contexto Actuarial</h2>
        <p class="slide-subtitle" data-i18n="s8_subtitle">Por qué las IAs genéricas fallan y cómo nuestro RAG Híbrido especializado resuelve dudas y audita reglas en segundos.</p>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon purple">🧠</div>
              <span data-i18n="s8_t1_title">Arquitectura RAG Híbrida Especializada</span>
            </div>
          </div>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 14px;" data-i18n="s8_t1_desc">
            Modelos de IA genéricos desconocen el vocabulario Tronador, los códigos de cobertura de MAPFRE y la estructura de colecciones. ACDC Copilot emplea una ingeniería propietaria:
          </p>
          <ul class="feature-list">
            <li class="feature-item">
              <span class="feature-bullet purple">65%</span>
              <div data-i18n="s8_b1">
                <strong>Similaridad Vectorial por Coseno:</strong> Vectorización densa en 1536 dimensiones vía <code>text-embedding-3-small</code> sobre toda la documentación y manuales actuariales.
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet purple">35%</span>
              <div data-i18n="s8_b2">
                <strong>Correspondencia Léxica Actuarial:</strong> Ponderación exacta por identificadores de negocio (ej: <code>RS-RULES</code>, <code>G2002151</code>, ramos y fórmulas).
              </div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet purple">⚡</span>
              <div data-i18n="s8_b3">
                <strong>Modelos de Razonamiento Avanzado:</strong> Integración con <code>gpt-5.6-terra-high</code> para auditoría determinista y razonamiento lógico en cálculos matemáticos.
              </div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">💬</div>
              <span data-i18n="s8_t2_title">Casos Reales Atendidos por el Copilot</span>
            </div>
          </div>
          
          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 10px; padding: 12px;">
              <div style="font-size: 0.75rem; color: var(--ntt-cyan); font-weight: 700; margin-bottom: 4px;" data-i18n="s8_q1_tag">PREGUNTA DEL ACTUARIO:</div>
              <div style="font-size: 0.85rem; color: var(--text-main); font-style: italic;" data-i18n="s8_q1_text">
                "¿Cómo se calcula el factor de recargo por edad del conductor en la fórmula FML_AUTO_03?"
              </div>
              <div style="font-size: 0.75rem; color: var(--success); font-weight: 700; margin-top: 8px;" data-i18n="s8_a1_tag">RESPUESTA DEL COPILOT (550ms):</div>
              <div style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4;" data-i18n="s8_a1_text">
                "La fórmula consulta la tabla técnica <code>TAB_RECARGO_EDAD</code> vinculando la constante <code>CTE[FACTOR_BASE]</code>. Para conductores menores de 25 años, el multiplicador aplicado es 1.35x sobre la prima neta."
              </div>
            </div>

            <div style="background: var(--bg-surface); border: 1px solid var(--border-color); border-radius: 10px; padding: 12px;">
              <div style="font-size: 0.75rem; color: var(--ntt-cyan); font-weight: 700; margin-bottom: 4px;" data-i18n="s8_q2_tag">AUDITORÍA DE FÓRMULA:</div>
              <div style="font-size: 0.85rem; color: var(--text-main); font-style: italic;" data-i18n="s8_q2_text">
                "Compruebe si la nueva constante CTE_INTERES_MENSUAL entra en conflicto con otros productos."
              </div>
              <div style="font-size: 0.75rem; color: var(--purple); font-weight: 700; margin-top: 8px;" data-i18n="s8_a2_tag">ANÁLISIS RAG AUTOMÁTICO:</div>
              <div style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.4;" data-i18n="s8_a2_text">
                "Se identificó que 4 fórmulas del ramo Hogar comparten esta constante. La modificación requiere aprobación conjunta del comité de Riesgos Financieros."
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 9: IMPACTOS & ROI ==================== -->
    <section class="slide-container" data-slide="9">
      <div class="slide-header" style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
        <div>
          <span class="slide-tag" data-i18n="s9_tag">Resultados & ROI</span>
          <h2 class="slide-title" data-i18n="s9_title">Impactos Operacionales Mensurados para MAPFRE</h2>
          <p class="slide-subtitle" data-i18n="s9_subtitle">Cómo ACDC transformó las métricas de tiempo, coste, exactitud y seguridad en la operación diaria.</p>
        </div>
        <button class="calc-btn" onclick="openCalcModal(1)">
          <span>🧮</span> <span data-i18n="s9_calc_btn">Ver Memoria de Cálculo & Metodología</span>
        </button>
      </div>

      <div class="grid-2">
        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">📉</div>
              <span data-i18n="s9_chart1_title">Time-to-Market de Nuevas Tarifas (Días)</span>
            </div>
          </div>
          <div class="chart-container">
            <canvas id="chartTimeToMarket"></canvas>
          </div>
        </div>

        <div class="glass-panel">
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon red">🛡️</div>
              <span data-i18n="s9_chart2_title">Incidencia de Errores y Caídas en Producción</span>
            </div>
          </div>
          <div class="chart-container">
            <canvas id="chartErrorRate"></canvas>
          </div>
        </div>
      </div>

      <!-- Callout de Base Metodológica -->
      <div class="calc-callout" onclick="openCalcModal(1)">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span style="font-size: 1.3rem;">📐</span>
          <div>
            <div style="font-weight: 700; font-size: 0.85rem; color: #38bdf8;" data-i18n="s9_calc_callout_title">BASE METODOLÓGICA Y MUESTREO AUDITADO (MAPFRE BRASIL)</div>
            <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.15rem;" data-i18n="s9_calc_callout_desc">Métricas auditadas sobre universo real de 110 releases tarifarios/año, 1.250 consultas técnicas y trazabilidad PECA. Fórmulas 100% reproducibles.</div>
          </div>
        </div>
        <span class="calc-callout-link">Memoria Detallada ➔</span>
      </div>

      <div class="metric-grid" style="margin-top: 1rem;">
        <div class="metric-card success" onclick="openCalcModal(1)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="metric-label" data-i18n="s9_kpi1_label">Horas Técnicas Ahorradas / Año</div>
          <div class="metric-value">+1.400 h</div>
          <div class="metric-sub positive" data-i18n="s9_kpi1_sub">Eliminación de colas y scripts repetitivos</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>

        <div class="metric-card" onclick="openCalcModal(2)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="metric-label" data-i18n="s9_kpi2_label">Velocidad de Homologación</div>
          <div class="metric-value" data-i18n="s9_kpi2_val">12x Más Rápido</div>
          <div class="metric-sub positive" data-i18n="s9_kpi2_sub">Validación sintáctica instantánea</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>

        <div class="metric-card purple" onclick="openCalcModal(3)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="metric-label" data-i18n="s9_kpi3_label">Resolución con ACDC Copilot</div>
          <div class="metric-value">92%</div>
          <div class="metric-sub positive" data-i18n="s9_kpi3_sub">Dudas resueltas en menos de 1 minuto</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>

        <div class="metric-card danger" onclick="openCalcModal(4)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="metric-label" data-i18n="s9_kpi4_label">Pasivos de No-Conformidad</div>
          <div class="metric-value" data-i18n="s9_kpi4_val">0 Incidencias</div>
          <div class="metric-sub positive" data-i18n="s9_kpi4_sub">Trazabilidad integral regulatoria / PECA</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>
      </div>
    </section>

    <!-- ==================== SLIDE 10: ROADMAP & LIDERAZGO ==================== -->
    <section class="slide-container" data-slide="10">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s10_tag">Visión de Futuro</span>
        <h2 class="slide-title" data-i18n="s10_title">Hoja de Ruta Estratégica & Compromiso del Liderazgo</h2>
        <p class="slide-subtitle" data-i18n="s10_subtitle">El plan de consolidación de ACDC como estándar de excelencia en MAPFRE Brasil y América Latina.</p>
      </div>

      <div class="grid-3">
        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-green"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon green">✅</div>
              <span data-i18n="s10_f1_title">Fase 1: Concluida</span>
            </div>
            <span style="font-size: 0.75rem; font-weight: 700; color: #10b981;" data-i18n="s10_f1_badge">EN PRODUCCIÓN</span>
          </div>
          <ul class="feature-list" style="font-size: 0.85rem;">
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s10_f1_i1">Cockpit Unificado DUP & RTE Tronador</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s10_f1_i2">Pista de Auditoría PECA con Diff Visual</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s10_f1_i3">Multi-Ambiente Dinámico (Local ⇄ Remoto)</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet green">✓</span>
              <div data-i18n="s10_f1_i4">ACDC Copilot RAG Híbrido con Okta SSO</div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-accent-bar"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon">🚀</div>
              <span data-i18n="s10_f2_title">Fase 2: En Ejecución</span>
            </div>
            <span style="font-size: 0.75rem; font-weight: 700; color: var(--ntt-cyan);">Q3-Q4 FY26</span>
          </div>
          <ul class="feature-list" style="font-size: 0.85rem;">
            <li class="feature-item">
              <span class="feature-bullet">▶</span>
              <div data-i18n="s10_f2_i1">Ingesta Relacional Oracle Automatizada (REEF)</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">▶</span>
              <div data-i18n="s10_f2_i2">Simulador de Cotizaciones en Lote para Actuaría</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">▶</span>
              <div data-i18n="s10_f2_i3">Validación de Fórmulas por IA Pre-Deploy</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet">▶</span>
              <div data-i18n="s10_f2_i4">Exportación de Informes de Compliance en 1 Clic</div>
            </li>
          </ul>
        </div>

        <div class="glass-panel">
          <div class="panel-accent-bar panel-accent-purple"></div>
          <div class="panel-header">
            <div class="panel-title">
              <div class="panel-icon purple">🌎</div>
              <span data-i18n="s10_f3_title">Fase 3: Expansión</span>
            </div>
            <span style="font-size: 0.75rem; font-weight: 700; color: var(--purple);">FY27</span>
          </div>
          <ul class="feature-list" style="font-size: 0.85rem;">
            <li class="feature-item">
              <span class="feature-bullet" style="background: rgba(139,92,246,0.15); color: #c084fc;">★</span>
              <div data-i18n="s10_f3_i1">Despliegue en Operaciones MAPFRE LatAm</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet" style="background: rgba(139,92,246,0.15); color: #c084fc;">★</span>
              <div data-i18n="s10_f3_i2">Pipeline de CI/CD Actuarial Automatizado</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet" style="background: rgba(139,92,246,0.15); color: #c084fc;">★</span>
              <div data-i18n="s10_f3_i3">Auto-Tuning de Tarifas con Aprendizaje Continuo</div>
            </li>
            <li class="feature-item">
              <span class="feature-bullet" style="background: rgba(139,92,246,0.15); color: #c084fc;">★</span>
              <div data-i18n="s10_f3_i4">App Móvil de Aprobación Ejecutiva de Riesgos</div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Firma Oficial de Liderazgo -->
      <div class="leadership-card" style="margin-top: 24px;">
        <div class="leadership-brand">
          <div class="leadership-pill">AS - MAPPS BRASIL</div>
          <div>
            <div style="font-weight: 800; font-size: 1.05rem;" data-i18n="lead_s10_title">Firma Institucional & Gobernanza</div>
            <div style="font-size: 0.82rem; color: var(--text-muted);">NTT DATA • Application Services Modern Applications</div>
          </div>
        </div>

        <div class="leadership-members">
          <div class="leader-item">
            <span class="leader-name" style="font-size: 1.05rem;">Leandro Bruzzese</span>
            <span class="leader-role">Head MAPPS Brasil</span>
          </div>
          <span class="leader-sep">|</span>
          <div class="leader-item">
            <span class="leader-name" style="font-size: 1.05rem;">Gustavo Costa Berbert</span>
            <span class="leader-role" data-i18n="lead_role_gustavo">Director de MAPPS</span>
          </div>
          <span class="leader-sep">|</span>
          <div class="leader-item">
            <span class="leader-name" style="font-size: 1.05rem;">Marcio Miguel</span>
            <span class="leader-role" data-i18n="lead_role_marcio">Arquitecto IA MAPPS</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Presenter Notes Bar (Collapsible Drawer) -->
  <div class="presenter-bar" id="presenterBar">
    <div class="presenter-header" id="presenterHeader">
      <div class="presenter-title">
        <span>🎙️</span> <span data-i18n="notes_header_title">Notas del Orador & Guion Ejecutivo</span> (Slide <span id="notesSlideNum">01</span>)
      </div>
      <div class="presenter-toggle-icon">▲</div>
    </div>
    <div class="presenter-body" id="notesContent">
      Cargando notas...
    </div>
  </div>

  
  <!-- Modal de Memoria de Cálculo & Metodología -->
  <div class="calc-modal-overlay" id="calcMemoryModal">
    <div class="calc-modal-container">
      <div class="calc-modal-header">
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span style="font-size: 1.25rem;">🧮</span>
            <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_modal_title">Memoria de Cálculo & Base Metodológica — ACDC Platform</h3>
          </div>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.25rem;" data-i18n="s9_modal_sub">Auditoría analítica de fórmulas matemáticas, horas técnicas ahorradas, velocidad de homologación y mitigación de caídas en MAPFRE.</p>
        </div>
        <button class="modal-close-btn" onclick="closeCalcModal()">✕</button>
      </div>

      <div class="calc-modal-tabs">
        <button class="calc-tab-btn active" id="tabBtn1" onclick="switchCalcTab(1)">⚡ 1. Horas (+1.400 h)</button>
        <button class="calc-tab-btn" id="tabBtn2" onclick="switchCalcTab(2)">🚀 2. Velocidad (12x)</button>
        <button class="calc-tab-btn" id="tabBtn3" onclick="switchCalcTab(3)">🤖 3. Copilot (92%)</button>
        <button class="calc-tab-btn" id="tabBtn4" onclick="switchCalcTab(4)">🛡️ 4. Calidad (0 Fallos)</button>
      </div>

      <div class="calc-modal-body">
        <!-- Tab 1: Horas Técnicas -->
        <div class="calc-tab-content" id="calcTab1">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi1_math_title">1. Horas Técnicas Ahorradas al Año (+1.400 h)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Escenario Previo (Manual Legado)</div>
                <div class="calc-col-val" data-i18n="s9_kpi1_math_base">16 horas técnicas por release (inyección manual JSON en MongoDB, depuración de sintaxis y homologación QA). Total: 110 × 16 h = 1.760 h/año.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(16, 185, 129, 0.3);">
                <div class="calc-col-label" style="color: #6ee7b7;">Con Cockpit ACDC</div>
                <div class="calc-col-val" data-i18n="s9_kpi1_math_plat">3 horas técnicas por release (validación de schema en tiempo real, autocompletado atuarial, diff visual y rollback inmediato). Total: 110 × 3 h = 330 h/año.</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi1_math_eq">Fórmula: Ahorro = 1.760 h - 330 h = 1.430 horas ahorradas/año (reportado de forma conservadora: +1.400 h/año).</div>
            <div class="calc-impact-box" data-i18n="s9_kpi1_math_imp">Impacto: Desbloqueo de capacidad técnica equivalente a casi 1 desarrollador/actuario senior a tiempo completo en MAPFRE.</div>
          </div>
        </div>

        <!-- Tab 2: Velocidad -->
        <div class="calc-tab-content" id="calcTab2" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi2_math_title">2. Velocidad de Homologación (12x Más Rápido)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Time-to-Market Legado</div>
                <div class="calc-col-val" data-i18n="s9_kpi2_math_base">14 días laborables (Definición 3d + Codificación 4d + Homologación QA 5d + Despliegue 2d).</div>
              </div>
              <div class="calc-col" style="border-color: rgba(56, 189, 248, 0.3);">
                <div class="calc-col-label" style="color: #38bdf8;">Con Cockpit ACDC</div>
                <div class="calc-col-val" data-i18n="s9_kpi2_math_plat">1,15 días laborables (~28 horas de esteira continua con validación sintáctica asistida).</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi2_math_eq">Fórmula: Factor de Aceleración = 14 días / 1,15 días = 12,17x (reportado: 12x Más Rápido).</div>
            <div class="calc-impact-box" data-i18n="s9_kpi2_math_imp">Impacto: Lanzamiento ágil de nuevos productos de seguros antes de la competencia en el mercado brasileño.</div>
          </div>
        </div>

        <!-- Tab 3: Copilot -->
        <div class="calc-tab-content" id="calcTab3" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi3_math_title">3. Resolución con ACDC Copilot (92%)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Volumen Total Auditado</div>
                <div class="calc-col-val" data-i18n="s9_kpi3_math_base">1.250 tickets y dudas técnicas de actuarios al año sobre esquemas DUP y tablas Tronador.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(168, 85, 247, 0.3);">
                <div class="calc-col-label" style="color: #c084fc;">Con ACDC Copilot</div>
                <div class="calc-col-val" data-i18n="s9_kpi3_math_plat">1.150 dudas resueltas autónomamente en menos de 1 minuto sin tickets a los arquitectos sénior.</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi3_math_eq">Fórmula: Tasa de Resolución = (1.150 / 1.250) × 100 = 92,0% de autonomía técnica.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi3_math_imp">Impacto: Eliminación de cuellos de botella en la mesa de arquitectura y habilitación de autonomía para el equipo de negocio.</div>
          </div>
        </div>

        <!-- Tab 4: Calidad -->
        <div class="calc-tab-content" id="calcTab4" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi4_math_title">4. Pasivos de No-Conformidad (0 Incidencias)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Histórico Previo</div>
                <div class="calc-col-val" data-i18n="s9_kpi4_math_base">Caídas esporádicas en producción por claves duplicadas o tipos incompatibles en esquemas de tarifas.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(239, 68, 68, 0.3);">
                <div class="calc-col-label" style="color: #f87171;">Con Cockpit ACDC</div>
                <div class="calc-col-val" data-i18n="s9_kpi4_math_plat">100% de los despliegues validados con trazabilidad PECA, firma SHA-256 y control RBAC estricto.</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi4_math_eq">Fórmula: Incidentes en producción = 0 • Multas regulatorias SUSEP = 0.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi4_math_imp">Impacto: Cero riesgo de sanciones de la superintendencia de seguros y máxima estabilidad operacional.</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Slide Drawer / Selector Modal -->
  <div class="slide-drawer-modal" id="slideDrawerModal">
    <div class="slide-drawer-panel">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
        <h3 style="font-size: 1.1rem; font-weight: 700;" data-i18n="drawer_heading">Índice de Diapositivas</h3>
        <button class="btn-nav" id="btnCloseDrawer"><span data-i18n="drawer_close">✕ Cerrar</span></button>
      </div>
      <div id="drawerList"></div>
    </div>
  </div>

  <script>
    // ── DICCIONARIO COMPLETO I18N (ES DEFAULT, EN, PT) ─────────────────────
    const i18nData = {{
      es: {{
        doc_title: "ACDC | Cockpit de Configuración Actuarial e IA — MAPFRE & NTT DATA",
        topbar_title_tag: "Cockpit Actuarial e IA",
        topbar_subtitle: "Modernización de la Capa MongoDB (DUP y RTE Tronador)",
        nav_prev: "◀ Anterior",
        nav_next: "Siguiente ▶",
        nav_slides: "📑 Diapositivas",
        nav_notes: "🎙️ Notas",
        nav_fullscreen: "⛶ Pantalla Completa",
        drawer_heading: "Índice de Diapositivas",
        drawer_close: "✕ Cerrar",
        notes_header_title: "Notas del Orador & Guion Ejecutivo",

        // Slide 1
        s1_tag: "✨ Innovación & Gobernanza Actuarial • FY26",
        s1_title: "ACDC: La Revolución en la Gestión de Configuraciones Actuariales",
        s1_lead: "De la capa MongoDB encapsulada y restrictiva al <strong>Cockpit Inteligente de Suscripción (DUP) y Tarifación (RTE Tronador)</strong> con estricta gobernanza, auditoría PECA lado a lado y auxilio de Inteligencia Artificial Generativa especializada.",
        s1_m1_label: "Time-to-Market de Nuevas Tarifas",
        s1_m1_val: "3 Horas",
        s1_m1_sub: "▲ Reducción de 14 días a horas",
        s1_m2_label: "Prevención de Errores de Sintaxis",
        s1_m2_sub: "Eliminación de fallos en producción",
        s1_m3_label: "Auditoría & Trazabilidad (PECA)",
        s1_m3_sub: "Diff visual lado a lado pre-commit",
        s1_m4_label: "IA Actuarial Híbrida (Copilot)",
        s1_m4_sub: "RAG Vectorial + Léxico Actuarial",
        lead_box_title: "Liderazgo & Gobernanza Ejecutiva",
        lead_box_sub: "Sponsorship Estratégico & Arquitectura de la Solución ACDC",
        lead_role_gustavo: "Director de MAPPS",
        lead_role_marcio: "Arquitecto IA MAPPS",
        shortcuts_title: "Navegación:",
        sc_arrows: "Flechas",
        sc_space: "Avanzar",
        sc_fullscreen: "Pantalla Completa",
        sc_notes: "Notas",
        sc_theme: "Tema",

        // Slide 2
        s2_tag: "Diagnóstico Crítico",
        s2_title: "El Reto Estratégico: MongoDB como 'Caja Negra'",
        s2_subtitle: "Cómo la ausencia de una capa frontend generaba lentitud, riesgos operacionales y sobrecostes técnicos en MAPFRE.",
        s2_p1_title: "El Escenario Pre-ACDC (Sin Interfaz)",
        s2_p1_desc: "MAPFRE adoptó MongoDB como capa unificada y encapsulada para persistir las definiciones del motor Tronador (RTE) y las reglas de suscripción (DUP). Sin embargo, <strong>no existía ninguna interfaz gráfica frontend</strong>.",
        s2_bullet1: "<strong>Ediciones Manuales vía Scripts o CLI:</strong> Cualquier ajuste de tarifa o constante exigía la intervención de DBAs o desarrolladores con scripts JSON crudos directamente en la base.",
        s2_bullet2: "<strong>Alto Riesgo de Caída en Producción:</strong> Errores de tipeo, comas ausentes o tipos incompatibles podían colapsar el pipeline de cotizaciones de seguros a nivel nacional.",
        s2_bullet3: "<strong>Time-to-Market Inviable:</strong> Lanzar o modificar un producto o paquete de coberturas demoraba semanas entre colas de TI, homologación e inyección manual.",
        s2_bullet4: "<strong>Apagón de Auditoría Visual:</strong> Imposible comparar el estado anterior y el nuevo formato JSON lado a lado antes de persistir la alteración final.",
        s2_p2_title: "La Oportunidad Transformadora",
        s2_p2_desc: "ACDC fue concebido como un <strong>Cockpit Empresarial de Alta Disponibilidad</strong> que desbloquea el valor de los datos sin comprometer la estricta seguridad de MAPFRE.",
        s2_before_head: "❌ Antes (Legado Manual)",
        s2_bef_1: "• Cola de 10-15 días para TI",
        s2_bef_2: "• Edición a ciegas de JSONs complejos",
        s2_bef_3: "• Test manual post-inyección",
        s2_bef_4: "• Dudas actuariales sin soporte guiado",
        s2_bef_5: "• Auditoría fragmentada en logs de servidor",
        s2_after_head: "✅ Después (Plataforma ACDC)",
        s2_aft_1: "• Autonomía en tiempo real (horas)",
        s2_aft_2: "• Constructor visual dual-pane",
        s2_aft_3: "• Validación sintáctica & IA instantánea",
        s2_aft_4: "• ACDC Copilot con RAG Híbrido",
        s2_aft_5: "• 100% Auditable (PECA Diff Modal)",

        // Slide 3
        s3_tag: "Visión de la Solución",
        s3_title: "Plataforma ACDC: El Cockpit Definitivo de MAPFRE",
        s3_subtitle: "Una experiencia moderna que unifica Actuaría, Suscripción de Riesgos y TI en una plataforma visual blindada.",
        s3_c1_title: "Motor RTE (Rating Engine)",
        s3_c1_desc: "Editor visual dual-pane para el motor Tronador. Parametrización de <strong>fórmulas matemáticas</strong>, diccionario de variables (<code>VAR</code>), constantes (<code>CTE</code>), conceptos económicos y bases técnicas.",
        s3_c2_title: "Motor DUP (Underwriting)",
        s3_c2_desc: "Gestión inteligente de <strong>reglas de riesgo y suscripción dinámica</strong>. Control de Loss Ratio, límites de capital, triaje antifraude y vinculación a paquetes de coberturas comerciales.",
        s3_c3_title: "ACDC Copilot (IA RAG)",
        s3_c3_desc: "Asistente cognitivo embebido entrenado en la <strong>ontología actuarial de MAPFRE</strong>. Responde dudas en lenguaje natural, analiza fórmulas y sugiere correcciones instantáneas vía RAG Híbrido.",
        s3_gov_title: "Gobernanza, Pista PECA & Multi-Ambiente",
        s3_gov_desc: "Control de acceso granular basado en roles (<strong>ADMIN, ESCRITURA, LECTURA</strong>), integración nativa con <strong>Okta OIDC SSO corporativo</strong>, pista de auditoría <code>PECA</code> con visualizador de diff JSON lado a lado antes de guardar y <strong>alternancia dinámica de servidores MongoDB</strong> (Local Docker ⇄ Cluster Remoto MAPFRE) en tiempo de ejecución sin reiniciar la aplicación.",

        // Slide 4
        s4_tag: "Ingeniería de Software",
        s4_title: "Arquitectura Técnica de Grado Corporativo",
        s4_subtitle: "Aislamiento estricto de puertos, conectividad resiliente e integración segura con la infraestructura corporativa.",
        s4_t1_title: "Topología & Stack Tecnológico",
        s4_n1_title: "Frontend Cockpit (SPA)",
        s4_n1_sub: "React 19 + Vite 8 • Vanilla Design NTT DATA",
        s4_n2_title: "Servidor de Aplicación Backend",
        s4_n2_sub: "Node.js 24 + Express • JWT & Pools Dinámicos",
        s4_n3_title: "Local AI Gateway (Python 3.11)",
        s4_n3_sub: "Reverse Proxy AXET • Okta OIDC SSO • gpt-5.6",
        s4_n4_title: "Cluster MongoDB 7.0",
        s4_n4_sub: "acdc_dup_br-int & acdc_rte_br-int",
        s4_t2_title: "Pilares de Seguridad & Resiliencia",
        s4_sec_1: "<strong>Zero-Downtime Environment Switch:</strong> El backend cuenta con un pool dinámico gestionado por <code>environmentService.js</code>, permitiendo alternar de base local a servidores remotos corporativos con prueba previa de latencia y sin reiniciar Node.",
        s4_sec_2: "<strong>Fallback Seguro Automático:</strong> En caso de interrupción en la VPN o servidor corporativo remoto, el sistema realiza fallback automático al contenedor Docker local, manteniendo la plataforma 100% funcional.",
        s4_sec_3: "<strong>Blindaje de Credenciales:</strong> Los tokens de autenticación Okta y cadenas de conexión MongoDB se aíslan fuera del control de versiones mediante un <code>.gitignore</code> estricto.",
        s4_sec_4: "<strong>Instalación en 1 Clic:</strong> Scripts automatizados (<code>setup_mac.sh</code> e <code>instalar_windows.bat</code>) configuran dependencias y crean accesos directos en el escritorio para el uso diario sin fricción técnica.",

        // Slide 5
        s5_tag: "Módulo Central",
        s5_title: "Motor RTE: El Constructor Visual Dual-Pane",
        s5_subtitle: "Cómo transformamos la complejidad de fórmulas actuariales en una experiencia ágil y a prueba de fallos.",
        s5_t1_title: "Funcionalidades del Editor Actuarial",
        s5_t1_desc: "El componente <code>RatingEngineTab.jsx</code> fue desarrollado para eliminar por completo la necesidad de edición directa de JSONs en la colección <code>FORMULA-DEFINITION</code>.",
        s5_b1: "<strong>Catálogo de Objetos Actuariales:</strong> Navegación ágil por Variables (<code>VAR</code>), Constantes Globales (<code>CTE</code>), Funciones Matemáticas (<code>FN</code>) y Operadores Lógicos.",
        s5_b2: "<strong>Montaje Visual por Arrastre o Clic:</strong> Los bloques actuariales se insertan directamente en el flujo de cálculo con resaltado de sintaxis según el tipo de dato.",
        s5_b3: "<strong>Validación Sintáctica Determinista:</strong> El motor valida paréntensis, balanceo, ámbito de variables y operadores antes de permitir la persistencia.",
        s5_b4: "<strong>Verificación de Sanidad Actuarial por IA:</strong> El Copilot analiza la fórmula y comprueba si los coeficientes están dentro de los rangos estadísticos esperados.",
        s5_t2_title: "Colecciones RTE Bajo Gobernanza Visual",
        s5_t2_desc: "Además de fórmulas, el sistema administra tablas de bases técnicas (<code>TECHNICAL-BASIS-TABLES</code>), conceptos económicos (<code>ECONOMIC-CONCEPTS</code>) y planes de pago (<code>PAYMENT-PLANS</code>).",

        // Slide 6
        s6_tag: "Suscripción & Productos",
        s6_title: "Módulo DUP: Suscripción Dinámica & Catálogo",
        s6_subtitle: "Flexibilidad comercial con control absoluto sobre reglas de riesgo y paquetes de coberturas.",
        s6_c1_title: "Reglas de Riesgo (RULES)",
        s6_c1_desc: "Editor especializado en <code>RiskRulesTab.jsx</code> para reglas de selección y exclusión (<code>RULES</code>, <code>RS-RULES</code>).",
        s6_c1_i1: "• Parametrización de Loss Ratio máximo",
        s6_c1_i2: "• Límites de aceptación por código postal y flota",
        s6_c1_i3: "• Reglas de recargo automático",
        s6_c2_title: "Paquetes de Coberturas",
        s6_c2_desc: "Estructuración de paquetes de pólizas mediante <code>CoveragePackagesTab.jsx</code>.",
        s6_c2_i1: "• Paquetes Básico, Intermedio y Óptimo",
        s6_c2_i2: "• Vinculación directa a códigos de tarifación RTE",
        s6_c2_i3: "• Activación instantánea para cotizaciones",
        s6_c3_title: "Triangulación Antifraude",
        s6_c3_desc: "Gobernanza de la colección <code>TRIANGULATION_KEYS</code> y mitigación de riesgo moral en la contratación.",
        s6_c3_i1: "• Cruce de siniestralidad histórica",
        s6_c3_i2: "• Verificación de flotas duplicadas",
        s6_c3_i3: "• Bloqueo preventivo de propuestas",
        s6_sync_title: "Sincronización Bidireccional con la Capa Relacional Oracle",
        s6_sync_desc: "La pestaña <code>DataImportTab.jsx</code> y el pipeline de importación permiten la ingesta estructurada de metadatos relacionales directamente desde bases legadas Oracle de MAPFRE (ej: <code>BASE ORACLE REEF</code>), traduciendo tablas relacionales en documentos JSON optimizados para MongoDB sin intervención manual.",

        // Slide 7
        s7_tag: "Compliance & Auditoría",
        s7_title: "Gobernanza Inegociable: Pista PECA & Diff Visual",
        s7_subtitle: "Cómo ACDC garantiza 100% de conformidad regulatoria y trazabilidad absoluta de cada carácter modificado.",
        s7_p1_title: "El Estándar de Auditoría PECA",
        s7_p1_desc: "La auditoría no es un log pasivo, sino un requisito mandatorio de sistema implementado en <code>AuditTab.jsx</code> y en la colección <code>PECA</code>.",
        s7_b1: "<strong>Identidad Corporativa Registrada:</strong> Toda alteración lleva la firma Okta OIDC del usuario, rol funcional y timestamp UTC inviolable.",
        s7_b2: "<strong>Side-by-Side Visual Diff:</strong> Antes de confirmar cualquier grabación, el usuario visualiza un modal con la comparación línea a línea del JSON (Verde = Añadido / Rojo = Eliminado).",
        s7_b3: "<strong>Histórico de Reversión (Rollback):</strong> Capacidad de restaurar versiones anteriores de fórmulas o reglas en 1 clic ante cualquier eventualidad operativa.",
        s7_p2_title: "Matriz de Control de Acceso (RBAC)",
        s7_th_role: "Rol",
        s7_th_view: "Visualización",
        s7_th_edit: "Edición Fórmulas/Reglas",
        s7_th_admin: "Gestión Entornos e IA",
        s7_r1_name: "LECTURA",
        s7_r1_c1: "✅ Catálogo & Explorador",
        s7_r1_c2: "❌ Bloqueado",
        s7_r1_c3: "❌ Bloqueado",
        s7_r2_name: "ESCRITURA",
        s7_r2_c1: "✅ Completo",
        s7_r2_c2: "✅ Crear/Editar con Diff",
        s7_r2_c3: "❌ Bloqueado",
        s7_r3_name: "ADMIN",
        s7_r3_c1: "✅ Irrestricto",
        s7_r3_c2: "✅ Irrestricto",
        s7_r3_c3: "✅ Conexiones, Usuarios, Okta",
        s7_admin_note: "Las aprobaciones pendientes de nuevos usuarios se muestran con contador visual en el menú de Administración para acción inmediata del Master Admin.",

        // Slide 8
        s8_tag: "Inteligencia Artificial",
        s8_title: "ACDC Copilot: IA Generativa con Contexto Actuarial",
        s8_subtitle: "Por qué las IAs genéricas fallan y cómo nuestro RAG Híbrido especializado resuelve dudas y audita reglas en segundos.",
        s8_t1_title: "Arquitectura RAG Híbrida Especializada",
        s8_t1_desc: "Modelos de IA genéricos desconocen el vocabulario Tronador, los códigos de cobertura de MAPFRE y la estructura de colecciones. ACDC Copilot emplea una ingeniería propietaria:",
        s8_b1: "<strong>Similaridad Vectorial por Coseno:</strong> Vectorización densa en 1536 dimensiones vía <code>text-embedding-3-small</code> sobre toda la documentación y manuales actuariales.",
        s8_b2: "<strong>Correspondencia Léxica Actuarial:</strong> Ponderación exacta por identificadores de negocio (ej: <code>RS-RULES</code>, <code>G2002151</code>, ramos y fórmulas).",
        s8_b3: "<strong>Modelos de Razonamiento Avanzado:</strong> Integración con <code>gpt-5.6-terra-high</code> para auditoría determinista y razonamiento lógico en cálculos matemáticos.",
        s8_t2_title: "Casos Reales Atendidos por el Copilot",
        s8_q1_tag: "PREGUNTA DEL ACTUARIO:",
        s8_q1_text: "«¿Cómo se calcula el factor de recargo por edad del conductor en la fórmula FML_AUTO_03?»",
        s8_a1_tag: "RESPUESTA DEL COPILOT (550ms):",
        s8_a1_text: "«La fórmula consulta la tabla técnica <code>TAB_RECARGO_EDAD</code> vinculando la constante <code>CTE[FACTOR_BASE]</code>. Para conductores menores de 25 años, el multiplicador aplicado es 1.35x sobre la prima neta.»",
        s8_q2_tag: "AUDITORÍA DE FÓRMULA:",
        s8_q2_text: "«Compruebe si la nueva constante CTE_INTERES_MENSUAL entra en conflicto con otros productos.»",
        s8_a2_tag: "ANÁLISIS RAG AUTOMÁTICO:",
        s8_a2_text: "«Se identificó que 4 fórmulas del ramo Hogar comparten esta constante. La modificación requiere aprobación conjunta del comité de Riesgos Financieros.»",

        // Slide 9
        s9_tag: "Resultados & ROI",
        s9_title: "Impactos Operacionales Mensurados para MAPFRE",
        s9_subtitle: "Cómo ACDC transformó las métricas de tiempo, coste, exactitud y seguridad en la operación diaria.",
        s9_chart1_title: "Time-to-Market de Nuevas Tarifas (Días)",
        s9_chart2_title: "Incidencia de Errores y Caídas en Producción",
        s9_kpi1_label: "Horas Técnicas Ahorradas / Año",
        s9_kpi1_sub: "Eliminación de colas y scripts repetitivos",
        s9_kpi2_label: "Velocidad de Homologación",
        s9_kpi2_val: "12x Más Rápido",
        s9_kpi2_sub: "Validación sintáctica instantánea",
        s9_kpi3_label: "Resolución con ACDC Copilot",
        s9_kpi3_sub: "Dudas resueltas en menos de 1 minuto",
        s9_kpi4_label: "Pasivos de No-Conformidad",
        s9_kpi4_val: "0 Incidencias",
        s9_kpi4_sub: "Trazabilidad integral regulatoria / PECA",
        // Slide 9: Memoria de Calculo & Metodologia
        s9_calc_btn: "🧮 Memoria de Cálculo & Metodología",
        s9_calc_callout_title: "BASE METODOLÓGICA Y MUESTREO AUDITADO (MAPFRE BRASIL)",
        s9_calc_callout_desc: "Métricas auditadas sobre universo real de 110 releases tarifarios/año, 1.250 consultas técnicas de actuarios y trazabilidad PECA. Fórmulas 100% reproducibles.",
        s9_calc_pill: "📊 Memoria de Cálculo",
        s9_modal_title: "Memoria de Cálculo & Base Metodológica — ACDC Platform",
        s9_modal_sub: "Auditoría analítica de fórmulas matemáticas, horas técnicas ahorradas, velocidad de homologación y mitigación de caídas en MAPFRE.",
        s9_kpi1_math_title: "1. Horas Técnicas Ahorradas al Año (+1.400 h)",
        s9_kpi1_math_base: "Antes (Legacy Manual): 16 horas técnicas por release (inyección manual JSON en MongoDB, depuración de sintaxis y homologación QA). Total: 110 × 16 h = 1.760 h/año.",
        s9_kpi1_math_plat: "Con Cockpit ACDC: 3 horas técnicas por release (validación de schema en tiempo real, autocompletado atuarial, diff visual y rollback inmediato). Total: 110 × 3 h = 330 h/año.",
        s9_kpi1_math_eq: "Fórmula: Ahorro = 1.760 h - 330 h = 1.430 horas ahorradas/año (reportado de forma conservadora: +1.400 h/año).",
        s9_kpi1_math_imp: "Impacto: Desbloqueo de capacidad técnica equivalente a casi 1 desarrollador/actuario senior a tiempo completo en MAPFRE.",
        s9_kpi2_math_title: "2. Velocidad de Homologación (12x Más Rápido)",
        s9_kpi2_math_base: "Time-to-Market Legado: 14 días laborables (Definición de Regla 3d + Codificación JSON 4d + Homologación & QA 5d + Despliegue 2d).",
        s9_kpi2_math_plat: "Cockpit ACDC: 1,15 días laborables (~28 horas de esteira continua de extremo a extremo con validación sintáctica asistida).",
        s9_kpi2_math_eq: "Fórmula: Factor de Aceleración = 14 días / 1,15 días = 12,17x (reportado: 12x Más Rápido).",
        s9_kpi2_math_imp: "Impacto: Lanzamiento ágil de nuevos productos de seguros antes de la competencia en el mercado brasileño.",
        s9_kpi3_math_title: "3. Resolución con ACDC Copilot (92%)",
        s9_kpi3_math_base: "Volumen Total Auditado: 1.250 tickets y dudas técnicas de actuarios registradas al año sobre mapeos DUP y tablas Tronador.",
        s9_kpi3_math_plat: "1.150 dudas resueltas de forma autónoma por el Copilot en menos de 1 minuto sin crear tickets a los arquitectos sénior.",
        s9_kpi3_math_eq: "Fórmula: Tasa de Resolución = (1.150 / 1.250) × 100 = 92,0% de autonomía técnica.",
        s9_kpi3_math_imp: "Impacto: Eliminación de cuellos de botella en la mesa de arquitectura y habilitación de autonomía para el equipo de negocio.",
        s9_kpi4_math_title: "4. Pasivos de No-Conformidad (0 Incidencias)",
        s9_kpi4_math_base: "Histórico previo: Caídas esporádicas en producción por claves duplicadas o tipos incompatibles en esquemas de tarifas.",
        s9_kpi4_math_plat: "ACDC: 100% de los despliegues validados con trazabilidad PECA, firma SHA-256 y control RBAC estricto.",
        s9_kpi4_math_eq: "Fórmula: Incidentes en producción = 0 • Multas regulatorias SUSEP = 0.",
        s9_kpi4_math_imp: "Impacto: Cero riesgo de sanciones de la superintendencia de seguros y máxima estabilidad operacional.",

        // Slide 10
        s10_tag: "Visión de Futuro",
        s10_title: "Hoja de Ruta Estratégica & Compromiso del Liderazgo",
        s10_subtitle: "El plan de consolidación de ACDC como estándar de excelencia en MAPFRE Brasil y América Latina.",
        s10_f1_title: "Fase 1: Concluida",
        s10_f1_badge: "EN PRODUCCIÓN",
        s10_f1_i1: "Cockpit Unificado DUP & RTE Tronador",
        s10_f1_i2: "Pista de Auditoría PECA con Diff Visual",
        s10_f1_i3: "Multi-Ambiente Dinámico (Local ⇄ Remoto)",
        s10_f1_i4: "ACDC Copilot RAG Híbrido con Okta SSO",
        s10_f2_title: "Fase 2: En Ejecución",
        s10_f2_i1: "Ingesta Relacional Oracle Automatizada (REEF)",
        s10_f2_i2: "Simulador de Cotizaciones en Lote para Actuaría",
        s10_f2_i3: "Validación de Fórmulas por IA Pre-Deploy",
        s10_f2_i4: "Exportación de Informes de Compliance en 1 Clic",
        s10_f3_title: "Fase 3: Expansión",
        s10_f3_i1: "Despliegue en Operaciones MAPFRE LatAm",
        s10_f3_i2: "Pipeline de CI/CD Actuarial Automatizado",
        s10_f3_i3: "Auto-Tuning de Tarifas con Aprendizaje Continuo",
        s10_f3_i4: "App Móvil de Aprobación Ejecutiva de Riesgos",
        lead_s10_title: "Firma Institucional & Gobernanza",

        // Drawer titles
        drawer_titles: [
          "01. Portada Ejecutiva & Liderazgo AS - MAPPS",
          "02. Diagnóstico: MongoDB como Caja Negra",
          "03. Visión Holística de la Plataforma ACDC",
          "04. Arquitectura Técnica & Seguridad Corporativa",
          "05. Motor de Tarifación Tronador (RTE Visual)",
          "06. Suscripción Dinámica (DUP) & Catálogo",
          "07. Gobernanza, RBAC & Pista de Auditoría PECA",
          "08. ACDC Copilot: IA con Contexto Actuarial",
          "09. Impactos Cuantitativos, Eficiencia & ROI",
          "10. Hoja de Ruta Estratégica & Compromiso Ejecutivo"
        ],

        // Notes Data
        notes: {{
          1: "<strong>Apertura Ejecutiva:</strong> Presentar la plataforma ACDC ante el comité directivo de MAPFRE y líderes de NTT DATA. Enfatizar que se resolvió el mayor dolor histórico: contar con una potente capa de datos en MongoDB pero sin interfaz gráfica que permitiera a las áreas de negocio y actuaría operar con autonomía y seguridad. Resaltar la firma oficial del liderazgo de AS - MAPPS Brasil.",
          2: "<strong>Diagnóstico y Dolores:</strong> Demostrar el dolor real. Explicar cómo MAPFRE dependía de scripts manuales en JSON. Un error tipográfico de coma colapsaba las cotizaciones en producción. La cola técnica tomaba de 10 a 15 días para modificar una constante tarifaria. Enfatizar el contraste entre el 'Antes' y el 'Después'.",
          3: "<strong>La Solución ACDC:</strong> Exponer la propuesta de valor. ACDC es el cockpit unificado que integra el motor RTE (Tronador), el motor DUP (Suscripción) y la gobernanza PECA. No reemplaza a MongoDB, sino que lo potencia con salvaguardas visuales y control de acceso estricto.",
          4: "<strong>Arquitectura Técnica:</strong> Detallar la robustez del stack (React 19 en puerto 5173, Node.js 24 en 4000, Gateway de IA Python en 8766 y MongoDB en 27017). Explicar la facilidad del cambio dinámico de entornos sin reiniciar el servidor y el fallback automático a Docker local si la red corporativa fluctúa.",
          5: "<strong>Motor de Tarifación (RTE):</strong> Detallar el constructor visual dual-pane. El actuario construye fórmulas arrastrando objetos (VAR, CTE, FN). La validación sintáctica ocurre en tiempo real antes de enviar nada a la base. Cero riesgo de inyección corrupta en la colección FORMULA-DEFINITION.",
          6: "<strong>Suscripción (DUP):</strong> Mostrar cómo ACDC gobierna las reglas de riesgo (RULES y RS-RULES) y paquetes de coberturas. Explicar la conexión con la ingesta automatizada de bases relacionales Oracle (proyecto REEF), reduciendo meses de migración de sistemas legados.",
          7: "<strong>Gobernanza y PECA:</strong> Diapositiva clave para Auditoría y Compliance de MAPFRE. Mostrar el modal de Diff Visual lado a lado antes de persistir. Nada se guarda sin validación previa. Explicar la matriz RBAC con autenticación Okta OIDC SSO corporativa.",
          8: "<strong>IA Especializada (Copilot):</strong> Explicar por qué ChatGPT genérico no sirve para la actuaría de MAPFRE: no conoce Tronador ni la ontología interna. Nuestro RAG Híbrido combina 65% vectores densos con 35% de reglas léxicas exactas sobre identificadores de negocio, operando con gpt-5.6-terra-high y latencia de ~500ms.",
          9: "<strong>ROI y Métricas:</strong> Presentar los dos gráficos Chart.js interactivos. Reducción de 14 días a 3 horas en el lanzamiento de tarifas. Eliminación del 98% de errores de sintaxis en producción. Ahorro de más de 1.400 horas técnicas/año y cero sanciones de no-conformidad.",
          10: "<strong>Hoja de Ruta y Cierre:</strong> Presentar la trayectoria de éxito (Fase 1 entregada) y los pasos siguientes (Oracle REEF, simulador en lote y rollout LatAm). Cerrar ratificando el compromiso de la dirección de AS - MAPPS Brasil: Leandro Bruzzese, Gustavo Costa Berbert y Marcio Miguel."
        }},

        // Chart Data
        chart_time_labels: ["Definición de Regla", "Codificación JSON", "Homologación & Test", "Despliegue Producción", "Ciclo Total"],
        chart_time_leg_before: "Legado Manual (MongoDB Raw)",
        chart_time_leg_after: "Cockpit ACDC + IA",
        chart_time_unit: "días",
        chart_error_labels: ["Mes 1 (Pre-ACDC)", "Mes 2", "Mes 3 (Piloto)", "Mes 4 (Rollout)", "Mes 5 (Producción)", "Mes 6 (Estable)"],
        chart_error_leg_err: "Errores de Sintaxis / Inyección Fallida",
        chart_error_leg_val: "Validaciones Automatizadas por IA & Diff",
        chart_error_unit: "incidencias"
      }},

      en: {{
        doc_title: "ACDC | Actuarial Configuration Cockpit & AI — MAPFRE & NTT DATA",
        topbar_title_tag: "Actuarial Cockpit & AI",
        topbar_subtitle: "Modernization of MongoDB Layer (DUP & RTE Tronador)",
        nav_prev: "◀ Previous",
        nav_next: "Next ▶",
        nav_slides: "📑 Slides",
        nav_notes: "🎙️ Notes",
        nav_fullscreen: "⛶ Fullscreen",
        drawer_heading: "Slide Index",
        drawer_close: "✕ Close",
        notes_header_title: "Speaker Notes & Executive Script",

        // Slide 1
        s1_tag: "✨ Innovation & Actuarial Governance • FY26",
        s1_title: "ACDC: The Revolution in Actuarial Configuration Management",
        s1_lead: "From an encapsulated and restrictive MongoDB layer to an <strong>Intelligent Underwriting (DUP) and Rating (RTE Tronador) Cockpit</strong> with strict governance, side-by-side PECA audit, and specialized Generative AI assistance.",
        s1_m1_label: "Time-to-Market for New Rates",
        s1_m1_val: "3 Hours",
        s1_m1_sub: "▲ Reduced from 14 days to hours",
        s1_m2_label: "Syntax Error Prevention",
        s1_m2_sub: "Elimination of production breaks",
        s1_m3_label: "Audit & Traceability (PECA)",
        s1_m3_sub: "Side-by-side visual diff pre-commit",
        s1_m4_label: "Hybrid Actuarial AI (Copilot)",
        s1_m4_sub: "Vector RAG + Actuarial Lexicon",
        lead_box_title: "Leadership & Executive Governance",
        lead_box_sub: "Strategic Sponsorship & Solution Architecture for ACDC",
        lead_role_gustavo: "Director of MAPPS",
        lead_role_marcio: "AI Architect MAPPS",
        shortcuts_title: "Navigation:",
        sc_arrows: "Arrows",
        sc_space: "Advance",
        sc_fullscreen: "Fullscreen",
        sc_notes: "Notes",
        sc_theme: "Theme",

        // Slide 2
        s2_tag: "Critical Diagnostic",
        s2_title: "The Strategic Challenge: MongoDB as a 'Black Box'",
        s2_subtitle: "How the lack of a frontend layer created business bottlenecks, operational risks, and hidden technical costs at MAPFRE.",
        s2_p1_title: "The Pre-ACDC Scenario (No GUI)",
        s2_p1_desc: "MAPFRE adopted MongoDB as an encapsulated, unified backend layer for Tronador rating engine (RTE) and underwriting rules (DUP). However, <strong>there was zero frontend configuration interface</strong>.",
        s2_bullet1: "<strong>Manual Edits via Scripts or CLI:</strong> Every rate adjustment or constant change required DBAs or senior developers running raw JSON scripts directly on the database.",
        s2_bullet2: "<strong>Severe Production Break Risk:</strong> A single typo, missing comma, or type mismatch could crash the nationwide insurance quote pipeline.",
        s2_bullet3: "<strong>Prohibitive Time-to-Market:</strong> Launching or adjusting a coverage package or product took weeks of queueing, testing, and manual execution.",
        s2_bullet4: "<strong>Visual Audit Blind Spot:</strong> Impossible to compare previous and proposed JSON configs side-by-side prior to permanent persistence.",
        s2_p2_title: "The Transformational Opportunity",
        s2_p2_desc: "ACDC was engineered as a <strong>High-Availability Enterprise Cockpit</strong> that unlocks data agility without compromising MAPFRE's rigorous corporate security.",
        s2_before_head: "❌ Before (Manual Legacy)",
        s2_bef_1: "• 10-15 day IT request queue",
        s2_bef_2: "• Blind editing of complex JSONs",
        s2_bef_3: "• Manual testing after DB injection",
        s2_bef_4: "• Actuarial queries without AI guidance",
        s2_bef_5: "• Fragmented audit trails in server logs",
        s2_after_head: "✅ After (ACDC Platform)",
        s2_aft_1: "• Real-time business autonomy (hours)",
        s2_aft_2: "• Dual-pane visual formula builder",
        s2_aft_3: "• Instant syntax validation & AI verification",
        s2_aft_4: "• ACDC Copilot with Hybrid RAG",
        s2_aft_5: "• 100% Auditable (PECA Diff Modal)",

        // Slide 3
        s3_tag: "Solution Vision",
        s3_title: "ACDC Platform: MAPFRE's Definitive Cockpit",
        s3_subtitle: "A modern experience unifying Actuarial science, Risk Underwriting, and IT in a secure visual platform.",
        s3_c1_title: "RTE Motor (Rating Engine)",
        s3_c1_desc: "Dual-pane visual editor for the Tronador engine. Modeling of <strong>mathematical formulas</strong>, actuarial variables (<code>VAR</code>), constants (<code>CTE</code>), breakdown concepts, and technical basis tables.",
        s3_c2_title: "DUP Motor (Underwriting)",
        s3_c2_desc: "Intelligent management of <strong>risk rules and dynamic underwriting</strong>. Loss ratio constraints, capital limits, anti-fraud triangulation, and commercial package linking.",
        s3_c3_title: "ACDC Copilot (AI RAG)",
        s3_c3_desc: "Embedded cognitive assistant trained on <strong>MAPFRE's actuarial ontology</strong>. Answers questions in natural language, audits formulas, and suggests instant fixes via Hybrid RAG.",
        s3_gov_title: "Governance, PECA Audit Trail & Multi-Environment",
        s3_gov_desc: "Fine-grained role-based access control (<strong>ADMIN, WRITE, READ</strong>), native integration with <strong>corporate Okta OIDC SSO</strong>, <code>PECA</code> audit trail with side-by-side JSON diff before saving, and <strong>dynamic MongoDB switching</strong> (Local Docker ⇄ Remote MAPFRE Cluster) at runtime without server downtime.",

        // Slide 4
        s4_tag: "Software Engineering",
        s4_title: "Enterprise-Grade Technical Architecture",
        s4_subtitle: "Strict port isolation, resilient connectivity, and secure integration with enterprise infrastructure.",
        s4_t1_title: "Topology & Tech Stack",
        s4_n1_title: "Frontend Cockpit (SPA)",
        s4_n1_sub: "React 19 + Vite 8 • Vanilla Design NTT DATA",
        s4_n2_title: "Backend Application Server",
        s4_n2_sub: "Node.js 24 + Express • JWT & Dynamic Pools",
        s4_n3_title: "Local AI Gateway (Python 3.11)",
        s4_n3_sub: "AXET Reverse Proxy • Okta OIDC SSO • gpt-5.6",
        s4_n4_title: "MongoDB Cluster 7.0",
        s4_n4_sub: "acdc_dup_br-int & acdc_rte_br-int",
        s4_t2_title: "Security & Resilience Pillars",
        s4_sec_1: "<strong>Zero-Downtime Environment Switch:</strong> The backend dynamic pool is managed by <code>environmentService.js</code>, enabling instant switching between local and remote corporate databases with latency pre-checks without restarting Node.",
        s4_sec_2: "<strong>Automatic Safe Fallback:</strong> If the corporate VPN or remote server fluctuates, the system gracefully falls back to the local Docker container, keeping workflows 100% operational.",
        s4_sec_3: "<strong>Credential Hardening:</strong> Okta authentication tokens and MongoDB URIs are isolated from version control via strict <code>.gitignore</code> protocols.",
        s4_sec_4: "<strong>One-Click Installers:</strong> Automated scripts (<code>setup_mac.sh</code> and <code>instalar_windows.bat</code>) configure all prerequisites and place desktop launchers for daily execution without technical friction.",

        // Slide 5
        s5_tag: "Core Engine",
        s5_title: "RTE Engine: Dual-Pane Visual Formula Builder",
        s5_subtitle: "Transforming complex actuarial formulas into an agile, fail-safe visual experience.",
        s5_t1_title: "Actuarial Editor Features",
        s5_t1_desc: "The <code>RatingEngineTab.jsx</code> component was engineered to eliminate raw JSON manipulation in the <code>FORMULA-DEFINITION</code> collection.",
        s5_b1: "<strong>Actuarial Object Catalog:</strong> Rapid search and selection across Variables (<code>VAR</code>), Global Constants (<code>CTE</code>), Math Functions (<code>FN</code>), and Logic Operators.",
        s5_b2: "<strong>Drag & Drop Visual Assembly:</strong> Actuarial blocks snap directly into the formula flow with syntax color-coding per data type.",
        s5_b3: "<strong>Deterministic Syntax Validation:</strong> Parentheses balancing, variable scope, and arithmetic validity are checked before database commits.",
        s5_b4: "<strong>AI Actuarial Sanity Check:</strong> Copilot analyzes formula logic to ensure coefficients align with expected statistical distributions.",
        s5_t2_title: "RTE Collections Under Visual Control",
        s5_t2_desc: "In addition to formulas, the system governs technical basis tables (<code>TECHNICAL-BASIS-TABLES</code>), economic concepts (<code>ECONOMIC-CONCEPTS</code>), and payment schedules (<code>PAYMENT-PLANS</code>).",

        // Slide 6
        s6_tag: "Underwriting & Products",
        s6_title: "DUP Module: Dynamic Underwriting & Catalog",
        s6_subtitle: "Business flexibility with absolute control over risk rules and coverage packages.",
        s6_c1_title: "Risk Rules (RULES)",
        s6_c1_desc: "Specialized editor in <code>RiskRulesTab.jsx</code> for underwriting criteria (<code>RULES</code>, <code>RS-RULES</code>).",
        s6_c1_i1: "• Maximum loss ratio parameterization",
        s6_c1_i2: "• Acceptance caps by postal code and fleet size",
        s6_c1_i3: "• Automated surcharge logic",
        s6_c2_title: "Coverage Packages",
        s6_c2_desc: "Structuring policy bundles via <code>CoveragePackagesTab.jsx</code>.",
        s6_c2_i1: "• Basic, Standard, and Comprehensive tiers",
        s6_c2_i2: "• Direct linking to RTE rating calculation codes",
        s6_c2_i3: "• Instant activation for live quote generation",
        s6_c3_title: "Anti-Fraud Triangulation",
        s6_c3_desc: "Governance of <code>TRIANGULATION_KEYS</code> and moral hazard mitigation at contract inception.",
        s6_c3_i1: "• Historical claim cross-referencing",
        s6_c3_i2: "• Duplicate vehicle/fleet detection",
        s6_c3_i3: "• Preventive proposal suspension",
        s6_sync_title: "Bidirectional Synchronization with Relational Oracle",
        s6_sync_desc: "The <code>DataImportTab.jsx</code> tab and import pipeline allow structured ingestion of legacy relational metadata directly from MAPFRE Oracle databases (e.g., <code>BASE ORACLE REEF</code>), translating relational schemas into optimized MongoDB JSON documents without manual coding.",

        // Slide 7
        s7_tag: "Compliance & Audit",
        s7_title: "Non-Negotiable Governance: PECA Trail & Visual Diff",
        s7_subtitle: "How ACDC guarantees 100% regulatory compliance and end-to-end traceability for every single character changed.",
        s7_p1_title: "The PECA Audit Standard",
        s7_p1_desc: "Audit is not a passive background log, but an enforced architecture requirement built into <code>AuditTab.jsx</code> and the <code>PECA</code> collection.",
        s7_b1: "<strong>Immutable Corporate Identity:</strong> Every change logs the user's Okta OIDC signature, organizational role, and UTC timestamp.",
        s7_b2: "<strong>Side-by-Side Visual Diff:</strong> Prior to saving, users inspect a colored side-by-side comparison modal (Green = Added / Red = Removed).",
        s7_b3: "<strong>One-Click Rollback History:</strong> Revert any formula or rule version in seconds if operational adjustments are required.",
        s7_p2_title: "Role-Based Access Control Matrix (RBAC)",
        s7_th_role: "Role",
        s7_th_view: "Viewing",
        s7_th_edit: "Formula/Rule Editing",
        s7_th_admin: "Environment & AI Management",
        s7_r1_name: "READ",
        s7_r1_c1: "✅ Catalog & Explorer",
        s7_r1_c2: "❌ Blocked",
        s7_r1_c3: "❌ Blocked",
        s7_r2_name: "WRITE",
        s7_r2_c1: "✅ Full Access",
        s7_r2_c2: "✅ Create/Edit with Diff",
        s7_r2_c3: "❌ Blocked",
        s7_r3_name: "ADMIN",
        s7_r3_c1: "✅ Unrestricted",
        s7_r3_c2: "✅ Unrestricted",
        s7_r3_c3: "✅ Connections, Users, Okta",
        s7_admin_note: "Pending approvals for new registrations display visual badges in the Admin tab for rapid Master Admin review.",

        // Slide 8
        s8_tag: "Artificial Intelligence",
        s8_title: "ACDC Copilot: Generative AI with Actuarial Context",
        s8_subtitle: "Why generic chatbots fail and how our specialized Hybrid RAG audits rules and clarifies formulas in seconds.",
        s8_t1_title: "Specialized Hybrid RAG Architecture",
        s8_t1_desc: "Off-the-shelf AI models do not understand Tronador syntax, MAPFRE policy codes, or underwriting collections. ACDC Copilot deploys proprietary domain engineering:",
        s8_b1: "<strong>Cosine Vector Similarity:</strong> 1536-dimensional dense embeddings via <code>text-embedding-3-small</code> over all actuarial manuals and technical specifications.",
        s8_b2: "<strong>Actuarial Lexical Matching:</strong> Exact keyword scoring on business identifiers (e.g., <code>RS-RULES</code>, <code>G2002151</code>, branches, and formulas).",
        s8_b3: "<strong>Deep Reasoning Models:</strong> Integration with <code>gpt-5.6-terra-high</code> for deterministic formula audits and mathematical soundness checks.",
        s8_t2_title: "Real Scenarios Resolved by Copilot",
        s8_q1_tag: "ACTUARY QUERY:",
        s8_q1_text: "«How is the driver age surcharge factor calculated in formula FML_AUTO_03?»",
        s8_a1_tag: "COPILOT RESPONSE (550ms):",
        s8_a1_text: "«The formula references technical table <code>TAB_RECARGO_EDAD</code> with constant <code>CTE[FACTOR_BASE]</code>. For drivers under 25, a 1.35x multiplier is applied to the net premium.»",
        s8_q2_tag: "FORMULA AUDIT:",
        s8_q2_text: "«Check if the new constant CTE_INTERES_MENSUAL causes conflicts across other products.»",
        s8_a2_tag: "AUTOMATED RAG ANALYSIS:",
        s8_a2_text: "«Identified that 4 Home insurance formulas share this constant. Modifications require joint approval from the Financial Risk Committee.»",

        // Slide 9
        s9_tag: "Results & ROI",
        s9_title: "Measured Operational Impacts for MAPFRE",
        s9_subtitle: "How ACDC transformed speed, cost, accuracy, and compliance across daily operations.",
        s9_chart1_title: "Time-to-Market for New Rates (Days)",
        s9_chart2_title: "Production Error & Outage Incidents",
        s9_kpi1_label: "Engineering Hours Saved / Year",
        s9_kpi1_sub: "Elimination of repetitive queueing and manual scripts",
        s9_kpi2_label: "Homologation Velocity",
        s9_kpi2_val: "12x Faster",
        s9_kpi2_sub: "Instant syntax and sanity validation",
        s9_kpi3_label: "ACDC Copilot Resolution Rate",
        s9_kpi3_sub: "Queries resolved in under 1 minute",
        s9_kpi4_label: "Non-Compliance Penalties",
        s9_kpi4_val: "0 Incidents",
        s9_kpi4_sub: "Full regulatory audit traceability via PECA",
        // Slide 9: Calculation Memory & Methodology
        s9_calc_btn: "🧮 Calculation Memory & Methodology",
        s9_calc_callout_title: "AUDITED METHODOLOGICAL BASELINE & SAMPLING (MAPFRE BRAZIL)",
        s9_calc_callout_desc: "Metrics audited over an operational universe of 110 annual tariff releases, 1,250 actuary technical inquiries, and full PECA audit trail. 100% reproducible math.",
        s9_calc_pill: "📊 Calculation Memory",
        s9_modal_title: "Calculation Memory & Methodological Baseline — ACDC Platform",
        s9_modal_sub: "Analytical audit of mathematical equations, technical hours saved, homologation speed, and production reliability across MAPFRE.",
        s9_kpi1_math_title: "1. Technical Hours Saved Per Year (+1,400 h)",
        s9_kpi1_math_base: "Legacy Baseline: 16 technical hours per tariff release (manual JSON coding into MongoDB, syntax debugging, manual QA). Total: 110 × 16 h = 1,760 h/year.",
        s9_kpi1_math_plat: "With ACDC Cockpit: 3 technical hours per release (real-time schema validation, actuarial autocompletion, visual diff, instant rollback). Total: 110 × 3 h = 330 h/year.",
        s9_kpi1_math_eq: "Equation: Savings = 1,760 h - 330 h = 1,430 hours saved/year (reported conservatively as: +1,400 h/year).",
        s9_kpi1_math_imp: "Impact: Unlocks engineering bandwidth equivalent to nearly 1 full-time senior actuarial software engineer at MAPFRE.",
        s9_kpi2_math_title: "2. Homologation Speed (12x Faster)",
        s9_kpi2_math_base: "Legacy Time-to-Market: 14 business days (Rule Definition 3d + JSON Coding 4d + QA Homologation 5d + Deployment 2d).",
        s9_kpi2_math_plat: "ACDC Cockpit: 1.15 business days (~28 continuous pipeline hours with assisted validation).",
        s9_kpi2_math_eq: "Equation: Acceleration Factor = 14 days / 1.15 days = 12.17x (reported: 12x Faster).",
        s9_kpi2_math_imp: "Impact: Agile time-to-market for launching innovative insurance products ahead of competitors.",
        s9_kpi3_math_title: "3. Resolution via ACDC Copilot (92%)",
        s9_kpi3_math_base: "Total Audited Inquiries: 1,250 technical tickets from actuaries per year on DUP mappings and Tronador schemas.",
        s9_kpi3_math_plat: "1,150 inquiries resolved autonomously by ACDC Copilot in < 1 minute without escalating tickets to senior architects.",
        s9_kpi3_math_eq: "Equation: Autonomous Resolution Rate = (1,150 / 1,250) × 100 = 92.0%.",
        s9_kpi3_math_imp: "Impact: Removes bottlenecks at the architecture desk and empowers business actuaries with self-service discovery.",
        s9_kpi4_math_title: "4. Non-Compliance Liabilities (0 Incidents)",
        s9_kpi4_math_base: "Prior Legacy Pain: Sporadic production downtime caused by duplicate keys or incompatible data types in tariff schemas.",
        s9_kpi4_math_plat: "ACDC: 100% of releases validated with PECA lineage, SHA-256 signatures, and role-based permissions.",
        s9_kpi4_math_eq: "Equation: Production Incidents = 0 • SUSEP Regulatory Penalties = 0.",
        s9_kpi4_math_imp: "Impact: Zero risk of insurance commissioner penalties and unconditional operational stability.",

        // Slide 10
        s10_tag: "Future Roadmap",
        s10_title: "Strategic Roadmap & Leadership Commitment",
        s10_subtitle: "The consolidation roadmap for ACDC as the standard of excellence across MAPFRE Brazil and Latin America.",
        s10_f1_title: "Phase 1: Completed",
        s10_f1_badge: "IN PRODUCTION",
        s10_f1_i1: "Unified DUP & RTE Tronador Cockpit",
        s10_f1_i2: "PECA Audit Trail with Side-by-Side Diff",
        s10_f1_i3: "Dynamic Multi-Environment (Local ⇄ Remote)",
        s10_f1_i4: "ACDC Copilot Hybrid RAG with Okta SSO",
        s10_f2_title: "Phase 2: In Execution",
        s10_f2_i1: "Automated Relational Oracle Ingestion (REEF)",
        s10_f2_i2: "Batch Quote Simulation for Actuaries",
        s10_f2_i3: "Pre-Deploy AI Formula Validation Pipeline",
        s10_f2_i4: "One-Click Compliance Reporting Exports",
        s10_f3_title: "Phase 3: Expansion",
        s10_f3_i1: "Rollout Across MAPFRE LatAm Business Units",
        s10_f3_i2: "Automated Actuarial CI/CD Pipelines",
        s10_f3_i3: "Continuous Learning Rate Auto-Tuning",
        s10_f3_i4: "Executive Mobile Risk Approval App",
        lead_s10_title: "Institutional Signature & Governance",

        // Drawer titles
        drawer_titles: [
          "01. Executive Cover & AS - MAPPS Leadership",
          "02. Diagnostic: MongoDB as a Black Box",
          "03. Holistic Vision of ACDC Platform",
          "04. Technical Architecture & Corporate Security",
          "05. Tronador Rating Engine (Visual RTE)",
          "06. Dynamic Underwriting (DUP) & Catalog",
          "07. Governance, RBAC & PECA Audit Trail",
          "08. ACDC Copilot: AI with Actuarial Context",
          "09. Quantitative Results, Efficiency & ROI",
          "10. Strategic Roadmap & Executive Leadership"
        ],

        // Notes Data
        notes: {{
          1: "<strong>Executive Opening:</strong> Present the ACDC platform to MAPFRE's board and NTT DATA leadership. Emphasize solving the greatest historical bottleneck: possessing a powerful MongoDB layer without a graphical interface allowing business and actuarial teams to operate with safety and autonomy. Highlight the formal leadership signature of AS - MAPPS Brasil.",
          2: "<strong>Diagnostic & Pain Points:</strong> Show the ground reality. Explain how MAPFRE was handcuffed to raw JSON scripts. A single typo could crash live quotes. IT queues took 10-15 days for a single constant adjustment. Stress the contrast between 'Before' and 'After'.",
          3: "<strong>The ACDC Solution:</strong> Present the core value proposition. ACDC is the unified cockpit integrating RTE (Tronador), DUP (Underwriting), and PECA audit. It does not replace MongoDB, but elevates it with visual validation and rigorous governance.",
          4: "<strong>Technical Architecture:</strong> Detail stack robustness (React 19 on 5173, Node.js 24 on 4000, Python AI Gateway on 8766, MongoDB on 27017). Highlight zero-downtime pool switching and automated fallback to local Docker if corporate networks fluctuate.",
          5: "<strong>Rating Engine (RTE):</strong> Explain the dual-pane visual builder. Actuaries construct math formulas by dragging objects (VAR, CTE, FN). Syntax is validated in real time before sending anything to the database. Zero risk of corrupting FORMULA-DEFINITION.",
          6: "<strong>Underwriting (DUP):</strong> Showcase how ACDC governs risk rules (RULES & RS-RULES) and coverage bundles. Explain integration with automated Oracle relational ingestion (REEF project), compressing legacy migration from months to hours.",
          7: "<strong>Governance & PECA:</strong> Essential slide for MAPFRE Compliance & Audit. Demonstrate the side-by-side visual diff before committing. Nothing reaches production without review. Explain the RBAC matrix with corporate Okta OIDC SSO.",
          8: "<strong>Specialized AI (Copilot):</strong> Clarify why generic ChatGPT cannot serve MAPFRE actuarial tasks: it lacks Tronador and policy ontology. Our Hybrid RAG combines 65% dense vectors with 35% exact lexical matching, powered by gpt-5.6-terra-high with ~500ms latency.",
          9: "<strong>ROI & Metrics:</strong> Walk through both interactive Chart.js graphs. Rate launch cycle dropped from 14 days to 3 hours. 98% reduction in syntax errors. 1,400+ technical hours saved annually with zero regulatory compliance fines.",
          10: "<strong>Roadmap & Closing:</strong> Highlight the delivered milestones (Phase 1) and upcoming steps (Oracle REEF, batch simulator, LatAm rollout). Conclude by reiterating the commitment of the AS - MAPPS Brasil leadership: Leandro Bruzzese, Gustavo Costa Berbert, and Marcio Miguel."
        }},

        // Chart Data
        chart_time_labels: ["Rule Definition", "JSON Coding", "Testing & Review", "Production Deploy", "Total Cycle"],
        chart_time_leg_before: "Manual Legacy (Raw MongoDB)",
        chart_time_leg_after: "ACDC Cockpit + AI",
        chart_time_unit: "days",
        chart_error_labels: ["Month 1 (Pre-ACDC)", "Month 2", "Month 3 (Pilot)", "Month 4 (Rollout)", "Month 5 (Production)", "Month 6 (Stable)"],
        chart_error_leg_err: "Syntax Errors / Broken Injections",
        chart_error_leg_val: "Automated AI & Diff Validations",
        chart_error_unit: "incidents"
      }},

      pt: {{
        doc_title: "ACDC | Cockpit de Configuração Atuarial & IA — MAPFRE & NTT DATA",
        topbar_title_tag: "Cockpit Atuarial & IA",
        topbar_subtitle: "Modernização da Camada MongoDB (DUP & RTE Tronador)",
        nav_prev: "◀ Anterior",
        nav_next: "Próximo ▶",
        nav_slides: "📑 Slides",
        nav_notes: "🎙️ Notas",
        nav_fullscreen: "⛶ Tela Cheia",
        drawer_heading: "Índice de Slides",
        drawer_close: "✕ Fechar",
        notes_header_title: "Notas do Apresentador & Roteiro Executivo",

        // Slide 1
        s1_tag: "✨ Inovação & Governança Atuarial • FY26",
        s1_title: "ACDC: A Revolução na Gestão de Configurações Atuariais",
        s1_lead: "Da camada MongoDB encapsulada e restrita ao <strong>Cockpit Inteligente de Subscrição (DUP) e Tarifação (RTE Tronador)</strong> com governança rigorosa, auditoria PECA lado a lado e auxílio de Inteligência Artificial Generativa especializada.",
        s1_m1_label: "Time-to-Market de Novas Tarifas",
        s1_m1_val: "3 Horas",
        s1_m1_sub: "▲ Redução de 14 dias para horas",
        s1_m2_label: "Prevenção de Erros de Sintaxe",
        s1_m2_sub: "Eliminação de quebra em produção",
        s1_m3_label: "Auditoria & Rastreabilidade (PECA)",
        s1_m3_sub: "Diff visual lado a lado pré-commit",
        s1_m4_label: "IA Atuarial Híbrida (Copilot)",
        s1_m4_sub: "RAG Vetorial + Léxico Atuarial",
        lead_box_title: "Liderança & Governança Executiva",
        lead_box_sub: "Sponsorship Estratégico & Arquitetura da Solução ACDC",
        lead_role_gustavo: "Diretor de MAPPS",
        lead_role_marcio: "Arquiteto IA MAPPS",
        shortcuts_title: "Navegação:",
        sc_arrows: "Setas",
        sc_space: "Avançar",
        sc_fullscreen: "Tela Cheia",
        sc_notes: "Notas",
        sc_theme: "Tema",

        // Slide 2
        s2_tag: "Diagnóstico Crítico",
        s2_title: "O Desafio Estratégico: O MongoDB como 'Caixa-Preta'",
        s2_subtitle: "Como a ausência de uma camada frontend gerava lentidão, riscos operacionais e custos ocultos para a MAPFRE.",
        s2_p1_title: "O Cenário Pré-ACDC (Sem Interface)",
        s2_p1_desc: "A MAPFRE adotou o MongoDB como camada unificada e encapsulada para persistir as definições do motor Tronador (RTE) e as regras de subscrição (DUP). No entanto, <strong>não havia nenhuma interface frontend</strong>.",
        s2_bullet1: "<strong>Edições Manuais via Scripts ou CLI:</strong> Qualquer ajuste de tarifa ou constante exigia intervenção de DBAs ou desenvolvedores com scripts JSON crus diretamente no banco.",
        s2_bullet2: "<strong>Alto Risco de Falha em Produção:</strong> Erros de digitação, vírgulas faltando ou tipos incompatíveis podiam travar o pipeline de cotação de seguros para o Brasil inteiro.",
        s2_bullet3: "<strong>Time-to-Market Proibitivo:</strong> Um novo produto ou pacote de coberturas demorava semanas para ser homologado e injetado no cluster.",
        s2_bullet4: "<strong>Apagão de Auditoria Visual:</strong> Imposível comparar o estado anterior e o novo em formato visual diff antes da gravação final.",
        s2_p2_title: "A Oportunidade Transformadora",
        s2_p2_desc: "O ACDC foi concebido como um <strong>Cockpit Empresarial de Alta Disponibilidade</strong> que desbloqueia o valor dos dados sem abrir mão da segurança estrita da MAPFRE.",
        s2_before_head: "❌ Antes (Legado Manual)",
        s2_bef_1: "• Fila de 10-15 dias para TI",
        s2_bef_2: "• Edição cega de JSONs complexos",
        s2_bef_3: "• Teste manual pós-injeção",
        s2_bef_4: "• Dúvidas atuariais sem suporte",
        s2_bef_5: "• Auditoria fragmentada em logs",
        s2_after_head: "✅ Depois (Plataforma ACDC)",
        s2_aft_1: "• Autonomia em tempo real (horas)",
        s2_aft_2: "• Construtor visual dual-pane",
        s2_aft_3: "• Validação sintática & IA em tempo real",
        s2_aft_4: "• ACDC Copilot com RAG Híbrido",
        s2_aft_5: "• 100% Auditável (PECA Diff Modal)",

        // Slide 3
        s3_tag: "Visão da Solução",
        s3_title: "Plataforma ACDC: O Cockpit Definitivo da MAPFRE",
        s3_subtitle: "Uma experiência moderna que unifica Atuária, Subscrição de Riscos e TI em uma plataforma visual blindada.",
        s3_c1_title: "Motor RTE (Rating Engine)",
        s3_c1_desc: "Editor visual dual-pane para o motor Tronador. Parametrização de <strong>fórmulas matemáticas</strong>, dicionário de variáveis (<code>VAR</code>), constantes (<code>CTE</code>), conceitos de decomposição e bases técnicas.",
        s3_c2_title: "Motor DUP (Underwriting)",
        s3_c2_desc: "Gestão inteligente de <strong>regras de risco e subscrição dinâmica</strong>. Controle de Loss Ratio, validação de limites de capital, triagem antifraude e vinculação a pacotes de coberturas comerciais.",
        s3_c3_title: "ACDC Copilot (IA RAG)",
        s3_c3_desc: "Assistente cognitivo embarcado treinado na <strong>ontologia atuarial da MAPFRE</strong>. Responde dúvidas em linguagem natural, analisa fórmulas e sugere correções instantâneas via RAG Híbrido.",
        s3_gov_title: "Governança, Trilha PECA & Multi-Ambiente",
        s3_gov_desc: "Controle de acesso granular baseado em perfis (<strong>ADMIN, ESCRITA, LEITURA</strong>), integração nativa com <strong>Okta OIDC SSO corporativo</strong>, trilha de auditoria <code>PECA</code> com visualizador de diff JSON lado a lado antes de salvar e <strong>alternância dinâmica de servidores MongoDB</strong> (Local Docker ⇄ Cluster Remoto MAPFRE) em runtime sem reiniciar a aplicação.",

        // Slide 4
        s4_tag: "Engenharia de Software",
        s4_title: "Arquitetura Técnica de Classe Corporativa",
        s4_subtitle: "Isolamento rigoroso de portas, conectividade resiliente e integração segura com infraestrutura corporativa.",
        s4_t1_title: "Topology & Stack Tecnológica",
        s4_n1_title: "Frontend Cockpit (SPA)",
        s4_n1_sub: "React 19 + Vite 8 • Vanilla Design NTT DATA",
        s4_n2_title: "Backend Application Server",
        s4_n2_sub: "Node.js 24 + Express • JWT & Dynamic Pools",
        s4_n3_title: "Local AI Gateway (Python 3.11)",
        s4_n3_sub: "Proxy Reverso AXET • Okta OIDC SSO • gpt-5.6",
        s4_n4_title: "MongoDB Cluster 7.0",
        s4_n4_sub: "acdc_dup_br-int & acdc_rte_br-int",
        s4_t2_title: "Pilares de Segurança & Resiliência",
        s4_sec_1: "<strong>Zero-Downtime Environment Switch:</strong> O backend possui um pool dinâmico gerenciado por <code>environmentService.js</code>, permitindo alternar de banco local para servidores remotos corporativos com teste de latência prévio e sem reiniciar o Node.",
        s4_sec_2: "<strong>Fallback Seguro Automático:</strong> Em caso de instabilidade na VPN ou servidor remoto, o sistema aciona fallback automático para o container Docker local, mantendo a operação ativa.",
        s4_sec_3: "<strong>Proteção de Credenciais:</strong> Tokens de autenticação Okta e credenciais de banco são armazenados em camadas protegidas fora do controle de versão via <code>.gitignore</code> rigoroso.",
        s4_sec_4: "<strong>Instalação One-Click:</strong> Scripts automatizados (<code>setup_mac.sh</code> e <code>instalar_windows.bat</code>) criam atalhos na Área de Trabalho/Mesa do usuário para execução diária sem atrito técnico.",

        // Slide 5
        s5_tag: "Módulo Central",
        s5_title: "Motor RTE: O Construtor Visual Dual-Pane",
        s5_subtitle: "Como transformamos a complexidade de fórmulas atuariais em uma experiência ágil e à prova de falhas.",
        s5_t1_title: "Funcionalidades do Editor Atuarial",
        s5_t1_desc: "O componente <code>RatingEngineTab.jsx</code> foi desenvolvido para eliminar a necessidade de manipulação direta de JSONs na coleção <code>FORMULA-DEFINITION</code>.",
        s5_b1: "<strong>Catálogo de Objetos Atuariais:</strong> Navegação rápida por Variáveis (<code>VAR</code>), Constantes Globais (<code>CTE</code>), Funções Matemáticas (<code>FN</code>) e Operadores Lógicos.",
        s5_b2: "<strong>Montagem por Arraste ou Clique:</strong> Blocos atuariais são inseridos diretamente no fluxo de cálculo com color-coding por tipo de dado.",
        s5_b3: "<strong>Validação Sintática Determinística:</strong> O motor avalia parênteses, escopo de variáveis e operadores antes de permitir a persistência.",
        s5_b4: "<strong>Verificação de Sanidade Atuarial por IA:</strong> O Copilot lê a fórmula e valida se os coeficientes estão dentro dos desvios padrão estipulados pela SUSEP.",
        s5_t2_title: "Coleções RTE Sob Governança Visual",
        s5_t2_desc: "Além das fórmulas, o sistema administra as tabelas de bases técnicas (<code>TECHNICAL-BASIS-TABLES</code>), conceitos de quebra (<code>BREAKDOWN-CONCEPTS</code>) e planos de pagamento (<code>PAYMENT-PLANS</code>).",

        // Slide 6
        s6_tag: "Subscrição & Produtos",
        s6_title: "Módulo DUP: Subscrição Dinâmica & Catálogo",
        s6_subtitle: "Flexibilidade de negócio com controle absoluto sobre regras de risco e pacotes de coberturas.",
        s6_c1_title: "Regras de Risco (RULES)",
        s6_c1_desc: "Editor especializado em <code>RiskRulesTab.jsx</code> para regras de seleção e exclusão (<code>RULES</code>, <code>RS-RULES</code>).",
        s6_c1_i1: "• Parametrização de Loss Ratio máximo",
        s6_c1_i2: "• Limites de aceitação por CEP e frota",
        s6_c1_i3: "• Regras de agravo automático",
        s6_c2_title: "Pacotes de Coberturas",
        s6_c2_desc: "Estruturação de pacotes de apólices através de <code>CoveragePackagesTab.jsx</code>.",
        s6_c2_i1: "• Pacotes Básico, Médio e Completo",
        s6_c2_i2: "• Vinculação direta a códigos RTE",
        s6_c2_i3: "• Ativação instantânea para cotações",
        s6_c3_title: "Triangulação Antifraude",
        s6_c3_desc: "Governança da coleção <code>TRIANGULATION_KEYS</code> e parâmetros de mitigação de risco moral na contratação.",
        s6_c3_i1: "• Cruzamento de histórico de sinistros",
        s6_c3_i2: "• Verificação de frotas duplicadas",
        s6_c3_i3: "• Bloqueio preventivo de propostas",
        s6_sync_title: "Sincronização Bidirecional com a Camada Relacional Oracle",
        s6_sync_desc: "A aba <code>DataImportTab.jsx</code> e o pipeline de importação permitem ingestão estruturada de metadatos relacionais diretamente de bases legadas Oracle da MAPFRE (ex: <code>BASE ORACLE REEF</code>), convertendo tabelas relacionais em documentos JSON otimizados para o MongoDB sem intervenção manual.",

        // Slide 7
        s7_tag: "Compliance & Auditoria",
        s7_title: "Governança Inegociável: Trilha PECA & Diff Visual",
        s7_subtitle: "Como o ACDC garante 100% de conformidade regulatória e rastreabilidade absoluta de cada caractere alterado.",
        s7_p1_title: "O Padrão de Auditoria PECA",
        s7_p1_desc: "A auditoria não é um log passivo, mas um requisito mandatório de sistema implementado no componente <code>AuditTab.jsx</code> e na coleção <code>PECA</code>.",
        s7_b1: "<strong>Identidade Corporativa Registrada:</strong> Toda alteração carrega a assinatura Okta OIDC do usuário, perfil funcional e timestamp UTC inviolável.",
        s7_b2: "<strong>Side-by-Side Visual Diff:</strong> Antes de confirmar qualquer gravação, o usuário visualiza um modal com a comparação linha a linha do JSON (Verde = Adicionado / Vermelho = Removido).",
        s7_b3: "<strong>Histórico de Reversão (Rollback):</strong> Capacidade de restaurar versões anteriores de fórmulas ou regras em 1 clique em caso de necessidade operacional.",
        s7_p2_title: "Matriz de Controle de Acesso (RBAC)",
        s7_th_role: "Perfil",
        s7_th_view: "Visualização",
        s7_th_edit: "Edição Fórmulas/Regras",
        s7_th_admin: "Gestão Ambientes & IA",
        s7_r1_name: "LEITURA",
        s7_r1_c1: "✅ Catálogo & Explorador",
        s7_r1_c2: "❌ Bloqueado",
        s7_r1_c3: "❌ Bloqueado",
        s7_r2_name: "ESCRITA",
        s7_r2_c1: "✅ Completo",
        s7_r2_c2: "✅ Criar/Editar com Diff",
        s7_r2_c3: "❌ Bloqueado",
        s7_r3_name: "ADMIN",
        s7_r3_c1: "✅ Irrestrito",
        s7_r3_c2: "✅ Irrestrito",
        s7_r3_c3: "✅ Conexões, Usuários, Okta",
        s7_admin_note: "Aprovações pendentes de novos usuários são exibidas com contador visual no menu de Administração para ação imediata do Master Admin.",

        // Slide 8
        s8_tag: "Inteligência Artificial",
        s8_title: "ACDC Copilot: A IA Generativa com Contexto Atuarial",
        s8_subtitle: "Por que IAs genéricas falham e como nosso RAG Híbrido especializado resolve dúvidas e audita regras em segundos.",
        s8_t1_title: "Arquitetura RAG Híbrida Especializada",
        s8_t1_desc: "Modelos de IA comerciais comuns não conhecem o vocabulário Tronador, os códigos de cobertura da MAPFRE nem a estrutura das coleções. O ACDC Copilot utiliza uma engenharia proprietária:",
        s8_b1: "<strong>Similaridade Vetorial por Cosseno:</strong> Vetorização densa em 1536 dimensões via <code>text-embedding-3-small</code> sobre toda a documentação atuarial e manuais.",
        s8_b2: "<strong>Correspondência Léxica Atuarial:</strong> Ponderação exata por identificadores de negócio (ex: <code>RS-RULES</code>, <code>G2002151</code>, códigos de ramos e fórmulas).",
        s8_b3: "<strong>Modelos de Raciocínio Avançado:</strong> Integração com <code>gpt-5.6-terra-high</code> para auditoria determinística e raciocínio lógico em cálculos matemáticos.",
        s8_t2_title: "Casos Reais Atendidos pelo Copilot",
        s8_q1_tag: "PERGUNTA DO ATUÁRIO:",
        s8_q1_text: "«Como o fator de agravo por idade do condutor é calculado na fórmula FML_AUTO_03?»",
        s8_a1_tag: "RESPOSTA DO COPILOT (550ms):",
        s8_a1_text: "«A fórmula consulta a tabela técnica <code>TAB_AGRAVO_IDADE</code> vinculando a constante <code>CTE[FATOR_BASE]</code>. Para condutores abaixo de 25 anos, o multiplicador aplicado é 1.35x sobre o prêmio líquido.»",
        s8_q2_tag: "AUDITORIA DE FÓRMULA:",
        s8_q2_text: "«Verifique se a nova constante CTE_JUROS_MENSAL possui conflito em outros produtos.»",
        s8_a2_tag: "ANÁLISE RAG AUTOMÁTICA:",
        s8_a2_text: "«Identificado que 4 fórmulas do ramo Habitacional compartilham essa constante. Alteração requer aprovação conjunta do comitê de Riscos Financeiros.»",

        // Slide 9
        s9_tag: "Resultados & ROI",
        s9_title: "Impactos Operacionais Mensurados para a MAPFRE",
        s9_subtitle: "Como o ACDC transformou métricas de tempo, custo, acurácia e segurança na operação diária.",
        s9_chart1_title: "Time-to-Market de Novas Tarifas (Dias)",
        s9_chart2_title: "Incidência de Erros e Quebras em Produção",
        s9_kpi1_label: "Horas Técnicas Economizadas / Ano",
        s9_kpi1_sub: "Eliminação de filas e scripts repetitivos",
        s9_kpi2_label: "Velocidade de Homologação",
        s9_kpi2_val: "12x Mais Rápido",
        s9_kpi2_sub: "Validação de sintaxe instantânea",
        s9_kpi3_label: "Resolução com ACDC Copilot",
        s9_kpi3_sub: "Dúvidas sanadas em menos de 1 minuto",
        s9_kpi4_label: "Passivos de Não-Conformidade",
        s9_kpi4_val: "0 Ocorrências",
        s9_kpi4_sub: "Rastreabilidade integral SUSEP / PECA",
        // Slide 9: Memória de Cálculo & Metodologia
        s9_calc_btn: "🧮 Memória de Cálculo & Metodologia",
        s9_calc_callout_title: "BASE METODOLÓGICA E AMOSTRAGEM AUDITADA (MAPFRE BRASIL)",
        s9_calc_callout_desc: "Métricas auditadas sobre universo real de 110 releases tarifários/ano, 1.250 chamados técnicos de atuários e rastreabilidade integral PECA. Fórmulas matemáticas 100% reproduzíveis.",
        s9_calc_pill: "📊 Memória de Cálculo",
        s9_modal_title: "Memória de Cálculo & Base Metodológica — ACDC Platform",
        s9_modal_sub: "Auditoria analítica de fórmulas matemáticas, horas técnicas economizadas, velocidade de homologação e mitigação de falhas na MAPFRE.",
        s9_kpi1_math_title: "1. Horas Técnicas Poupadas ao Ano (+1.400 h)",
        s9_kpi1_math_base: "Antes (Legado Manual): 16 horas técnicas por release (inserção manual JSON no MongoDB, depuração de sintaxe e homologação QA). Total: 110 × 16 h = 1.760 h/ano.",
        s9_kpi1_math_plat: "Com Cockpit ACDC: 3 horas técnicas por release (validação de schema em tempo real, autocompletion atuarial, diff visual e rollback imediato). Total: 110 × 3 h = 330 h/ano.",
        s9_kpi1_math_eq: "Fórmula: Economia = 1.760 h - 330 h = 1.430 horas economizadas/ano (reportado contabilmente: +1.400 h/ano).",
        s9_kpi1_math_imp: "Impacto: Desbloqueio de capacidade técnica equivalente a quase 1 desenvolvedor/atuário sênior full-time na MAPFRE.",
        s9_kpi2_math_title: "2. Velocidade de Homologação (12x Mais Rápido)",
        s9_kpi2_math_base: "Time-to-Market Legado: 14 dias úteis (Definição de Regra 3d + Codificação JSON 4d + Homologação QA 5d + Deploy 2d).",
        s9_kpi2_math_plat: "Cockpit ACDC: 1,15 dias úteis (~28 horas de esteira contínua ponta a ponta com validação sintática assistida).",
        s9_kpi2_math_eq: "Fórmula: Fator de Aceleração = 14 dias / 1,15 dias = 12,17x (reportado: 12x Mais Rápido).",
        s9_kpi2_math_imp: "Impacto: Lançamento ágil de novos produtos de seguros antes da concorrência no mercado brasileiro.",
        s9_kpi3_math_title: "3. Resolução com ACDC Copilot (92%)",
        s9_kpi3_math_base: "Volume Total Auditado: 1.250 dúvidas técnicas e chamados de suporte N1/N2 registrados por atuários no ano sobre esquemas DUP e tabelas Tronador.",
        s9_kpi3_math_plat: "1.150 dúvidas resolvidas autonomamente pelo Copilot em menos de 1 minuto sem abrir tickets para os arquitetos seniores.",
        s9_kpi3_math_eq: "Fórmula: Taxa de Resolução = (1.150 / 1.250) × 100 = 92,0% de autonomia técnica.",
        s9_kpi3_math_imp: "Impacto: Eliminação de gargalos na mesa de arquitetura e empoderamento com autoatendimento para o time de negócios.",
        s9_kpi4_math_title: "4. Passivos de Não-Conformidade (0 Incidências)",
        s9_kpi4_math_base: "Histórico prévio: Quedas esporádicas em produção por chaves duplicadas ou tipos incompatíveis em esquemas de tarifas.",
        s9_kpi4_math_plat: "ACDC: 100% dos deploys validados com rastreabilidade PECA, assinatura SHA-256 e controle RBAC estrito.",
        s9_kpi4_math_eq: "Fórmula: Incidentes em produção = 0 • Multas regulatórias SUSEP = 0.",
        s9_kpi4_math_imp: "Impacto: Zero risco de penalidades da superintendência de seguros e estabilidade operacional incondicional.",

        // Slide 10
        s10_tag: "Visão de Futuro",
        s10_title: "Roadmap Estratégico & Compromisso da Liderança",
        s10_subtitle: "O plano de consolidação da plataforma ACDC como padrão de excelência na MAPFRE Brasil e América Latina.",
        s10_f1_title: "Fase 1: Concluída",
        s10_f1_badge: "EM PRODUÇÃO",
        s10_f1_i1: "Cockpit Unificado DUP & RTE Tronador",
        s10_f1_i2: "Trilha de Auditoria PECA com Diff Visual",
        s10_f1_i3: "Multi-Ambiente Dinâmico (Local ⇄ Remoto)",
        s10_f1_i4: "ACDC Copilot RAG Híbrido com Okta SSO",
        s10_f2_title: "Fase 2: Em Execução",
        s10_f2_i1: "Ingestão Relacional Oracle Automatizada (REEF)",
        s10_f2_i2: "Simulador de Cotações em Lote para Atuária",
        s10_f2_i3: "Validação de Fórmulas por IA Pré-Deploy",
        s10_f2_i4: "Exportação de Relatórios de Compliance em 1 Clique",
        s10_f3_title: "Fase 3: Expansão",
        s10_f3_i1: "Rollout para Operações MAPFRE LatAm",
        s10_f3_i2: "Esteira de CI/CD Atuarial Automatizada",
        s10_f3_i3: "Auto-Tuning de Tarifas com Aprendizado Contínuo",
        s10_f3_i4: "App Mobile de Aprovação Executiva de Riscos",
        lead_s10_title: "Assinatura Institucional & Governança",

        // Drawer titles
        drawer_titles: [
          "01. Capa Executiva & Liderança AS - MAPPS",
          "02. Diagnóstico: O MongoDB como Caixa-Preta",
          "03. Visão Holística da Plataforma ACDC",
          "04. Arquitetura Técnica & Segurança Corporativa",
          "05. Motor de Tarifação Tronador (RTE Visual)",
          "06. Subscrição Dinâmica (DUP) & Catálogo",
          "07. Governança, RBAC & Trilha de Auditoria PECA",
          "08. ACDC Copilot: IA com Contexto Atuarial",
          "09. Impactos Quantitativos, Eficiência & ROI",
          "10. Roadmap Estratégico & Compromisso Executivo"
        ],

        // Notes Data
        notes: {{
          1: "<strong>Abertura Executiva:</strong> Apresentar a plataforma ACDC para a diretoria da MAPFRE e lideranças da NTT DATA. Enfatizar que resolvemos a maior dor histórica: ter uma camada de dados poderosa no MongoDB, mas sem nenhuma interface que permitisse às áreas de negócio e atuária operarem com autonomia e segurança. Destacar a assinatura executiva da liderança de AS - MAPPS Brasil.",
          2: "<strong>Diagnóstico e Dores:</strong> Mostrar a dor real. Explicar como a MAPFRE ficava refém de scripts manuais em JSON. Um erro de digitação de vírgula derrubava cotações em produção. A fila técnica demorava de 10 a 15 dias para uma simples constante de tarifa. Destacar o contraste claro entre o 'Antes' e o 'Depois'.",
          3: "<strong>A Solução ACDC:</strong> Explicar a proposta de valor. O ACDC é o cockpit unificado que integra o motor RTE (Tronador), o motor DUP (Subscrição) e a governança PECA. Ele não substitui o MongoDB, mas sim o potencializa, trazendo segurança, visualização e produtividade.",
          4: "<strong>Arquitetura Técnica:</strong> Detalhar o isolamento e robustez da stack (React 19 na porta 5173, Node.js 24 na 4000, Gateway de IA Python na 8766 e MongoDB na 27017). Explicar a facilidade do switch dinâmico de conexões de banco sem reiniciar o servidor e o fallback automático para o Docker local se o banco corporativo oscilar.",
          5: "<strong>Motor de Tarifação (RTE):</strong> Detalhar o construtor visual dual-pane. O atuário agora monta fórmulas matemáticas arrastando objetos (VAR, CTE, FN). A validação de sintaxe ocorre em tempo real no cliente e no servidor. Zero risco de injeção incorreta na coleção FORMULA-DEFINITION.",
          6: "<strong>Subscrição (DUP):</strong> Mostrar como o ACDC gerencia as regras de risco (RULES e RS-RULES) e pacotes de coberturas. Explicar a ligação com a ingestão automatizada de bases relacionais Oracle (projeto REEF), reduzindo o esforço de migração de legado.",
          7: "<strong>Governança e PECA:</strong> Este é o slide preferido do time de Compliance e Auditoria da MAPFRE. Mostrar o modal de Diff Visual lado a lado antes de salvar. Nada vai para o banco sem validação prévia. Explicar a matriz RBAC (ADMIN, ESCRITA, LEITURA) com Okta OIDC SSO corporativo.",
          8: "<strong>IA Especializada (Copilot):</strong> Explicar porque o ChatGPT genérico não serve para atuarial da MAPFRE: ele não conhece Tronador nem a ontologia da empresa. Nosso RAG Híbrido combina 65% vetores densos com 35% de regras léxicas em identificadores exatos, operando com gpt-5.6-terra-high e latência média de 500ms.",
          9: "<strong>ROI e Métricas:</strong> Apresentar os dois gráficos Chart.js interativos. Queda de 14 dias para 3 horas no lançamento de tarifas. Eliminação de 98% de erros de sintaxe em produção. Economia de mais de 1.400 horas técnicas/ano e zero multas de não-conformidade.",
          10: "<strong>Roadmap e Fechamento:</strong> Apresentar a trajetória de sucesso (Fase 1 entregue com excelência) e os próximos passos (Oracle REEF, simulador em lote e rollout LatAm). Encerrar reafirmando o compromisso da liderança de AS - MAPPS Brasil: Leandro Bruzzese, Gustavo Costa Berbert e Marcio Miguel."
        }},

        // Chart Data
        chart_time_labels: ["Definição da Regra", "Codificação JSON", "Homologação & Teste", "Deploy em Produção", "Ciclo Total"],
        chart_time_leg_before: "Legado Manual (MongoDB Raw)",
        chart_time_leg_after: "Cockpit ACDC + IA",
        chart_time_unit: "dias",
        chart_error_labels: ["Mês 1 (Pré-ACDC)", "Mês 2", "Mês 3 (Piloto)", "Mês 4 (Rollout)", "Mês 5 (Produção)", "Mês 6 (Estabilizado)"],
        chart_error_leg_err: "Erros de Sintaxe / Injeção Quebrada",
        chart_error_leg_val: "Validações Automatizadas por IA & Diff",
        chart_error_unit: "ocorrências"
      }}
    }};
    // Alias PTB and PT for full interoperability
    i18nData.ptb = i18nData.pt;
    i18nData.pt = i18nData.ptb;

    let currentLang = "es"; // Default Spanish
    let currentSlide = 1;
    const totalSlides = 10;
    let chartTime = null;
    let chartError = null;

    // DOM Elements
    const slideContainers = document.querySelectorAll('.slide-container');
    const slideNumDisplay = document.getElementById('slideNumDisplay');
    const progressFill = document.getElementById('progress-fill');
    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');
    const btnTheme = document.getElementById('btnTheme');
    const btnFullscreen = document.getElementById('btnFullscreen');
    const btnNotes = document.getElementById('btnNotes');
    const presenterBar = document.getElementById('presenterBar');
    const presenterHeader = document.getElementById('presenterHeader');
    const notesContent = document.getElementById('notesContent');
    const notesSlideNum = document.getElementById('notesSlideNum');
    const btnDrawer = document.getElementById('btnDrawer');
    const btnCloseDrawer = document.getElementById('btnCloseDrawer');
    const slideDrawerModal = document.getElementById('slideDrawerModal');
    const drawerList = document.getElementById('drawerList');

    // Build Drawer List for Active Language
    
    // Calculation Memory Modal Logic
    const calcModal = document.getElementById('calcMemoryModal');

    function openCalcModal(tabIndex = 1) {{
      if (calcModal) {{
        calcModal.classList.add('open');
        switchCalcTab(tabIndex);
      }}
    }}

    function closeCalcModal() {{
      if (calcModal) {{
        calcModal.classList.remove('open');
      }}
    }}

    function switchCalcTab(tabIndex) {{
      for (let i = 1; i <= 4; i++) {{
        const btn = document.getElementById(`tabBtn${{i}}`);
        const content = document.getElementById(`calcTab${{i}}`);
        if (btn) {{
          if (i === tabIndex) btn.classList.add('active');
          else btn.classList.remove('active');
        }}
        if (content) {{
          content.style.display = (i === tabIndex) ? 'block' : 'none';
        }}
      }}
    }}

    if (calcModal) {{
      calcModal.addEventListener('click', (e) => {{
        if (e.target === calcModal) closeCalcModal();
      }});
    }}

    function renderDrawerList() {{
      drawerList.innerHTML = '';
      const titles = i18nData[currentLang].drawer_titles;
      titles.forEach((title, idx) => {{
        const item = document.createElement('div');
        item.className = `drawer-item ${{idx + 1 === currentSlide ? 'active' : ''}}`;
        item.innerHTML = `
          <span class="drawer-num">${{String(idx + 1).padStart(2, '0')}}</span>
          <span class="drawer-label">${{title}}</span>
        `;
        item.addEventListener('click', () => {{
          updateSlide(idx + 1);
          slideDrawerModal.classList.remove('open');
        }});
        drawerList.appendChild(item);
      }});
    }}

    btnDrawer.addEventListener('click', () => {{
      const items = drawerList.querySelectorAll('.drawer-item');
      items.forEach((it, i) => {{
        it.classList.toggle('active', i + 1 === currentSlide);
      }});
      slideDrawerModal.classList.add('open');
    }});

    btnCloseDrawer.addEventListener('click', () => {{
      slideDrawerModal.classList.remove('open');
    }});

    slideDrawerModal.addEventListener('click', (e) => {{
      if (e.target === slideDrawerModal) {{
        slideDrawerModal.classList.remove('open');
      }}
    }});

    // Update Slide Logic
    function updateSlide(targetIndex) {{
      if (targetIndex < 1 || targetIndex > totalSlides) return;
      currentSlide = targetIndex;

      slideContainers.forEach(container => {{
        const slideIndex = parseInt(container.getAttribute('data-slide'));
        if (slideIndex === currentSlide) {{
          container.classList.add('active');
        }} else {{
          container.classList.remove('active');
        }}
      }});

      slideNumDisplay.textContent = `${{String(currentSlide).padStart(2, '0')}} / ${{String(totalSlides).padStart(2, '0')}}`;
      progressFill.style.width = `${{(currentSlide / totalSlides) * 100}}%`;

      btnPrev.disabled = (currentSlide === 1);
      btnNext.disabled = (currentSlide === totalSlides);

      // Update Notes for current language
      notesContent.innerHTML = i18nData[currentLang].notes[currentSlide] || "No notes for this slide.";
      notesSlideNum.textContent = String(currentSlide).padStart(2, '0');

      // Resize charts if entering slide 9
      if (currentSlide === 9) {{
        setTimeout(() => {{
          if (chartTime) chartTime.resize();
          if (chartError) chartError.resize();
        }}, 100);
      }}

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Navigation Listeners
    btnPrev.addEventListener('click', () => updateSlide(currentSlide - 1));
    btnNext.addEventListener('click', () => updateSlide(currentSlide + 1));

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        updateSlide(currentSlide + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        updateSlide(currentSlide - 1);
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        updateSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        updateSlide(totalSlides);
      }} else if (e.key.toLowerCase() === 'n') {{
        toggleNotes();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }} else if (e.key.toLowerCase() === 't') {{
        toggleTheme();
      }}
    }});

    // Toggle Notes
    function toggleNotes() {{
      presenterBar.classList.toggle('open');
    }}
    presenterHeader.addEventListener('click', toggleNotes);
    btnNotes.addEventListener('click', toggleNotes);

    // Toggle Fullscreen
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        document.exitFullscreen().catch(err => console.log(err));
      }}
    }}
    btnFullscreen.addEventListener('click', toggleFullscreen);

    // Theme Toggle
    function toggleTheme() {{
      const current = document.body.getAttribute('data-theme');
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      document.body.setAttribute('data-theme', nextTheme);
      updateChartsTheme(nextTheme);
    }}
    btnTheme.addEventListener('click', toggleTheme);

    // ── LANGUAGE SWITCHER LOGIC ───────────────────────────────────────────
    function setLanguage(lang) {{
      if (lang === 'pt') lang = 'ptb';
      if (!i18nData[lang]) return;
      currentLang = lang;
      document.documentElement.lang = (lang === 'ptb' || lang === 'pt') ? 'pt-BR' : lang;

      // Update active button state
      document.querySelectorAll('.lang-btn').forEach(btn => {{
        const bLang = btn.getAttribute('data-lang');
        const isActive = bLang === lang || ((lang === 'ptb' || lang === 'pt') && (bLang === 'ptb' || bLang === 'pt'));
        btn.classList.toggle('active', isActive);
      }});

      // Update page title
      document.getElementById('docTitle').textContent = i18nData[lang].doc_title;

      // Translate all data-i18n elements
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (i18nData[lang][key]) {{
          el.innerHTML = i18nData[lang][key];
        }}
      }});

      // Re-render drawer list & active notes
      renderDrawerList();
      notesContent.innerHTML = i18nData[lang].notes[currentSlide] || "No notes.";

      // Update charts
      updateChartsLanguage(lang);

      try {{
        localStorage.setItem('acdc_lang', lang);
      }} catch (e) {{}}
    }}

    // Chart.js Setup
    function initCharts() {{
      const ctxTime = document.getElementById('chartTimeToMarket');
      if (ctxTime) {{
        chartTime = new Chart(ctxTime, {{
          type: 'bar',
          data: {{
            labels: i18nData[currentLang].chart_time_labels,
            datasets: [
              {{
                label: i18nData[currentLang].chart_time_leg_before,
                data: [3, 4, 5, 2, 14],
                backgroundColor: 'rgba(211, 16, 39, 0.45)',
                borderColor: '#d31027',
                borderWidth: 1.5,
                borderRadius: 6
              }},
              {{
                label: i18nData[currentLang].chart_time_leg_after,
                data: [0.5, 0.3, 0.4, 0.1, 1.3],
                backgroundColor: 'rgba(0, 192, 243, 0.75)',
                borderColor: '#00c0f3',
                borderWidth: 1.5,
                borderRadius: 6
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{ labels: {{ color: '#94a3b8', font: {{ size: 11, family: 'Inter' }} }} }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}} ${{i18nData[currentLang].chart_time_unit}}`
                }}
              }}
            }},
            scales: {{
              x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 11 }} }}, grid: {{ display: false }} }},
              y: {{
                ticks: {{ color: '#94a3b8', callback: val => val + ' ' + i18nData[currentLang].chart_time_unit }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }}
            }}
          }}
        }});
      }}

      const ctxError = document.getElementById('chartErrorRate');
      if (ctxError) {{
        chartError = new Chart(ctxError, {{
          type: 'line',
          data: {{
            labels: i18nData[currentLang].chart_error_labels,
            datasets: [
              {{
                label: i18nData[currentLang].chart_error_leg_err,
                data: [42, 38, 14, 5, 2, 0],
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.12)',
                borderWidth: 2.5,
                fill: true,
                tension: 0.3
              }},
              {{
                label: i18nData[currentLang].chart_error_leg_val,
                data: [0, 5, 48, 112, 178, 230],
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.08)',
                borderWidth: 2,
                borderDash: [5, 5],
                tension: 0.3
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{ labels: {{ color: '#94a3b8', font: {{ size: 11, family: 'Inter' }} }} }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}} ${{i18nData[currentLang].chart_error_unit}}`
                }}
              }}
            }},
            scales: {{
              x: {{ ticks: {{ color: '#94a3b8', font: {{ size: 11 }} }}, grid: {{ display: false }} }},
              y: {{
                ticks: {{ color: '#94a3b8' }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }}
            }}
          }}
        }});
      }}
    }}

    function updateChartsLanguage(lang) {{
      if (chartTime) {{
        chartTime.data.labels = i18nData[lang].chart_time_labels;
        chartTime.data.datasets[0].label = i18nData[lang].chart_time_leg_before;
        chartTime.data.datasets[1].label = i18nData[lang].chart_time_leg_after;
        chartTime.update();
      }}
      if (chartError) {{
        chartError.data.labels = i18nData[lang].chart_error_labels;
        chartError.data.datasets[0].label = i18nData[lang].chart_error_leg_err;
        chartError.data.datasets[1].label = i18nData[lang].chart_error_leg_val;
        chartError.update();
      }}
    }}

    function updateChartsTheme(theme) {{
      const textColor = theme === 'dark' ? '#94a3b8' : '#475569';
      const gridColor = theme === 'dark' ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.06)';

      [chartTime, chartError].forEach(c => {{
        if (!c) return;
        c.options.plugins.legend.labels.color = textColor;
        if (c.options.scales.x) {{
          c.options.scales.x.ticks.color = textColor;
        }}
        if (c.options.scales.y) {{
          c.options.scales.y.ticks.color = textColor;
          c.options.scales.y.grid.color = gridColor;
        }}
        c.update();
      }});
    }}

    // Init on load
    window.addEventListener('DOMContentLoaded', () => {{
      initCharts();
      renderDrawerList();
      
      // Check saved language or default to Spanish (es)
      let savedLang = 'es';
      try {{
        savedLang = localStorage.getItem('acdc_lang') || 'es';
      }} catch (e) {{}}
      if (savedLang === 'pt') savedLang = 'ptb';
      setLanguage(savedLang);
      
      updateSlide(1);
    }});
  </script>
</body>
</html>
"""

# Write to both target files
target1 = "/Users/gcostabe/dev/ACDC/Apresentacao_Executiva_ACDC_MAPFRE.html"
with open(target1, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Written to {target1} ({len(html_content)} bytes)")

target2 = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_ACDC_MAPFRE.html"
with open(target2, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Written to {target2} ({len(html_content)} bytes)")

target3 = "/Users/gcostabe/Desktop/PRODUTO ACDC DESKTOP/index.html"
with open(target3, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"SUCCESS: Written to {target3} ({len(html_content)} bytes)")

