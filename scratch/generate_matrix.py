import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

# Load user's photo
src_path = 'e:/github-portfolio/assets/passport-photo.jpg'
img = Image.open(src_path).convert('RGB')
w, h = img.size

# We want roughly 54 columns by 50 rows of ASCII characters
cols = 52
rows = 48

# Resize image
resized = img.resize((cols, rows), Image.Resampling.LANCZOS)
np_img = np.array(resized)

# Color palettes like Pandiyan (from faint cloud to deep teal)
# Level 0 (bg): transparent/empty
# Level 1 (faint edge): · (#cfe2ea)
# Level 2 (light): ░ (#a6c9d6)
# Level 3 (medium): ▒ (#58a6ff)
# Level 4 (dark): ▓ (#0284c7)
# Level 5 (very dark hair/eyes/beard): █ (#0f766e / #0369a1)

ascii_lines = []
start_y = 284.0
step_y = 3.3
start_time = 2.05
step_time = 0.035

# Color mapping helper
def get_char_and_color(r, g, b, x_idx, y_idx):
    # Detect background (greenish trees/leaves or bright sky around outer borders)
    # If green > r + 15 and green > b: it's the green foliage
    # If y_idx < 15 and (x_idx < 12 or x_idx > 40) and g > 110: background
    is_green_bg = (int(g) > int(r) + 12) and (int(g) > int(b) + 5)
    is_outer_bg = (y_idx < 22 and (x_idx < 10 or x_idx > 42)) or (y_idx < 12 and (x_idx < 14 or x_idx > 38))
    
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    
    # If background, return None
    if (is_green_bg or is_outer_bg) and luminance > 90:
        return None
    
    if luminance > 200:
        return None # bright/white
    elif luminance > 165:
        return ('·', '#cfe2ea')
    elif luminance > 130:
        return ('░', '#a6c9d6')
    elif luminance > 95:
        return ('▒', '#38bdf8')
    elif luminance > 60:
        return ('▓', '#0284c7')
    else:
        return ('█', '#0f766e')

svg_subject_lines = []

for row_idx in range(rows):
    y_pos = start_y + row_idx * step_y
    begin_t = start_time + row_idx * step_time
    
    current_spans = []
    current_char_run = ""
    current_color = None
    run_start_x = None
    
    for col_idx in range(cols):
        r, g, b = np_img[row_idx, col_idx]
        res = get_char_and_color(r, g, b, col_idx, row_idx)
        
        # Position x in SVG coordinate space (center around 740, width ~ 80)
        x_pos = round(700 + col_idx * 1.6, 1)
        
        if res is not None:
            char, color = res
            if color == current_color and run_start_x is not None:
                current_char_run += char
            else:
                if current_char_run:
                    text_len = round(len(current_char_run) * 1.6, 1)
                    current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = char
                current_color = color
                run_start_x = x_pos
        else:
            if current_char_run:
                text_len = round(len(current_char_run) * 1.6, 1)
                current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
                current_char_run = ""
                current_color = None
                run_start_x = None
                
    if current_char_run:
        text_len = round(len(current_char_run) * 1.6, 1)
        current_spans.append(f'<tspan x="{run_start_x}" textLength="{text_len}" lengthAdjust="spacingAndGlyphs" fill="{current_color}">{current_char_run}</tspan>')
        
    if current_spans:
        spans_str = ''.join(current_spans)
        line_svg = f'<text y="{round(y_pos, 1)}" opacity="0">{spans_str}<animate attributeName="opacity" from="0" to="1" begin="{round(begin_t, 2)}s" dur="0.35s" fill="freeze"/></text>'
        svg_subject_lines.append(line_svg)

print(f'Generated {len(svg_subject_lines)} progressive animated holographic matrix scan lines!')
with open('e:/github-portfolio/scratch/subject_matrix.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_subject_lines))
