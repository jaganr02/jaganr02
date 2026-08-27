import urllib.request
import re

try:
    req = urllib.request.Request('https://raw.githubusercontent.com/S-PANDIYAN/S-PANDIYAN/main/README.md', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        readme = resp.read().decode('utf-8')
    print('S-PANDIYAN README:')
    print(readme)
    
    # Extract SVG source
    matches = re.findall(r'src="([^"]+\.svg)"', readme)
    for m in matches:
        url = 'https://raw.githubusercontent.com/S-PANDIYAN/S-PANDIYAN/main/' + m.lstrip('./')
        print('Fetching SVG:', url)
        req_svg = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_svg) as resp_svg:
            svg_data = resp_svg.read().decode('utf-8')
        with open('e:/github-portfolio/input/pandiyan.svg', 'w', encoding='utf-8') as f:
            f.write(svg_data)
        print('Saved pandiyan.svg! Length:', len(svg_data))
        break
except Exception as e:
    print('Error:', e)
