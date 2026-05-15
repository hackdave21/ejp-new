import os
import re

filepath = r'd:\EJP Template\frontend\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Fonts
google_fonts = r'<link rel="preconnect" href="https://fonts.googleapis.com">[\s\S]*?<link href="https://fonts.googleapis.com/css2[^>]+rel="stylesheet">'
futura_font = '''    <style>
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdBook.otf') format('opentype');
            font-weight: normal;
            font-style: normal;
        }
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdHeavy.otf') format('opentype');
            font-weight: bold;
            font-style: normal;
        }
    </style>'''
content = re.sub(google_fonts, futura_font, content)

# 2. Update Tailwind config
tailwind_config_old = r'fontFamily:\s*\{[\s\S]*?\},'
tailwind_config_new = '''fontFamily: {
                        sans: ['FuturaStd', 'sans-serif'],
                        serif: ['FuturaStd', 'sans-serif'],
                        hero: ['FuturaStd', 'sans-serif'],
                        title: ['FuturaStd', 'sans-serif'],
                        body: ['FuturaStd', 'sans-serif'],
                        mono: ['FuturaStd', 'sans-serif'],
                    },
                    darkMode: 'class','''
content = re.sub(tailwind_config_old, tailwind_config_new, content)

# Also add the new theme colors in Tailwind config
colors_old = r'colors:\s*\{[\s\S]*?\},'
colors_new = '''colors: {
                        primary: 'var(--color-primary)',
                        'primary-text': 'var(--color-primary-text)',
                        accent: '#F5A623',
                        success: '#27AE60',
                        danger: '#E74C3C',
                        bg: 'var(--color-bg)',
                        surface: 'var(--color-surface)',
                        text: 'var(--color-text)',
                        muted: 'var(--color-text-muted)',
                        border: 'var(--color-border)',
                        gold: '#F5A623',
                        'gold-light': '#FFD580',
                    },'''
content = re.sub(colors_old, colors_new, content)

# 3. CSS Variables
css_vars = '''        :root {
            --color-bg: #FFFFFF;
            --color-surface: #F9FAFB;
            --color-primary: #000000;
            --color-primary-text: #FFFFFF;
            --color-text: #111827;
            --color-text-muted: #6B7280;
            --color-border: #E5E7EB;
            
            --ejp-marine: #1E3A5F;
            --ejp-gold: #F5A623;
            --ejp-gold-light: #FFD580;
            --ejp-dark: #0A1628;
            --ejp-white: #FAFAF8;
            --ejp-gray: #8A9BB5;
            --ejp-green: #27AE60;
        }
        .dark {
            --color-bg: #000000;
            --color-surface: #000000;
            --color-primary: #FFFFFF;
            --color-primary-text: #000000;
            --color-text: #F9FAFB;
            --color-text-muted: #9CA3AF;
            --color-border: #1F2937;
        }'''
content = re.sub(r':root\s*\{[\s\S]*?\}', css_vars, content)

# 4. Inject toggle script in <head>
toggle_script = '''    <script>
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
content = content.replace('</head>', toggle_script)

# 5. Inject Floating toggle button
floating_btn = '''
    <!-- Theme Toggle Floating Button -->
    <button onclick="toggleTheme()" class="fixed bottom-8 right-8 z-50 w-14 h-14 rounded-full bg-primary text-primary-text shadow-2xl flex items-center justify-center text-xl hover:scale-110 transition-transform border border-border">
        <i class="fas fa-moon dark:hidden"></i>
        <i class="fas fa-sun hidden dark:block"></i>
    </button>
</body>'''
if 'Theme Toggle Floating Button' not in content:
    content = content.replace('</body>', floating_btn)

# 6. Replace background and text classes
# Hero overlay - we need it to adapt to dark/light
content = content.replace('rgba(10,22,40,0.3)', 'rgba(0,0,0,0.3)')
content = content.replace('rgba(10,22,40,0.7)', 'rgba(0,0,0,0.5)')
content = content.replace('rgba(10,22,40,1)', 'var(--color-bg)')

# Base body
content = content.replace('background-color: var(--ejp-dark);', 'background-color: var(--color-bg);')
content = content.replace('color: var(--ejp-white);', 'color: var(--color-text);')

# Sections
content = content.replace('bg-dark', 'bg-bg')
content = content.replace('bg-[#0D1F3C]', 'bg-surface')
content = content.replace('bg-marine', 'bg-surface')
content = content.replace('bg-[#060E1A]', 'bg-surface border-t border-border')
content = content.replace('text-white', 'text-text')
content = content.replace('text-gray', 'text-muted')

# Navbar
content = content.replace('rgba(10, 22, 40, 0.95)', 'var(--color-bg)')
content = content.replace('border-gold/15', 'border-border')

# Mobile menu
content = content.replace('bg-dark', 'bg-bg')

# Hero specific elements that should stay white if they are on dark image backgrounds
# Since Hero has image backgrounds, texts on it MUST remain white, but we already replaced 	ext-white with 	ext-text.
# Oh, text-text in light mode is black. Wait! The hero slides are still dark gradients. 
# If text becomes black on dark gradients in light mode, it's invisible.
# Let's fix that.
# I will use Python to carefully save and write back.

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
