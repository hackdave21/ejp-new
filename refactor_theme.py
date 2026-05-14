import os
import re

directories = ['frontend', 'admin', 'chef']

# Emojis to Icons map
emojis = {
    '??': '<i class="fas fa-users text-accent"></i>',
    '??': '<i class="fas fa-clipboard-list text-accent"></i>',
    '??': '<i class="fas fa-file-alt text-accent"></i>',
    '??': '<i class="fas fa-hand-sparkles text-accent"></i>',
    '??': '<i class="fas fa-exclamation-triangle text-amber-500"></i>',
    '??': '<i class="fas fa-glass-cheers text-accent"></i>',
    '??': '<i class="fas fa-trophy text-accent"></i>',
    '??': '<i class="fas fa-calendar-alt text-accent"></i>',
    '??': '<i class="fas fa-cog text-accent"></i>',
    '??': '<i class="fas fa-lock text-accent"></i>',
    '?': '<i class="fas fa-check-circle text-success"></i>',
    '??': '<i class="fas fa-book text-accent"></i>',
    '??': '<i class="fas fa-chart-line text-accent"></i>'
}

css_vars = '''
        :root {
            --color-bg: #FFFFFF;
            --color-surface: #F9FAFB;
            --color-primary: #000000;
            --color-primary-text: #FFFFFF;
            --color-text: #111827;
            --color-text-muted: #6B7280;
            --color-border: #E5E7EB;
        }
        .dark {
            --color-bg: #000000;
            --color-surface: #111111;
            --color-primary: #FFFFFF;
            --color-primary-text: #000000;
            --color-text: #F9FAFB;
            --color-text-muted: #9CA3AF;
            --color-border: #374151;
        }
'''

toggle_script = '''
    <script>
        // Theme Toggle Script
        function initTheme() {
            if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }
        initTheme();
        
        function toggleTheme() {
            document.documentElement.classList.toggle('dark');
            if (document.documentElement.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        }
    </script>
</head>
'''

toggle_btn = '''<button onclick="toggleTheme()" class="w-10 h-10 rounded-full bg-surface border border-border text-text hover:text-accent transition-colors flex items-center justify-center relative shadow-sm">
                        <i class="fas fa-moon dark:hidden"></i>
                        <i class="fas fa-sun hidden dark:block"></i>
                    </button>'''

for d in directories:
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Replace emojis
                for emoji, icon in emojis.items():
                    content = content.replace(emoji, icon)

                # 2. Inject CSS Vars into <style> block
                if '<style>' in content and '--color-bg' not in content:
                    content = content.replace('<style>', f'<style>{css_vars}')

                # 3. Inject Toggle Script before </head>
                if 'initTheme()' not in content:
                    content = content.replace('</head>', toggle_script)

                # 4. Update Tailwind config
                # Make primary black, text dynamic. Add dark classes to standard HTML elements.
                content = re.sub(r'colors:\s*\{[^}]+\}', "colors: { primary: 'var(--color-primary)', accent: '#F5A623', success: '#27AE60', danger: '#E74C3C', bg: 'var(--color-bg)', surface: 'var(--color-surface)', text: 'var(--color-text)', muted: 'var(--color-text-muted)', border: 'var(--color-border)', chef: '#115E59' }", content)
                if 'darkMode:' not in content:
                    content = content.replace('tailwind.config = {', "tailwind.config = {\n            darkMode: 'class',")

                # 5. Class replacements
                content = content.replace('bg-white', 'bg-surface')
                content = content.replace('bg-[#F4F7FE]', 'bg-bg')
                content = content.replace('text-[#1A1A2E]', 'text-text')
                content = content.replace('text-gray-900', 'text-text')
                content = content.replace('text-gray-800', 'text-text')
                content = content.replace('text-gray-500', 'text-muted')
                content = content.replace('text-gray-400', 'text-muted')
                content = content.replace('border-gray-50', 'border-border')
                content = content.replace('border-gray-100', 'border-border')
                content = content.replace('border-gray-200', 'border-border')
                
                # Careful with text-white: if it's on a bg-primary button, it needs to be text-primary-text
                # Since we changed bg-primary to use black in light mode, text-white should become text-primary-text inside primary buttons.
                # Actually, standardizing 	ext-white inside buttons to 	ext-primary-text when g-primary is present:
                # This is tricky with simple replace. Let's just do 	ext-white -> 	ext-primary-text ONLY if it's right next to g-primary.
                content = re.sub(r'bg-primary(.*?)text-white', r'bg-primary\1text-primary-text', content)

                # 6. Inject Toggle button in the header. We'll find <div class="flex items-center gap-4"> in headers and prepend the button.
                if 'toggleTheme()' not in content and '<div class="flex items-center gap-4">' in content:
                    content = content.replace('<div class="flex items-center gap-4">', f'<div class="flex items-center gap-4">\n                    {toggle_btn}', 1)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Refactored {filepath}")
