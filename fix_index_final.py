# -*- coding: utf-8 -*-
import re

filepath = r'd:\EJP Template\frontend\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# 1. HERO SECTION: restore text-white (dark bg with inline styles)
# ============================================================
hero_start = content.find('<section id="hero"')
about_start = content.find('<section id="about"')
if hero_start != -1 and about_start != -1:
    hero = content[hero_start:about_start]
    hero = hero.replace('text-text', 'text-white')
    content = content[:hero_start] + hero + content[about_start:]

# ============================================================
# 2. CTA SECTION: restore text-white (always on colored bg)
# ============================================================
cta_start = content.find('<section id="cta"')
footer_start = content.find('<footer')
if cta_start != -1 and footer_start != -1:
    cta = content[cta_start:footer_start]
    cta = cta.replace('text-text', 'text-white')
    content = content[:cta_start] + cta + content[footer_start:]

# ============================================================
# 3. Fix CTA gradient (marine color was removed from config)
# ============================================================
content = content.replace('bg-gradient-to-br from-surface to-gold/40', 
                           'bg-gradient-to-br from-[#1E3A5F] to-[#F5A623]/40')
content = content.replace('bg-surface', 'bg-bg dark:bg-black')
# Fix the one that says "bg-bg dark:bg-black border-t border-border"
content = content.replace('bg-bg dark:bg-black border-t border-border', 'bg-[#060E1A] dark:bg-black border-t border-border')

# ============================================================
# 4. Nav links: use text-white since nav is over hero initially
# ============================================================
# Already fixed by hero section fix above for desktop links inside hero
# Fix nav links outside hero
nav_start = content.find('<nav id="navbar"')
nav_end = content.find('</nav>') + len('</nav>')
if nav_start != -1 and nav_end != -1:
    nav = content[nav_start:nav_end]
    nav = nav.replace('text-text', 'text-white')
    content = content[:nav_start] + nav + content[nav_end:]

# Mobile menu
mob_start = content.find('<div id="mobile-menu"')
mob_end = content.find('</div>\n\n    <main>') 
if mob_start != -1 and mob_end != -1:
    mob = content[mob_start:mob_end]
    mob = mob.replace('text-text', 'text-white')
    content = content[:mob_start] + mob + content[mob_end:]

# ============================================================
# 5. Testimonials section: keep dark bg, white text
# ============================================================
test_start = content.find('<section id="temoignages"')
cta_start2 = content.find('<section id="cta"')
if test_start != -1 and cta_start2 != -1:
    test = content[test_start:cta_start2]
    # This section has inline dark star pattern bg, text must be white
    test = test.replace('text-text', 'text-white')
    content = content[:test_start] + test + content[cta_start2:]

# ============================================================
# 6. Parcours section: cards are on dark marine bg, text stays white
# ============================================================
parc_start = content.find('<section id="parcours"')
form_start = content.find('<section id="formations"')
if parc_start != -1 and form_start != -1:
    parc = content[parc_start:form_start]
    parc = parc.replace('text-text', 'text-white')
    # Fix bg-marine/60 which no longer exists
    parc = parc.replace('bg-marine/60', 'bg-[#1E3A5F]/60')
    content = content[:parc_start] + parc + content[form_start:]

# ============================================================
# 7. Events section: also had dark bg
# ============================================================
ev_start = content.find('<section id="evenements"')
test_start2 = content.find('<section id="temoignages"')
if ev_start != -1 and test_start2 != -1:
    ev = content[ev_start:test_start2]
    ev = ev.replace('text-text', 'text-white')
    content = content[:ev_start] + ev + content[test_start2:]

# ============================================================
# 8. Fix loader screen color
# ============================================================
content = content.replace(
    "background-color: var(--ejp-dark);",
    "background-color: #0A1628;"
)

# ============================================================
# 9. Fix body bg
# ============================================================
content = content.replace(
    "background-color: var(--color-bg);",
    "background-color: var(--color-bg);"
)

# ============================================================
# 10. Add marine color back to Tailwind config (needed for CTA)
# ============================================================
content = content.replace(
    "'gold-light': '#FFD580',",
    "'gold-light': '#FFD580',\n                        marine: '#1E3A5F',"
)

# ============================================================
# 11. Fix footer text colors (footer has dark bg always)
# ============================================================
footer_start2 = content.find('<footer')
footer_end = content.find('</footer>') + len('</footer>')
if footer_start2 != -1 and footer_end != -1:
    foot = content[footer_start2:footer_end]
    foot = foot.replace('text-text', 'text-white')
    content = content[:footer_start2] + foot + content[footer_end:]

# ============================================================
# 12. Ensure toggle script exists
# ============================================================
if 'function toggleTheme()' not in content:
    toggle = '''    <script>
        function toggleTheme() {
            document.documentElement.classList.toggle('dark');
            localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
        }
        if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    </script>
</head>'''
    content = content.replace('</head>', toggle)

# ============================================================
# 13. Ensure floating toggle button exists
# ============================================================
if 'Theme Toggle Floating Button' not in content:
    btn = '''
    <!-- Theme Toggle Floating Button -->
    <button onclick="toggleTheme()" class="fixed bottom-8 right-8 z-[10003] w-14 h-14 rounded-full bg-gold text-white shadow-2xl flex items-center justify-center text-xl hover:scale-110 transition-transform border border-gold/50">
        <i class="fas fa-moon dark:hidden"></i>
        <i class="fas fa-sun hidden dark:block"></i>
    </button>
</body>'''
    content = content.replace('</body>', btn)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("All fixes applied successfully!")
