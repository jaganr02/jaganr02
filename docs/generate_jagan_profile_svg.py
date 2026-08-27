import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET

# Load Jagan's real cropped photo
src_path = 'e:/github-portfolio/assets/passport-photo.jpg'
img = Image.open(src_path).convert('RGB')

# Matrix dimension for portrait: 48 cols by 46 rows
cols = 48
rows = 46
resized = img.resize((cols, rows), Image.Resampling.LANCZOS)
np_img = np.array(resized)

def get_char_and_color(r, g, b, x_idx, y_idx):
    # Isolate foreground (Jagan) from background (green trees/outdoor foliage)
    is_green_bg = (int(g) > int(r) + 10) and (int(g) > int(b) + 3)
    is_corner_bg = (y_idx < 16 and (x_idx < 10 or x_idx > 38)) or (y_idx < 8 and (x_idx < 14 or x_idx > 34))
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    
    if (is_green_bg or is_corner_bg) and luminance > 85:
        return None
    
    if luminance > 215:
        return None
    elif luminance > 175:
        return ('&#183;', '#cfe2ea') # Dot
    elif luminance > 140:
        return ('&#9617;', '#a6c9d6') # Light shade
    elif luminance > 105:
        return ('&#9618;', '#38bdf8') # Medium shade
    elif luminance > 65:
        return ('&#9619;', '#0284c7') # Dark shade
    else:
        return ('&#9608;', '#0f766e') # Deep cyan block

start_y = 284.0
step_y = 3.4
start_time = 1.85
step_time = 0.035

svg_subject_lines = []

for row_idx in range(rows):
    y_pos = start_y + row_idx * step_y
    begin_t = start_time + row_idx * step_time
    
    current_spans = []
    current_char_run = ""
    current_color = None
    run_start_x = None
    char_count = 0
    
    for col_idx in range(cols):
        r, g, b = np_img[row_idx, col_idx]
        res = get_char_and_color(r, g, b, col_idx, row_idx)
        
        x_pos = round(700 + col_idx * 1.75, 1)
        
        if res is not None:
            char, color = res
            if color == current_color and run_start_x is not None:
                current_char_run += char
                char_count += 1
            else:
                if current_char_run:
                    text_len = round(char_count * 1.75, 1)
                    current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = char
                current_color = color
                run_start_x = x_pos
                char_count = 1
        else:
            if current_char_run:
                text_len = round(char_count * 1.75, 1)
                current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = ""
                current_color = None
                run_start_x = None
                char_count = 0
                
    if current_char_run:
        text_len = round(char_count * 1.75, 1)
        current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
        
    if current_spans:
        spans_str = ''.join(current_spans)
        line_svg = f'<text y="{round(y_pos, 1)}" opacity="0">{spans_str}<animate attributeName="opacity" from="0" to="1" begin="{round(begin_t, 2)}s" dur="0.35s" fill="freeze"/></text>'
        svg_subject_lines.append(line_svg)

matrix_xml = '\n'.join(svg_subject_lines)

