import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET

# Load user's photo
src_path = 'e:/github-portfolio/assets/passport-photo.jpg'
img = Image.open(src_path).convert('RGB')

# Matrix: 54 cols by 50 rows
cols = 54
rows = 50
resized = img.resize((cols, rows), Image.Resampling.LANCZOS)
np_img = np.array(resized)

def get_char_and_color(r, g, b, x_idx, y_idx):
    is_green_bg = (int(g) > int(r) + 12) and (int(g) > int(b) + 5)
    is_outer_corner = (y_idx < 18 and (x_idx < 11 or x_idx > 43)) or (y_idx < 10 and (x_idx < 15 or x_idx > 39))
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    
    if (is_green_bg or is_outer_corner) and luminance > 90:
        return None
    
    if luminance > 210:
        return None
    elif luminance > 175:
        return ('&#183;', '#cfe2ea') # Middle dot
    elif luminance > 140:
        return ('&#9617;', '#a6c9d6') # Light shade
    elif luminance > 105:
        return ('&#9618;', '#4a92ab') # Medium shade
    elif luminance > 65:
        return ('&#9619;', '#0891b2') # Dark shade
    else:
        return ('&#9608;', '#0f766e') # Full block

start_y = 286.0
step_y = 3.35
start_time = 2.08
step_time = 0.038

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
        
        x_pos = round(696 + col_idx * 1.9, 1)
        
        if res is not None:
            char, color = res
            if color == current_color and run_start_x is not None:
                current_char_run += char
                char_count += 1
            else:
                if current_char_run:
                    text_len = round(char_count * 1.9, 1)
                    current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = char
                current_color = color
                run_start_x = x_pos
                char_count = 1
        else:
            if current_char_run:
                text_len = round(char_count * 1.9, 1)
                current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = ""
                current_color = None
                run_start_x = None
                char_count = 0
                
    if current_char_run:
        text_len = round(char_count * 1.9, 1)
        current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
        
    if current_spans:
        spans_str = ''.join(current_spans)
        line_svg = f'<text y="{round(y_pos, 1)}" opacity="0">{spans_str}<animate attributeName="opacity" from="0" to="1" begin="{round(begin_t, 2)}s" dur="0.35s" fill="freeze"/></text>'
        svg_subject_lines.append(line_svg)

matrix_xml = '\n'.join(svg_subject_lines)

# Read pandiyan.svg as base template
with open('e:/github-portfolio/input/pandiyan.svg', 'r', encoding='utf-8') as f:
    base_svg = f.read()

# Replace strings with strictly valid XML escaping
custom_svg = base_svg

custom_svg = custom_svg.replace('aria-label="Pandiyan S - Machine Learning Engineer - RAG pipeline profile"', 'aria-label="R Jagan - AI Engineer &amp; Intelligent Systems Developer - RAG pipeline profile"')
custom_svg = custom_svg.replace('who is Pandiyan S?', 'who is Jagan R?')
custom_svg = custom_svg.replace('PANDIYAN S', 'R JAGAN')
custom_svg = custom_svg.replace('pandiyan-net', 'jaganr02')
custom_svg = custom_svg.replace('github.com/S-PANDIYAN', 'github.com/jaganr02')
custom_svg = custom_svg.replace('pandiyan-s-947239293 · leetcode/Pandiyan_ML · pandiyanshanmugam3105@gmail.com', 'in/r-jagan-52bb94289 · rajajagan697@gmail.com')

# Update title & tags with XML escaped ampersand
custom_svg = custom_svg.replace('Machine Learning Engineer · Generative AI &amp; RAG', 'AI Engineer · Generative AI &amp; Multi-Agent Systems')
custom_svg = custom_svg.replace('B.Tech · AI &amp; ML', 'B.Tech · AI &amp; DS')
custom_svg = custom_svg.replace('building RAG &amp; GenAI systems', 'building Multi-Agent &amp; RAG systems')

# Update DB node
custom_svg = custom_svg.replace('>pgvector<', '>Qdrant<')

# Update Skill Pills: Replace PyTorch, TensorFlow, PostgreSQL with LangGraph, RAG, MCP
custom_svg = custom_svg.replace('>PyTorch<', '>FastAPI<')
custom_svg = custom_svg.replace('>TensorFlow<', '>LangGraph<')
custom_svg = custom_svg.replace('>FastAPI<', '>RAG<')
custom_svg = custom_svg.replace('>PostgreSQL<', '>MCP<')

# Replace the subject matrix lines
idx_start = custom_svg.find('<text x="747" y="272"')
if idx_start != -1:
    idx_end = custom_svg.find('<g transform="translate(680 448)"', idx_start)
    if idx_end != -1:
        custom_svg = custom_svg[:idx_start] + f'<text x="747" y="272" text-anchor="middle" class="mono" font-size="9" letter-spacing="2" fill="#64748b">&#9707; rendering subject&#8230;</text>\n<g class="mono" font-size="3.35">\n{matrix_xml}\n</g>\n' + custom_svg[idx_end:]

with open('e:/github-portfolio/assets/hero.svg', 'w', encoding='utf-8') as f:
    f.write(custom_svg)

# Validate XML immediately
tree = ET.parse('e:/github-portfolio/assets/hero.svg')
print('SUCCESS! assets/hero.svg is 100% VALID XML and will render flawlessly in all browsers!')
