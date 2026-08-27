import random

# Generate a standalone local animated contribution snake SVG
width = 860
height = 160
cols = 48
rows = 7
cell_size = 11
gap = 4
offset_x = 24
offset_y = 28

# Realistic green palette
greens = [
    "#161b22", # empty
    "#0e4429", # low
    "#006d32", # medium
    "#26a641", # high
    "#39d353"  # very high
]

cells_svg = []
random.seed(42)

for c in range(cols):
    for r in range(rows):
        x = offset_x + c * (cell_size + gap)
        y = offset_y + r * (cell_size + gap)
        # Higher density in recent months
        weight = [0.45, 0.25, 0.15, 0.1, 0.05] if c < 30 else [0.2, 0.3, 0.25, 0.15, 0.1]
        color = random.choices(greens, weights=weight)[0]
        cells_svg.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{color}" />')

svg_content = f'''<svg width="100%" height="auto" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes snakeMove {{
      0% {{ transform: translate(0px, 0px); }}
      25% {{ transform: translate(320px, 45px); }}
      50% {{ transform: translate(580px, 15px); }}
      75% {{ transform: translate(400px, 60px); }}
      100% {{ transform: translate(0px, 0px); }}
    }}
    .snake-body {{
      animation: snakeMove 14s ease-in-out infinite;
    }}
  </style>

  <!-- Container -->
  <rect width="{width}" height="{height}" rx="12" fill="#0d1117" stroke="#30363d" stroke-width="1" />
  
  <!-- Header Text -->
  <text x="{offset_x}" y="18" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#8b949e">
    CONTRIBUTION ACTIVITY · LAST 12 MONTHS
  </text>
  <text x="{width - offset_x}" y="18" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" fill="#58a6ff">
    ● Active Developer
  </text>

  <!-- Grid Cells -->
  {''.join(cells_svg)}

  <!-- Animated Snake -->
  <g class="snake-body" transform="translate({offset_x + 120}, {offset_y + 30})">
    <!-- Snake Tail to Head -->
    <rect x="-30" y="0" width="{cell_size}" height="{cell_size}" rx="2" fill="#38bdf8" opacity="0.4" />
    <rect x="-15" y="0" width="{cell_size}" height="{cell_size}" rx="2" fill="#38bdf8" opacity="0.7" />
    <rect x="0" y="0" width="{cell_size}" height="{cell_size}" rx="2" fill="#38bdf8" />
    <circle cx="9" cy="4" r="1.5" fill="#ffffff" />
    <circle cx="9" cy="8" r="1.5" fill="#ffffff" />
  </g>
</svg>'''

with open('e:/github-portfolio/assets/contribution-snake.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('Generated local assets/contribution-snake.svg successfully!')
