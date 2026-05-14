import os
import re

admin_dir = 'admin'
frontend_dir = 'frontend'

def process_file(filepath, is_admin):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    if is_admin:
        # Admin aside
        content = re.sub(r'<aside class="([^"]*)bg-dark text-white([^"]*)">', r'<aside class="\1bg-surface border-r border-border\2">', content)
        # Admin links
        content = content.replace('text-white/50', 'text-muted')
        content = content.replace('text-white/40', 'text-muted')
        # Bottom logout link text color
        content = content.replace('border-white/5', 'border-border')
        
    else:
        # Frontend aside
        content = re.sub(r'<aside id="sidebar" class="([^"]*)bg-primary text-white border-r border-primary/20([^"]*)">', r'<aside id="sidebar" class="\1bg-surface border-r border-border\2">', content)
        # For frontend there might be other bg-primary classes, so we only target sidebar related
        content = content.replace('text-white/70', 'text-muted')
        content = content.replace('text-white/40', 'text-muted')
        content = content.replace('border-white/10', 'border-border')
        # The EJP logo background
        content = content.replace('bg-white text-primary', 'bg-primary text-primary-text')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated sidebar in {filepath}")

for root, _, files in os.walk(admin_dir):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file), True)

for root, _, files in os.walk(frontend_dir):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file), False)

