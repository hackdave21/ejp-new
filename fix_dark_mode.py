import os
import re

directories = ['frontend', 'admin', 'chef']

css_vars_dark = '''        .dark {
            --color-bg: #000000;
            --color-surface: #000000;
            --color-primary: #FFFFFF;
            --color-primary-text: #000000;
            --color-text: #F9FAFB;
            --color-text-muted: #9CA3AF;
            --color-border: #1F2937;
        }'''

for d in directories:
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Update dark mode variables to be pure black
                content = re.sub(r'\.dark\s*\{[^}]+\}', css_vars_dark, content)
                
                # 2. Aggressively remove/replace light hardcoded backgrounds
                content = content.replace('bg-gray-50', 'bg-surface')
                content = content.replace('bg-gray-100', 'bg-surface')
                content = content.replace('bg-[#F8F9FA]', 'bg-surface')
                content = content.replace('bg-[#F4F7FE]', 'bg-bg')
                
                # 3. Replace text colors that might have been missed
                content = content.replace('text-gray-600', 'text-muted')
                content = content.replace('text-gray-700', 'text-text')
                content = content.replace('text-gray-800', 'text-text')
                content = content.replace('text-gray-900', 'text-text')
                content = content.replace('text-gray-500', 'text-muted')
                content = content.replace('text-gray-400', 'text-muted')
                content = content.replace('text-[#1A1A2E]', 'text-text')
                
                # 4. Replace remaining border colors
                content = content.replace('border-gray-50', 'border-border')
                content = content.replace('border-gray-100', 'border-border')
                content = content.replace('border-gray-200', 'border-border')
                content = content.replace('border-gray-300', 'border-border')
                
                # 5. Fix icons. Some icons might be colored with text-gray-* or they are invisible because they have no color and inherit.
                # Actually, if we fixed text-gray-*, the icons should inherit text-muted or text-text which is white in dark mode.

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed colors in {filepath}")
