import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import base64

# Load Jagan's cropped photo
src_path = 'e:/github-portfolio/assets/passport-photo.jpg'
img = Image.open(src_path).convert('RGB')
w, h = img.size

# High-resolution enhancement
enh_s = ImageEnhance.Sharpness(img)
sharp = enh_s.enhance(2.0)
enh_c = ImageEnhance.Contrast(sharp)
contrast = enh_c.enhance(1.3)

np_img = np.array(contrast)

# Create alpha channel to cleanly remove the green foliage / outdoor background
# Green foliage has high G channel relative to R and B
r = np_img[:, :, 0].astype(int)
g = np_img[:, :, 1].astype(int)
b = np_img[:, :, 2].astype(int)

# Background mask: green foliage and corner sky
is_green = (g > r + 8) & (g > b + 4)
# Corner background areas (outer edges above shoulders)
y_coords, x_coords = np.indices((h, w))
is_top_corner = ((y_coords < int(h * 0.35)) & ((x_coords < int(w * 0.22)) | (x_coords > int(w * 0.78)))) | \
                ((y_coords < int(h * 0.18)) & ((x_coords < int(w * 0.30)) | (x_coords > int(w * 0.70))))

is_bg = (is_green | is_top_corner) & ((r + g + b) / 3 > 80)

# Build smooth alpha mask
alpha = np.where(is_bg, 0, 255).astype(np.uint8)

# Feather the edges with Gaussian blur on the mask for natural blending
alpha_img = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(radius=1.2))

# Combine into RGBA
rgba_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
rgba_img.paste(contrast, (0, 0), alpha_img)

# Save HD crystal clear cutout
rgba_img.save('e:/github-portfolio/assets/jagan-hd-cutout.png', 'PNG')
print('HD Crystal Clear Cutout saved! Size:', rgba_img.size)

# Convert to Base64
with open('e:/github-portfolio/assets/jagan-hd-cutout.png', 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')

with open('e:/github-portfolio/scratch/photo_b64.txt', 'w') as f:
    f.write(b64_str)
print('Base64 ready!')
