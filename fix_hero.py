import os
import re

filepath = r'd:\EJP Template\frontend\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Nav Bar (It starts transparent over dark hero, so links should be text-white)
# Then when scrolled it gets bg-surface, but the text needs to adapt.
# Actually, if the hero is ALWAYS dark, the transparent nav MUST have white text. 
# But when scrolled, it gets g-bg, so the text should become 	ext-text.
# Tailwind allows 	ext-white but we can change it on scroll via JS. 
# For now, let's just make the text adapt in JS, or keep it 	ext-primary.
# Let's just fix the hero section:
hero_start = content.find('<section id="hero"')
about_start = content.find('<section id="about"')

hero_content = content[hero_start:about_start]
hero_content = hero_content.replace('text-text', 'text-white')
content = content[:hero_start] + hero_content + content[about_start:]

# Fix CTA Section
cta_start = content.find('<section id="cta"')
footer_start = content.find('<footer')

cta_content = content[cta_start:footer_start]
cta_content = cta_content.replace('text-text', 'text-white')
content = content[:cta_start] + cta_content + content[footer_start:]

# Fix Testimonials Section - it has a dark bg
test_start = content.find('<section id="temoignages"')
cta_start_again = content.find('<section id="cta"')
test_content = content[test_start:cta_start_again]
# Actually wait, I made all sections use bg-surface or bg-bg in the first script!
# Let's check what I replaced:
# content = content.replace('bg-dark', 'bg-bg')
# content = content.replace('bg-[#0D1F3C]', 'bg-surface')
# content = content.replace('bg-marine', 'bg-surface')

# Since I replaced bg-dark with bg-bg, in light mode the backgrounds ARE white!
# So 	ext-text becoming black is PERFECTLY CORRECT!
# The only exception is the Hero section, which uses inline style="background: linear-gradient...".
# So the Hero section backgrounds are permanently dark!
# And the CTA section has an absolute div with g-gradient-to-br from-marine to-gold/40. 
# Wait, rom-marine was removed from Tailwind config! It's now rom-surface or broken.
# Let's check if marine is in Tailwind config. No, I overwrote colors: {...} and removed marine.
