#!/usr/bin/env python3
"""
fix_menu_navigation_sync.py
Fixes the synchronization inside updateSlide(targetIndex):
- Updates mobileSlideNumDisplay (e.g. '02 / 10')
- Updates suspendedSlideCounter (e.g. '02 / 10')
- Updates btnSuspendedPrev & btnSuspendedNext disabled state
- Updates suspendedQuickPills active class for current slide
- Updates drawerList items active class for current slide
- Adds touch swipe navigation for mobile
"""

import os
import re

def fix_presentation(filepath, name):
    print(f"Fixing navigation sync in {name} ({filepath})...")
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Target block inside updateSlide
    old_target = """      slideNumDisplay.textContent = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      progressFill.style.width = `${(currentSlide / totalSlides) * 100}%`;

      btnPrev.disabled = (currentSlide === 1);
      btnNext.disabled = (currentSlide === totalSlides);"""

    new_replacement = """      // Slide Counter Updates (Desktop and Mobile)
      const formattedNum = `${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      if (slideNumDisplay) slideNumDisplay.textContent = formattedNum;
      if (mobileSlideNumDisplay) mobileSlideNumDisplay.textContent = formattedNum;
      if (suspendedSlideCounter) suspendedSlideCounter.textContent = formattedNum;
      
      if (progressFill) progressFill.style.width = `${(currentSlide / totalSlides) * 100}%`;

      // Navigation Buttons Disabled State (Desktop & Mobile)
      if (btnPrev) btnPrev.disabled = (currentSlide === 1);
      if (btnNext) btnNext.disabled = (currentSlide === totalSlides);
      if (btnSuspendedPrev) btnSuspendedPrev.disabled = (currentSlide === 1);
      if (btnSuspendedNext) btnSuspendedNext.disabled = (currentSlide === totalSlides);

      // Mobile Suspended Menu Quick Pills (1..10)
      if (suspendedQuickPills) {
        const pills = suspendedQuickPills.querySelectorAll('.quick-pill');
        pills.forEach((p, idx) => {
          p.classList.toggle('active', (idx + 1) === currentSlide);
        });
      }

      // Lateral Drawer List Items (1..10)
      if (drawerList) {
        const drawerItems = drawerList.querySelectorAll('.drawer-item');
        drawerItems.forEach((it, i) => {
          it.classList.toggle('active', (i + 1) === currentSlide);
        });
      }"""

    if old_target in html:
        html = html.replace(old_target, new_replacement, 1)
        print("  -> Replaced updateSlide counters and pill/drawer sync.")
    else:
        print("  -> WARNING: old_target not matched exactly, checking regex...")
        # fallback regex replace
        pattern = re.compile(
            r"slideNumDisplay\.textContent = `\$\{String\(currentSlide\)\.padStart\(2, '0'\)\} / \$\{String\(totalSlides\)\.padStart\(2, '0'\)\}`;[\s\S]*?btnNext\.disabled = \(currentSlide === totalSlides\);",
            re.MULTILINE
        )
        html = pattern.sub(new_replacement, html, count=1)
        print("  -> Substituted via regex.")

    # Also add touch swipe support if not present
    touch_swipe_code = """
    // Touch swipe navigation for mobile
    let touchStartX = 0;
    let touchStartY = 0;
    document.addEventListener('touchstart', (e) => {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      if (!e.changedTouches || !e.changedTouches[0]) return;
      const touchEndX = e.changedTouches[0].screenX;
      const touchEndY = e.changedTouches[0].screenY;
      const dx = touchEndX - touchStartX;
      const dy = touchEndY - touchStartY;
      // Only trigger horizontal swipe if movement > 50px and predominantly horizontal
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        if (dx < 0) {
          updateSlide(currentSlide + 1); // Swipe left -> next slide
        } else {
          updateSlide(currentSlide - 1); // Swipe right -> prev slide
        }
      }
    }, { passive: true });
    """

    if "// Touch swipe navigation for mobile" not in html:
        target_listeners = "btnNext.addEventListener('click', () => updateSlide(currentSlide + 1));"
        html = html.replace(target_listeners, target_listeners + touch_swipe_code, 1)
        print("  -> Added touch swipe support.")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Finished fixing {name}.\n")

if __name__ == "__main__":
    fix_presentation("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_AXET_REEF.html", "AXET")
    fix_presentation("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_ACDC_MAPFRE.html", "ACDC")
