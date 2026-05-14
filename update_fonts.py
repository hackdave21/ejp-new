import os
import re

directories = ['frontend', 'admin', 'chef']

google_fonts_pattern = re.compile(r'<!-- Fonts -->\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*<link href="https://fonts\.googleapis\.com/css2\?family=[^"]+" rel="stylesheet">', re.MULTILINE)

futura_css = '''<!-- Fonts (FuturaStd) -->
    <style>
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdBook.otf') format('opentype');
            font-weight: 400;
            font-style: normal;
        }
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdMedium.otf') format('opentype');
            font-weight: 500;
            font-style: normal;
        }
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdHeavy.otf') format('opentype');
            font-weight: 600;
            font-style: normal;
        }
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdBold.otf') format('opentype');
            font-weight: 700;
            font-style: normal;
        }
        @font-face {
            font-family: 'FuturaStd';
            src: url('fonts/FuturaStdExtraBold.otf') format('opentype');
            font-weight: 800;
            font-style: normal;
        }
    </style>'''

tailwind_font_pattern = re.compile(r'fontFamily:\s*\{\s*sans:\s*\[\'Inter\',\s*\'sans-serif\'\],\s*serif:\s*\[\'Playfair Display\',\s*\'serif\'\],\s*\}', re.MULTILINE)

tailwind_font_replacement = '''fontFamily: {
                        sans: ['FuturaStd', 'sans-serif'],
                        serif: ['FuturaStd', 'sans-serif'],
                    }'''

for d in directories:
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = google_fonts_pattern.sub(futura_css, content)
                new_content = tailwind_font_pattern.sub(tailwind_font_replacement, new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")