svg_template = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="570" viewBox="0 0 900 570" fill="none" role="img" aria-label="R Jagan - AI Engineer &amp; Intelligent Systems Developer - RAG pipeline profile">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff"/>
    <stop offset="1" stop-color="#eef2fb"/>
  </linearGradient>

  <linearGradient id="nameGrad" gradientUnits="userSpaceOnUse" x1="70" y1="0" x2="500" y2="0">
    <stop offset="0" stop-color="#7c3aed"/>
    <stop offset="0.5" stop-color="#0284c7"/>
    <stop offset="1" stop-color="#7c3aed"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="-430 0" to="430 0" dur="4s" repeatCount="indefinite"/>
  </linearGradient>

  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="#0284c7" stop-opacity="0.8"/>
    <stop offset="1" stop-color="#0284c7" stop-opacity="0"/>
  </radialGradient>

  <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
    <feGaussianBlur stdDeviation="3"/>
  </filter>

  <filter id="d3" x="-30%" y="-30%" width="160%" height="170%">
    <feDropShadow dx="0" dy="7" stdDeviation="8" flood-color="#64748b" flood-opacity="0.25"/>
  </filter>

  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
    <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#e2e8f0" stroke-width="0.8"/>
  </pattern>

  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Consolas, Menlo, monospace; }}
    .sans {{ font-family: 'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, sans-serif; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    .cursor {{ animation: blink 1s infinite; }}
  </style>
</defs>

<!-- Outer Canvas -->
<rect width="900" height="570" rx="20" fill="url(#bg)"/>
<rect width="900" height="570" rx="20" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="8 8"/>
<rect width="900" height="570" rx="20" fill="url(#grid)" opacity="0.6"/>

<!-- Top Search Bar -->
<g transform="translate(60 38)" filter="url(#d3)">
  <rect width="360" height="42" rx="21" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <text x="24" y="26" class="mono" font-size="14" font-weight="600" fill="#0284c7">&gt;</text>
  <text x="42" y="26" class="sans" font-size="14" font-weight="500" fill="#1e293b">&quot;who is Jagan R?&quot;</text>
  <rect x="188" y="13" width="8" height="17" fill="#0284c7" class="cursor"/>
</g>

<!-- Top Pipeline Header & Status -->
<text x="470" y="64" class="mono" font-size="11" font-weight="600" fill="#64748b" letter-spacing="1.5">RAG PIPELINE / PROFILE v2.0</text>
<text x="770" y="64" class="mono" font-size="11" font-weight="600" fill="#64748b">online</text>
<circle cx="820" cy="60" r="4" fill="#10b981"/>

<!-- Vertical Flow Line from Search Bar to Node 1 -->
<line x1="200" y1="80" x2="200" y2="135" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3 3"/>

<!-- Pipeline Horizontal Stream Path -->
<path d="M 200 160 L 780 160" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="4 4"/>

<!-- Animated Pulse Dot Traveling Through Pipeline -->
<circle r="4" fill="#0284c7">
  <animateMotion path="M 200 160 L 780 160" dur="4s" repeatCount="indefinite"/>
</circle>

<!-- Pipeline Nodes -->
<!-- Node 1: Query Embedding -->
<g transform="translate(175 135)">
  <circle cx="25" cy="25" r="24" fill="#ffffff" stroke="#0284c7" stroke-width="1.8"/>
  <circle cx="25" cy="25" r="5" fill="#0284c7"/>
  <text x="25" y="62" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">1 · QUERY</text>
  <text x="25" y="72" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">EMBEDDING</text>
</g>

<!-- Node 2: Qdrant Vector Store -->
<g transform="translate(290 132)">
  <ellipse cx="40" cy="12" rx="34" ry="10" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
  <path d="M 6 12 v 14 a 34 10 0 0 0 68 0 v -14" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
  <path d="M 6 26 v 14 a 34 10 0 0 0 68 0 v -14" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="40" y="16" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#7c3aed">Qdrant</text>
  <text x="40" y="65" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">2 · SIMILARITY</text>
  <text x="40" y="75" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">SEARCH</text>
</g>

<!-- Node 3: Top-K Chunks -->
<g transform="translate(405 134)">
  <rect x="0" y="0" width="48" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1"/>
  <text x="24" y="9" text-anchor="middle" class="mono" font-size="7" font-weight="600" fill="#0284c7">chunk 1</text>
  
  <rect x="0" y="16" width="48" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1"/>
  <text x="24" y="25" text-anchor="middle" class="mono" font-size="7" font-weight="600" fill="#0284c7">chunk 2</text>

  <rect x="0" y="32" width="48" height="13" rx="3" fill="#ffffff" stroke="#38bdf8" stroke-width="1"/>
  <text x="24" y="41" text-anchor="middle" class="mono" font-size="7" font-weight="600" fill="#0284c7">chunk 3</text>
  
  <text x="24" y="63" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">3 · TOP-K</text>
  <text x="24" y="73" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">CHUNKS</text>
</g>

<!-- Node 4: Prompt Construction -->
<g transform="translate(490 134)">
  <rect x="0" y="0" width="88" height="48" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="44" y="28" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#7c3aed">PROMPT</text>
  <text x="44" y="63" text-anchor="middle" class="mono" font-size="8" font-weight="600" fill="#64748b">4 · PROMPT CONSTRUCT</text>
  <text x="44" y="73" text-anchor="middle" class="mono" font-size="8" font-weight="600" fill="#64748b">(query + context)</text>
</g>

<!-- Node 5: LLM Generation -->
<g transform="translate(615 134)">
  <rect x="0" y="0" width="88" height="48" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.8"/>
  <text x="44" y="28" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="#0284c7">LLM</text>
  <text x="44" y="63" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">5 · GENERATION</text>
</g>

<!-- Node 6: Final Answer -->
<g transform="translate(740 135)">
  <circle cx="25" cy="25" r="24" fill="#ffffff" stroke="#10b981" stroke-width="2"/>
  <text x="25" y="62" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">FINAL</text>
  <text x="25" y="72" text-anchor="middle" class="mono" font-size="8.5" font-weight="600" fill="#64748b">ANSWER</text>
</g>

<!-- Vertical Connector Line from Final Answer to Streaming Terminal Card -->
<line x1="765" y1="184" x2="765" y2="235" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>

<!-- ================= STREAMING TERMINAL PROFILE CARD ================= -->
<g transform="translate(60 235)" filter="url(#d3)">
  <!-- Card Background -->
  <rect width="780" height="268" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>

  <!-- Top Terminal Controls -->
  <circle cx="24" cy="22" r="5" fill="#ef4444"/>
  <circle cx="38" cy="22" r="5" fill="#f59e0b"/>
  <circle cx="52" cy="22" r="5" fill="#10b981"/>
  <text x="72" y="26" class="mono" font-size="11" fill="#64748b">generated_profile.md · streaming...</text>

  <!-- Candidate Name with Shimmering Gradient -->
  <text x="24" y="68" class="sans" font-size="34" font-weight="900" fill="url(#nameGrad)" letter-spacing="-0.5px">R JAGAN</text>

  <!-- Role Title -->
  <text x="24" y="93" class="sans" font-size="15" font-weight="600" fill="#0284c7">AI Engineer · Generative AI &amp; Multi-Agent Systems</text>

  <!-- Details Row -->
  <g transform="translate(24, 116)">
    <text x="0" y="0" class="sans" font-size="12" font-weight="500" fill="#475569">🎓 B.Tech · AI &amp; DS</text>
    <text x="160" y="0" class="sans" font-size="12" font-weight="500" fill="#475569">📍 India</text>
    <text x="235" y="0" class="sans" font-size="12" font-weight="500" fill="#475569">🛠️ building Multi-Agent &amp; RAG systems</text>
  </g>

  <!-- Tech Skill Pills: Row 1 -->
  <g transform="translate(24, 132)">
    <!-- Python -->
    <rect x="0" y="0" width="66" height="22" rx="11" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <circle cx="9" cy="11" r="3" fill="#16a34a"/>
    <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="#166534">Python</text>

    <!-- FastAPI -->
    <rect x="74" y="0" width="70" height="22" rx="11" fill="#f0fdfa" stroke="#99f6e4" stroke-width="1"/>
    <circle cx="83" cy="11" r="3" fill="#0d9488"/>
    <text x="92" y="15" class="mono" font-size="10" font-weight="600" fill="#115e59">FastAPI</text>

    <!-- LangGraph -->
    <rect x="152" y="0" width="86" height="22" rx="11" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
    <circle cx="161" cy="11" r="3" fill="#9333ea"/>
    <text x="170" y="15" class="mono" font-size="10" font-weight="600" fill="#6b21a8">LangGraph</text>

    <!-- RAG -->
    <rect x="246" y="0" width="56" height="22" rx="11" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1"/>
    <circle cx="255" cy="11" r="3" fill="#7c3aed"/>
    <text x="264" y="15" class="mono" font-size="10" font-weight="600" fill="#5b21b6">RAG</text>

    <!-- Qdrant -->
    <rect x="310" y="0" width="70" height="22" rx="11" fill="#fef2f2" stroke="#fecaca" stroke-width="1"/>
    <circle cx="319" cy="11" r="3" fill="#dc2626"/>
    <text x="328" y="15" class="mono" font-size="10" font-weight="600" fill="#991b1b">Qdrant</text>

    <!-- Scikit-Learn -->
    <rect x="388" y="0" width="94" height="22" rx="11" fill="#fffbeb" stroke="#fde68a" stroke-width="1"/>
    <circle cx="397" cy="11" r="3" fill="#d97706"/>
    <text x="406" y="15" class="mono" font-size="10" font-weight="600" fill="#92400e">scikit-learn</text>
  </g>

  <!-- Tech Skill Pills: Row 2 -->
  <g transform="translate(24, 160)">
    <!-- MCP -->
    <rect x="0" y="0" width="56" height="22" rx="11" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <circle cx="9" cy="11" r="3" fill="#16a34a"/>
    <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="#166534">MCP</text>

    <!-- LangChain -->
    <rect x="64" y="0" width="86" height="22" rx="11" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1"/>
    <circle cx="73" cy="11" r="3" fill="#7c3aed"/>
    <text x="82" y="15" class="mono" font-size="10" font-weight="600" fill="#5b21b6">LangChain</text>

    <!-- Docker -->
    <rect x="158" y="0" width="70" height="22" rx="11" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1"/>
    <circle cx="167" cy="11" r="3" fill="#0284c7"/>
    <text x="176" y="15" class="mono" font-size="10" font-weight="600" fill="#0369a1">Docker</text>

    <!-- MySQL -->
    <rect x="236" y="0" width="66" height="22" rx="11" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
    <circle cx="245" cy="11" r="3" fill="#2563eb"/>
    <text x="254" y="15" class="mono" font-size="10" font-weight="600" fill="#1e40af">MySQL</text>
  </g>

  <!-- Motto Quote -->
  <text x="24" y="206" class="sans" font-style="italic" font-weight="500" font-size="13" fill="#6366f1">&quot;Learn relentlessly. Build fearlessly. Ship something that matters.&quot;</text>

  <!-- Contact Line with Blinking Cursor -->
  <text x="24" y="235" class="mono" font-size="11" fill="#64748b">linkedin.com/in/r-jagan-52bb94289 · rajajagan697@gmail.com</text>
  <rect x="446" y="224" width="6" height="13" fill="#0284c7" class="cursor"/>
</g>

<!-- Right Side: Jagan's 3D Progressive Holographic Portrait Matrix -->
<text x="742" y="268" text-anchor="middle" class="mono" font-size="9" letter-spacing="2" fill="#64748b">&#9707; rendering subject&#8230;</text>
<g class="mono" font-size="3.35">
{matrix_xml}
</g>

<!-- Status Pill Below Subject -->
<g transform="translate(696 450)">
  <rect width="92" height="20" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
  <circle cx="12" cy="10" r="3.5" fill="#10b981"/>
  <text x="22" y="14" class="mono" font-size="9.5" font-weight="600" fill="#334155">jaganr02</text>
</g>

<!-- Bottom Telemetry Status Line -->
<g transform="translate(60 540)">
  <text x="0" y="0" class="mono" font-size="10" fill="#64748b">
    retrieved: <tspan fill="#0284c7" font-weight="600">top-k chunks</tspan>  ·  latency: <tspan fill="#334155" font-weight="600">38 ms</tspan>  ·  throughput: <tspan fill="#334155" font-weight="600">94 tok/s</tspan>  ·  context: <tspan fill="#16a34a" font-weight="600">grounded ✓</tspan>
  </text>
  <text x="780" y="0" text-anchor="end" class="mono" font-size="10" font-weight="600" fill="#64748b">
    github.com/jaganr02
  </text>
</g>
</svg>'''

with open('e:/github-portfolio/assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(svg_template)

# Validate XML immediately
tree = ET.parse('e:/github-portfolio/assets/hero.svg')
print('SUCCESS! Pure Jagan hero.svg created and validated with zero Pandiyan data and real Jagan holographic face!')
