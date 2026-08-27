import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('e:/github-portfolio/input/pandiyan.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

idx = svg.find('rendering subject')
print('=== AROUND RENDERING SUBJECT ===')
print(svg[idx-200:idx+3000])

print('=== ALL ANIMATE TAGS IN PANDIYAN SVG ===')
import re
animates = re.findall(r'<animate[\s\S]*?/>|<animate[\s\S]*?</animate>', svg)
for a in animates[:10]:
    print('ANIMATE:', a)
