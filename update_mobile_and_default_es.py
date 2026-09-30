#!/usr/bin/env python3
"""
update_mobile_and_default_es.py
Implements:
1. Mobile suspended menu (menu suspenso) containing:
   - Botões de escolha (Language switcher: ES, EN, PTB)
   - Navegador (Slide navigation: Prev, Counter, Next, Quick Pills 1..10)
2. Mobile lateral menu (menu lateral / drawer) containing "o resto":
   - Notas do Apresentador
   - Memoria de Cálculo (AXET)
   - Alternar Tema (Modo Escuro / Claro)
   - Tela Cheia (Pantalla Completa)
   - Índice de Diapositivas (list of slides 1..10)
3. Spanish ('es') default language strictly enforced on fresh load for both presentations.
4. Mobile layout & table responsiveness improvements.
"""

import os
import re

def update_axet_presentation(filepath):
    print(f"Updating AXET at: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. CSS Injection before </style>
    mobile_css = """
    /* ==========================================================================
       MOBILE RESPONSIVE NAVIGATION: SUSPENDED MENU & LATERAL DRAWER
       ========================================================================== */
    .mobile-nav-triggers {
      display: none;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }

    .mobile-dropdown-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-size: 0.825rem;
      font-weight: 700;
      color: var(--ntt-cyan) !important;
      border: 1px solid rgba(56, 189, 248, 0.45) !important;
      background: rgba(56, 189, 248, 0.12) !important;
      border-radius: 8px;
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
    }

    .mobile-dropdown-btn:hover {
      background: rgba(56, 189, 248, 0.22) !important;
      border-color: var(--ntt-cyan) !important;
    }

    .mobile-dropdown-arrow {
      font-size: 0.72rem;
      transition: transform 0.25s ease;
      display: inline-block;
    }

    .mobile-dropdown-btn.open .mobile-dropdown-arrow {
      transform: rotate(180deg);
    }

    .mobile-menu-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 11px;
      font-size: 1.15rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-main);
      cursor: pointer;
      transition: var(--transition);
    }

    .mobile-menu-btn:hover {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    /* Menu Suspenso (Dropdown Panel) */
    .mobile-suspended-menu {
      position: fixed;
      top: 68px;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 1060;
      pointer-events: none;
      visibility: hidden;
      transition: visibility 0.25s ease;
    }

    .mobile-suspended-menu.open {
      pointer-events: auto;
      visibility: visible;
    }

    .suspended-menu-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(5px);
      -webkit-backdrop-filter: blur(5px);
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .mobile-suspended-menu.open .suspended-menu-backdrop {
      opacity: 1;
    }

    .suspended-menu-panel {
      position: relative;
      width: 100%;
      max-width: 480px;
      margin: 0 auto;
      background: var(--bg-surface);
      border-bottom: 2px solid var(--border-highlight);
      border-left: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-radius: 0 0 16px 16px;
      box-shadow: 0 24px 50px rgba(0, 0, 0, 0.7);
      padding: 1.25rem 1.25rem 1.5rem;
      transform: translateY(-24px);
      opacity: 0;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
    }

    .mobile-suspended-menu.open .suspended-menu-panel {
      transform: translateY(0);
      opacity: 1;
    }

    .suspended-section-label {
      font-family: 'Outfit', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--ntt-cyan);
      margin-bottom: 0.5rem;
    }

    .suspended-lang-switcher {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }

    .suspended-lang-btn {
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 6px;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2px;
      transition: var(--transition);
    }

    .suspended-lang-btn span {
      font-weight: 800;
      font-size: 0.88rem;
    }

    .suspended-lang-btn small {
      font-size: 0.7rem;
      color: var(--text-muted);
    }

    .suspended-lang-btn:hover, .suspended-lang-btn.active {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
      color: #fff;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
    }

    .suspended-lang-btn.active span {
      color: var(--ntt-cyan);
    }

    .suspended-nav-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .suspended-nav-btn {
      flex: 1;
      justify-content: center;
      padding: 9px 12px;
      font-size: 0.84rem;
      font-weight: 600;
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      transition: var(--transition);
    }

    .suspended-nav-btn:hover:not(:disabled) {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    .suspended-nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .suspended-counter {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 0.95rem;
      color: var(--ntt-cyan);
      padding: 6px 14px;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 8px;
      border: 1px solid var(--border-color);
      white-space: nowrap;
    }

    .suspended-pills-row {
      display: flex;
      gap: 6px;
      margin-top: 0.75rem;
      justify-content: center;
      flex-wrap: wrap;
    }

    .quick-pill {
      width: 34px;
      height: 34px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.82rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }

    .quick-pill:hover, .quick-pill.active {
      background: var(--ntt-blue-light);
      border-color: var(--ntt-cyan);
      color: #fff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }

    /* Lateral Drawer Mobile Actions */
    .drawer-actions-mobile {
      display: none;
      flex-direction: column;
      gap: 8px;
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
      background: rgba(0, 0, 0, 0.15);
    }

    .drawer-action-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-main);
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      text-align: left;
      width: 100%;
    }

    .drawer-action-btn:hover {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    .drawer-action-btn .action-icon {
      font-size: 1.05rem;
      min-width: 22px;
      text-align: center;
    }

    .drawer-list-heading {
      padding: 0.9rem 1.25rem 0.35rem;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }

    .drawer-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(4px);
      -webkit-backdrop-filter: blur(4px);
      z-index: 1040;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .drawer-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    /* Mobile media query overrides */
    @media (max-width: 900px) {
      .topbar {
        padding: 0 12px !important;
        justify-content: space-between;
      }
      .brand-group {
        gap: 8px !important;
      }
      .brand-logos-capsule {
        display: none !important;
      }
      .brand-tag {
        display: none !important;
      }
      .brand-subtitle {
        display: none !important;
      }
      .brand-name {
        font-size: 1rem !important;
      }
      .nav-actions {
        display: none !important;
      }
      .mobile-nav-triggers {
        display: flex !important;
      }
      .drawer-actions-mobile {
        display: flex !important;
      }
      .slide-drawer-modal {
        width: 86% !important;
        max-width: 350px !important;
      }
      .slide-container {
        padding: 20px 16px 120px 16px !important;
      }
      .slide-title {
        font-size: 1.9rem !important;
        line-height: 1.2 !important;
      }
      .slide-subtitle {
        font-size: 0.95rem !important;
      }
      .compare-table-wrap {
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
      }
      .compare-table {
        min-width: 600px !important;
      }
    }
    """

    if "/* ==========================================================================\n       MOBILE RESPONSIVE NAVIGATION" not in html:
        html = html.replace("</style>", mobile_css + "\n  </style>", 1)

    # 2. Add Mobile triggers to <header class="topbar">
    mobile_triggers = """      <!-- Mobile Nav Triggers (visible on mobile / tablet <= 900px) -->
      <div class="mobile-nav-triggers">
        <button class="btn-nav mobile-dropdown-btn" id="btnMobileDropdown" title="Navegador e Idioma" aria-expanded="false" aria-controls="mobileSuspendedMenu">
          <span id="mobileSlideNumDisplay">01 / 10</span>
          <span class="mobile-dropdown-arrow" id="mobileDropdownArrow">▾</span>
        </button>
        <button class="btn-nav mobile-menu-btn" id="btnMobileDrawer" title="Menú lateral" aria-label="Menú lateral">
          <span>☰</span>
        </button>
      </div>"""

    if 'id="btnMobileDropdown"' not in html:
        html = html.replace("</header>", mobile_triggers + "\n  </header>", 1)

    # 3. Add Mobile Suspended Menu & Drawer Backdrop after </header>
    suspended_menu_html = """
  <!-- Menu Suspenso (Dropdown for Navigator & Language Selector) -->
  <div class="mobile-suspended-menu" id="mobileSuspendedMenu">
    <div class="suspended-menu-backdrop" id="suspendedMenuBackdrop"></div>
    <div class="suspended-menu-panel">
      <!-- Section 1: Botões de Escolha (Idioma) -->
      <div class="suspended-section">
        <div class="suspended-section-label" data-i18n="menu_lang_label">Idioma (Elección)</div>
        <div class="suspended-lang-switcher" role="group" aria-label="Selector de idioma">
          <button class="suspended-lang-btn active" data-lang="es" onclick="setLanguage('es')">
            <span>ES</span><small>Español</small>
          </button>
          <button class="suspended-lang-btn" data-lang="en" onclick="setLanguage('en')">
            <span>EN</span><small>English</small>
          </button>
          <button class="suspended-lang-btn" data-lang="ptb" onclick="setLanguage('ptb')">
            <span>PTB</span><small>Português</small>
          </button>
        </div>
      </div>

      <!-- Section 2: Navegador de Diapositivas -->
      <div class="suspended-section">
        <div class="suspended-section-label" data-i18n="menu_nav_label">Navegador de Diapositivas</div>
        <div class="suspended-nav-row">
          <button class="suspended-nav-btn" id="btnSuspendedPrev">
            <span data-i18n="nav_prev">◀ Anterior</span>
          </button>
          <div class="suspended-counter" id="suspendedSlideCounter">01 / 10</div>
          <button class="suspended-nav-btn" id="btnSuspendedNext">
            <span data-i18n="nav_next">Siguiente ▶</span>
          </button>
        </div>
        <!-- Direct Quick Jump Pills -->
        <div class="suspended-pills-row" id="suspendedQuickPills"></div>
      </div>
    </div>
  </div>

  <!-- Lateral Drawer Backdrop -->
  <div class="drawer-backdrop" id="drawerBackdrop"></div>
"""

    if 'id="mobileSuspendedMenu"' not in html:
        html = html.replace("</header>", "</header>\n" + suspended_menu_html, 1)

    # 4. Enhance Slide Drawer Modal with Mobile Actions ("o resto")
    drawer_mobile_actions = """    <!-- Mobile Action Buttons ("O resto" no menu lateral) -->
    <div class="drawer-actions-mobile">
      <button class="drawer-action-btn" id="btnDrawerNotes">
        <span class="action-icon">🎙️</span>
        <span data-i18n="btn_notes">Notas del Orador</span>
      </button>
      <button class="drawer-action-btn" id="btnDrawerCalc" onclick="openCalcModal(1); closeDrawer();">
        <span class="action-icon">🧮</span>
        <span data-i18n="s9_calc_btn">Memoria de Cálculo</span>
      </button>
      <button class="drawer-action-btn" id="btnDrawerTheme">
        <span class="action-icon">🌓</span>
        <span data-i18n="btn_theme">Alternar Tema</span>
      </button>
      <button class="drawer-action-btn" id="btnDrawerFullscreen">
        <span class="action-icon">⛶</span>
        <span data-i18n="nav_fullscreen">Pantalla Completa</span>
      </button>
    </div>
    <div class="drawer-list-heading" data-i18n="drawer_slides_heading">Diapositivas</div>"""

    if 'class="drawer-actions-mobile"' not in html:
        target_str = '<div class="drawer-list" id="drawerList"></div>'
        html = html.replace(target_str, drawer_mobile_actions + "\n    " + target_str, 1)

    # 5. Add translations to i18nData
    if '"menu_lang_label":' not in html:
        html = html.replace(
            '"btn_drawer": "Índice",',
            '"btn_drawer": "Índice",\n       "menu_lang_label": "Idioma (Elección)",\n       "menu_nav_label": "Navegador de Diapositivas",\n       "drawer_slides_heading": "Índice de Diapositivas",\n       "btn_theme": "Alternar Tema",\n       "nav_fullscreen": "Pantalla Completa",',
            1
        )
        html = html.replace(
            '"btn_drawer": "Index",',
            '"btn_drawer": "Index",\n       "menu_lang_label": "Language (Selection)",\n       "menu_nav_label": "Slide Navigator",\n       "drawer_slides_heading": "Slide Index",\n       "btn_theme": "Toggle Theme",\n       "nav_fullscreen": "Fullscreen",',
            1
        )
        html = html.replace(
            '"btn_drawer": "Índice",\n       "drawer_titles":',
            '"btn_drawer": "Índice",\n       "menu_lang_label": "Idioma (Escolha)",\n       "menu_nav_label": "Navegador de Slides",\n       "drawer_slides_heading": "Índice de Slides",\n       "btn_theme": "Alternar Tema",\n       "nav_fullscreen": "Tela Cheia",\n       "drawer_titles":',
            1
        )

    # 6. JavaScript bindings & default language
    js_mobile_logic = """
    // Mobile Suspended Menu & Lateral Drawer Elements
    const btnMobileDropdown = document.getElementById('btnMobileDropdown');
    const mobileSuspendedMenu = document.getElementById('mobileSuspendedMenu');
    const suspendedMenuBackdrop = document.getElementById('suspendedMenuBackdrop');
    const mobileSlideNumDisplay = document.getElementById('mobileSlideNumDisplay');
    const suspendedSlideCounter = document.getElementById('suspendedSlideCounter');
    const btnSuspendedPrev = document.getElementById('btnSuspendedPrev');
    const btnSuspendedNext = document.getElementById('btnSuspendedNext');
    const suspendedQuickPills = document.getElementById('suspendedQuickPills');
    const btnMobileDrawer = document.getElementById('btnMobileDrawer');
    const drawerBackdrop = document.getElementById('drawerBackdrop');
    const btnDrawerNotes = document.getElementById('btnDrawerNotes');
    const btnDrawerTheme = document.getElementById('btnDrawerTheme');
    const btnDrawerFullscreen = document.getElementById('btnDrawerFullscreen');

    function toggleSuspendedMenu(show) {
      const isOpen = show !== undefined ? show : !mobileSuspendedMenu.classList.contains('open');
      mobileSuspendedMenu.classList.toggle('open', isOpen);
      btnMobileDropdown.classList.toggle('open', isOpen);
      btnMobileDropdown.setAttribute('aria-expanded', isOpen);
    }

    function openDrawer() {
      renderDrawerList();
      slideDrawerModal.classList.add('open');
      if (drawerBackdrop) drawerBackdrop.classList.add('open');
      toggleSuspendedMenu(false);
    }

    function closeDrawer() {
      slideDrawerModal.classList.remove('open');
      if (drawerBackdrop) drawerBackdrop.classList.remove('open');
    }

    if (btnMobileDropdown) {
      btnMobileDropdown.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleSuspendedMenu();
      });
    }

    if (suspendedMenuBackdrop) {
      suspendedMenuBackdrop.addEventListener('click', () => toggleSuspendedMenu(false));
    }

    if (btnMobileDrawer) {
      btnMobileDrawer.addEventListener('click', (e) => {
        e.stopPropagation();
        openDrawer();
      });
    }

    if (btnDrawer) {
      btnDrawer.addEventListener('click', (e) => {
        e.stopPropagation();
        openDrawer();
      });
    }

    if (btnCloseDrawer) {
      btnCloseDrawer.addEventListener('click', closeDrawer);
    }

    if (drawerBackdrop) {
      drawerBackdrop.addEventListener('click', closeDrawer);
    }

    if (btnSuspendedPrev) {
      btnSuspendedPrev.addEventListener('click', () => {
        updateSlide(currentSlide - 1);
      });
    }

    if (btnSuspendedNext) {
      btnSuspendedNext.addEventListener('click', () => {
        updateSlide(currentSlide + 1);
      });
    }

    if (btnDrawerNotes) {
      btnDrawerNotes.addEventListener('click', () => {
        toggleNotes();
        closeDrawer();
      });
    }

    if (btnDrawerTheme) {
      btnDrawerTheme.addEventListener('click', () => {
        toggleTheme();
      });
    }

    if (btnDrawerFullscreen) {
      btnDrawerFullscreen.addEventListener('click', () => {
        toggleFullscreen();
        closeDrawer();
      });
    }

    // Render Quick Pills in Suspended Menu
    function renderQuickPills() {
      if (!suspendedQuickPills) return;
      suspendedQuickPills.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const pill = document.createElement('button');
        pill.className = `quick-pill ${i === currentSlide ? 'active' : ''}`;
        pill.textContent = i;
        pill.title = `Diapositiva ${i}`;
        pill.addEventListener('click', () => {
          updateSlide(i);
          toggleSuspendedMenu(false);
        });
        suspendedQuickPills.appendChild(pill);
      }
    }
    """

    if "function toggleSuspendedMenu" not in html:
        target_fn = "function updateSlide(targetIndex) {"
        html = html.replace(target_fn, js_mobile_logic + "\n    " + target_fn, 1)

    # 7. Update updateSlide logic to sync mobile displays
    update_slide_repl = """      slideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (mobileSlideNumDisplay) mobileSlideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (suspendedSlideCounter) suspendedSlideCounter.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (btnSuspendedPrev) btnSuspendedPrev.disabled = (currentSlide === 1);
      if (btnSuspendedNext) btnSuspendedNext.disabled = (currentSlide === totalSlides);
      
      // Update quick pills in mobile suspended menu
      if (suspendedQuickPills) {
        const pills = suspendedQuickPills.querySelectorAll('.quick-pill');
        pills.forEach((p, idx) => p.classList.toggle('active', idx + 1 === currentSlide));
      }"""

    if "mobileSlideNumDisplay" not in html:
        html = html.replace(
            "slideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;",
            update_slide_repl,
            1
        )

    # 8. Update setLanguage to sync suspended language buttons
    sync_lang_btns = """      // Update active state in both desktop and mobile switchers
      document.querySelectorAll('.lang-btn, .suspended-lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
      });"""

    if ".suspended-lang-btn" not in html:
        html = re.sub(
            r"document\.querySelectorAll\('\.lang-btn'\)\.forEach\(btn => \{\s+btn\.classList\.toggle\('active',\s*btn\.getAttribute\('data-lang'\)\s*===\s*lang\);\s+\}\);",
            sync_lang_btns,
            html
        )

    # 9. Strictly enforce Spanish ('es') default on load
    init_default_es = """      // Check saved language or default to Spanish (es)
      let savedLang = 'es';
      try {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('lang')) {
          savedLang = urlParams.get('lang');
        } else if (sessionStorage.getItem('axet_lang')) {
          savedLang = sessionStorage.getItem('axet_lang');
        } else {
          savedLang = 'es'; // Always default to Spanish
        }
      } catch (e) {
        savedLang = 'es';
      }
      if (savedLang === 'pt') savedLang = 'ptb';
      if (!i18nData[savedLang]) savedLang = 'es';
      setLanguage(savedLang);
      renderQuickPills();"""

    html = re.sub(
        r"// Check saved language or default to Spanish \(es\)\s+let savedLang = 'es';[\s\S]*?setLanguage\(savedLang\);[\s\S]*?renderQuickPills\(\);",
        init_default_es,
        html
    )

    # 10. Update static presenter notes header to Spanish default
    html = html.replace(
        "<span>🎙️</span> <span>NOTAS DO APRESENTADOR (SLIDE <span id=\"notesSlideNum\">01</span>)</span>",
        "<span>🎙️</span> <span>NOTAS DEL ORADOR (SLIDE <span id=\"notesSlideNum\">01</span>)</span>"
    )
    html = html.replace(
        "Clique ou pressione [N] para recolher",
        "Haga clic o presione [N] para contraer"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("AXET updated successfully.")


def update_acdc_presentation(filepath):
    print(f"Updating ACDC at: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. CSS Injection before </style>
    mobile_css = """
    /* ==========================================================================
       MOBILE RESPONSIVE NAVIGATION: SUSPENDED MENU & LATERAL DRAWER
       ========================================================================== */
    .mobile-nav-triggers {
      display: none;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }

    .mobile-dropdown-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      font-size: 0.825rem;
      font-weight: 700;
      color: var(--ntt-cyan) !important;
      border: 1px solid rgba(56, 189, 248, 0.45) !important;
      background: rgba(56, 189, 248, 0.12) !important;
      border-radius: 8px;
      cursor: pointer;
      white-space: nowrap;
      transition: var(--transition);
    }

    .mobile-dropdown-btn:hover {
      background: rgba(56, 189, 248, 0.22) !important;
      border-color: var(--ntt-cyan) !important;
    }

    .mobile-dropdown-arrow {
      font-size: 0.72rem;
      transition: transform 0.25s ease;
      display: inline-block;
    }

    .mobile-dropdown-btn.open .mobile-dropdown-arrow {
      transform: rotate(180deg);
    }

    .mobile-menu-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 11px;
      font-size: 1.15rem;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-main);
      cursor: pointer;
      transition: var(--transition);
    }

    .mobile-menu-btn:hover {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    /* Menu Suspenso (Dropdown Panel) */
    .mobile-suspended-menu {
      position: fixed;
      top: 68px;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 1060;
      pointer-events: none;
      visibility: hidden;
      transition: visibility 0.25s ease;
    }

    .mobile-suspended-menu.open {
      pointer-events: auto;
      visibility: visible;
    }

    .suspended-menu-backdrop {
      position: absolute;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(5px);
      -webkit-backdrop-filter: blur(5px);
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .mobile-suspended-menu.open .suspended-menu-backdrop {
      opacity: 1;
    }

    .suspended-menu-panel {
      position: relative;
      width: 100%;
      max-width: 480px;
      margin: 0 auto;
      background: var(--bg-surface);
      border-bottom: 2px solid var(--border-highlight);
      border-left: 1px solid var(--border-color);
      border-right: 1px solid var(--border-color);
      border-radius: 0 0 16px 16px;
      box-shadow: 0 24px 50px rgba(0, 0, 0, 0.7);
      padding: 1.25rem 1.25rem 1.5rem;
      transform: translateY(-24px);
      opacity: 0;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
    }

    .mobile-suspended-menu.open .suspended-menu-panel {
      transform: translateY(0);
      opacity: 1;
    }

    .suspended-section-label {
      font-family: 'Outfit', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--ntt-cyan);
      margin-bottom: 0.5rem;
    }

    .suspended-lang-switcher {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }

    .suspended-lang-btn {
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 6px;
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2px;
      transition: var(--transition);
    }

    .suspended-lang-btn span {
      font-weight: 800;
      font-size: 0.88rem;
    }

    .suspended-lang-btn small {
      font-size: 0.7rem;
      color: var(--text-muted);
    }

    .suspended-lang-btn:hover, .suspended-lang-btn.active {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
      color: #fff;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
    }

    .suspended-lang-btn.active span {
      color: var(--ntt-cyan);
    }

    .suspended-nav-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }

    .suspended-nav-btn {
      flex: 1;
      justify-content: center;
      padding: 9px 12px;
      font-size: 0.84rem;
      font-weight: 600;
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      transition: var(--transition);
    }

    .suspended-nav-btn:hover:not(:disabled) {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    .suspended-nav-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .suspended-counter {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 0.95rem;
      color: var(--ntt-cyan);
      padding: 6px 14px;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 8px;
      border: 1px solid var(--border-color);
      white-space: nowrap;
    }

    .suspended-pills-row {
      display: flex;
      gap: 6px;
      margin-top: 0.75rem;
      justify-content: center;
      flex-wrap: wrap;
    }

    .quick-pill {
      width: 34px;
      height: 34px;
      border-radius: 6px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-muted);
      font-weight: 700;
      font-size: 0.82rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }

    .quick-pill:hover, .quick-pill.active {
      background: var(--ntt-blue-light);
      border-color: var(--ntt-cyan);
      color: #fff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }

    /* Lateral Drawer Mobile Actions */
    .drawer-actions-mobile {
      display: none;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 1.25rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-color);
    }

    .drawer-action-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 9px 12px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-glass);
      color: var(--text-main);
      font-size: 0.86rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      text-align: left;
      width: 100%;
    }

    .drawer-action-btn:hover {
      background: var(--border-highlight);
      border-color: var(--ntt-cyan);
    }

    .drawer-action-btn .action-icon {
      font-size: 1.05rem;
      min-width: 22px;
      text-align: center;
    }

    .drawer-list-heading {
      padding: 0 0 0.5rem 0;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }

    /* Mobile media query overrides for ACDC */
    @media (max-width: 900px) {
      .topbar {
        padding: 0 12px !important;
        justify-content: space-between;
      }
      .brand-group {
        gap: 8px !important;
      }
      .brand-logos-capsule {
        display: none !important;
      }
      .brand-title-divider {
        display: none !important;
      }
      .brand-title-tag {
        display: none !important;
      }
      .brand-subtitle-line {
        display: none !important;
      }
      .brand-title-main {
        font-size: 1rem !important;
      }
      .nav-actions {
        display: none !important;
      }
      .mobile-nav-triggers {
        display: flex !important;
      }
      .drawer-actions-mobile {
        display: flex !important;
      }
      .slide-drawer-panel {
        width: 86% !important;
        max-width: 350px !important;
      }
      .slide-container {
        padding: 20px 16px 120px 16px !important;
      }
      .slide-title {
        font-size: 1.9rem !important;
        line-height: 1.2 !important;
      }
    }
    """

    if "/* ==========================================================================\n       MOBILE RESPONSIVE NAVIGATION" not in html:
        html = html.replace("</style>", mobile_css + "\n  </style>", 1)

    # 2. Add Mobile triggers to <header class="topbar">
    mobile_triggers = """      <!-- Mobile Nav Triggers (visible on mobile / tablet <= 900px) -->
      <div class="mobile-nav-triggers">
        <button class="btn-nav mobile-dropdown-btn" id="btnMobileDropdown" title="Navegador e Idioma" aria-expanded="false" aria-controls="mobileSuspendedMenu">
          <span id="mobileSlideNumDisplay">01 / 10</span>
          <span class="mobile-dropdown-arrow" id="mobileDropdownArrow">▾</span>
        </button>
        <button class="btn-nav mobile-menu-btn" id="btnMobileDrawer" title="Menú lateral" aria-label="Menú lateral">
          <span>☰</span>
        </button>
      </div>"""

    if 'id="btnMobileDropdown"' not in html:
        html = html.replace("</header>", mobile_triggers + "\n  </header>", 1)

    # 3. Add Mobile Suspended Menu after </header>
    suspended_menu_html = """
  <!-- Menu Suspenso (Dropdown for Navigator & Language Selector) -->
  <div class="mobile-suspended-menu" id="mobileSuspendedMenu">
    <div class="suspended-menu-backdrop" id="suspendedMenuBackdrop"></div>
    <div class="suspended-menu-panel">
      <!-- Section 1: Botões de Escolha (Idioma) -->
      <div class="suspended-section">
        <div class="suspended-section-label" data-i18n="menu_lang_label">Idioma (Elección)</div>
        <div class="suspended-lang-switcher" role="group" aria-label="Selector de idioma">
          <button class="suspended-lang-btn active" data-lang="es" onclick="setLanguage('es')">
            <span>ES</span><small>Español</small>
          </button>
          <button class="suspended-lang-btn" data-lang="en" onclick="setLanguage('en')">
            <span>EN</span><small>English</small>
          </button>
          <button class="suspended-lang-btn" data-lang="ptb" onclick="setLanguage('ptb')">
            <span>PTB</span><small>Português</small>
          </button>
        </div>
      </div>

      <!-- Section 2: Navegador de Diapositivas -->
      <div class="suspended-section">
        <div class="suspended-section-label" data-i18n="menu_nav_label">Navegador de Diapositivas</div>
        <div class="suspended-nav-row">
          <button class="suspended-nav-btn" id="btnSuspendedPrev">
            <span data-i18n="nav_prev">◀ Anterior</span>
          </button>
          <div class="suspended-counter" id="suspendedSlideCounter">01 / 10</div>
          <button class="suspended-nav-btn" id="btnSuspendedNext">
            <span data-i18n="nav_next">Siguiente ▶</span>
          </button>
        </div>
        <!-- Direct Quick Jump Pills -->
        <div class="suspended-pills-row" id="suspendedQuickPills"></div>
      </div>
    </div>
  </div>
"""

    if 'id="mobileSuspendedMenu"' not in html:
        html = html.replace("</header>", "</header>\n" + suspended_menu_html, 1)

    # 4. Enhance Slide Drawer Modal with Mobile Actions ("o resto")
    drawer_mobile_actions = """      <!-- Mobile Action Buttons ("O resto" no menu lateral) -->
      <div class="drawer-actions-mobile">
        <button class="drawer-action-btn" id="btnDrawerNotes">
          <span class="action-icon">🎙️</span>
          <span data-i18n="nav_notes">Notas del Orador</span>
        </button>
        <button class="drawer-action-btn" id="btnDrawerTheme">
          <span class="action-icon">☀️ / 🌙</span>
          <span data-i18n="btn_theme">Alternar Tema</span>
        </button>
        <button class="drawer-action-btn" id="btnDrawerFullscreen">
          <span class="action-icon">⛶</span>
          <span data-i18n="nav_fullscreen">Pantalla Completa</span>
        </button>
      </div>
      <div class="drawer-list-heading" data-i18n="drawer_heading">Diapositivas</div>"""

    if 'class="drawer-actions-mobile"' not in html:
        target_str = '<div id="drawerList"></div>'
        html = html.replace(target_str, drawer_mobile_actions + "\n      " + target_str, 1)

    # 5. Add translations to i18nData
    if '"menu_lang_label":' not in html:
        html = html.replace(
            '"drawer_heading": "Índice de Diapositivas",',
            '"drawer_heading": "Índice de Diapositivas",\n        "menu_lang_label": "Idioma (Elección)",\n        "menu_nav_label": "Navegador de Diapositivas",\n        "btn_theme": "Alternar Tema",',
            1
        )
        html = html.replace(
            '"drawer_heading": "Slide Index",',
            '"drawer_heading": "Slide Index",\n        "menu_lang_label": "Language (Selection)",\n        "menu_nav_label": "Slide Navigator",\n        "btn_theme": "Toggle Theme",',
            1
        )
        html = html.replace(
            '"drawer_heading": "Índice de Slides",',
            '"drawer_heading": "Índice de Slides",\n        "menu_lang_label": "Idioma (Escolha)",\n        "menu_nav_label": "Navegador de Slides",\n        "btn_theme": "Alternar Tema",',
            1
        )

    # 6. JavaScript bindings
    js_mobile_logic = """
    // Mobile Suspended Menu & Lateral Drawer Elements
    const btnMobileDropdown = document.getElementById('btnMobileDropdown');
    const mobileSuspendedMenu = document.getElementById('mobileSuspendedMenu');
    const suspendedMenuBackdrop = document.getElementById('suspendedMenuBackdrop');
    const mobileSlideNumDisplay = document.getElementById('mobileSlideNumDisplay');
    const suspendedSlideCounter = document.getElementById('suspendedSlideCounter');
    const btnSuspendedPrev = document.getElementById('btnSuspendedPrev');
    const btnSuspendedNext = document.getElementById('btnSuspendedNext');
    const suspendedQuickPills = document.getElementById('suspendedQuickPills');
    const btnMobileDrawer = document.getElementById('btnMobileDrawer');
    const btnDrawerNotes = document.getElementById('btnDrawerNotes');
    const btnDrawerTheme = document.getElementById('btnDrawerTheme');
    const btnDrawerFullscreen = document.getElementById('btnDrawerFullscreen');

    function toggleSuspendedMenu(show) {
      const isOpen = show !== undefined ? show : !mobileSuspendedMenu.classList.contains('open');
      mobileSuspendedMenu.classList.toggle('open', isOpen);
      btnMobileDropdown.classList.toggle('open', isOpen);
      btnMobileDropdown.setAttribute('aria-expanded', isOpen);
    }

    function openDrawer() {
      renderDrawerList();
      slideDrawerModal.classList.add('open');
      toggleSuspendedMenu(false);
    }

    function closeDrawer() {
      slideDrawerModal.classList.remove('open');
    }

    if (btnMobileDropdown) {
      btnMobileDropdown.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleSuspendedMenu();
      });
    }

    if (suspendedMenuBackdrop) {
      suspendedMenuBackdrop.addEventListener('click', () => toggleSuspendedMenu(false));
    }

    if (btnMobileDrawer) {
      btnMobileDrawer.addEventListener('click', (e) => {
        e.stopPropagation();
        openDrawer();
      });
    }

    if (btnSuspendedPrev) {
      btnSuspendedPrev.addEventListener('click', () => {
        updateSlide(currentSlide - 1);
      });
    }

    if (btnSuspendedNext) {
      btnSuspendedNext.addEventListener('click', () => {
        updateSlide(currentSlide + 1);
      });
    }

    if (btnDrawerNotes) {
      btnDrawerNotes.addEventListener('click', () => {
        toggleNotes();
        closeDrawer();
      });
    }

    if (btnDrawerTheme) {
      btnDrawerTheme.addEventListener('click', () => {
        toggleTheme();
      });
    }

    if (btnDrawerFullscreen) {
      btnDrawerFullscreen.addEventListener('click', () => {
        toggleFullscreen();
        closeDrawer();
      });
    }

    // Render Quick Pills in Suspended Menu
    function renderQuickPills() {
      if (!suspendedQuickPills) return;
      suspendedQuickPills.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const pill = document.createElement('button');
        pill.className = `quick-pill ${i === currentSlide ? 'active' : ''}`;
        pill.textContent = i;
        pill.title = `Diapositiva ${i}`;
        pill.addEventListener('click', () => {
          updateSlide(i);
          toggleSuspendedMenu(false);
        });
        suspendedQuickPills.appendChild(pill);
      }
    }
    """

    if "function toggleSuspendedMenu" not in html:
        target_fn = "function updateSlide(targetIndex) {"
        html = html.replace(target_fn, js_mobile_logic + "\n    " + target_fn, 1)

    # 7. Update updateSlide logic to sync mobile displays
    update_slide_repl = """      slideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (mobileSlideNumDisplay) mobileSlideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (suspendedSlideCounter) suspendedSlideCounter.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (btnSuspendedPrev) btnSuspendedPrev.disabled = (currentSlide === 1);
      if (btnSuspendedNext) btnSuspendedNext.disabled = (currentSlide === totalSlides);
      
      // Update quick pills in mobile suspended menu
      if (suspendedQuickPills) {
        const pills = suspendedQuickPills.querySelectorAll('.quick-pill');
        pills.forEach((p, idx) => p.classList.toggle('active', idx + 1 === currentSlide));
      }"""

    if "mobileSlideNumDisplay" not in html:
        html = html.replace(
            "slideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;",
            update_slide_repl,
            1
        )

    # 8. Update setLanguage to sync suspended language buttons
    sync_lang_btns = """      // Update active state in both desktop and mobile switchers
      document.querySelectorAll('.lang-btn, .suspended-lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
      });"""

    if ".suspended-lang-btn" not in html:
        html = re.sub(
            r"document\.querySelectorAll\('\.lang-btn'\)\.forEach\(btn => \{\s+btn\.classList\.toggle\('active',\s*btn\.getAttribute\('data-lang'\)\s*===\s*lang\);\s+\}\);",
            sync_lang_btns,
            html
        )

    # 9. Strictly enforce Spanish ('es') default on load
    init_default_es = """      // Check saved language or default to Spanish (es)
      let savedLang = 'es';
      try {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('lang')) {
          savedLang = urlParams.get('lang');
        } else if (sessionStorage.getItem('acdc_lang')) {
          savedLang = sessionStorage.getItem('acdc_lang');
        } else {
          savedLang = 'es'; // Always default to Spanish
        }
      } catch (e) {
        savedLang = 'es';
      }
      if (savedLang === 'pt') savedLang = 'ptb';
      if (!i18nData[savedLang]) savedLang = 'es';
      setLanguage(savedLang);
      renderQuickPills();"""

    html = re.sub(
        r"// Check saved language or default to Spanish \(es\)\s+let savedLang = 'es';[\s\S]*?setLanguage\(savedLang\);",
        init_default_es,
        html
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("ACDC updated successfully.")


if __name__ == "__main__":
    update_axet_presentation('/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_AXET_REEF.html')
    update_acdc_presentation('/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_ACDC_MAPFRE.html')
