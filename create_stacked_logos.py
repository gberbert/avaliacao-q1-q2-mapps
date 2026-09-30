import os
from PIL import Image, ImageDraw, ImageFont

# Source logos
ntt_path = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_nttdata.png"
mapfre_path = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_mapfre.png"

img_ntt = Image.open(ntt_path).convert("RGBA")
img_mapfre = Image.open(mapfre_path).convert("RGBA")

# 1. Create a pure stacked logo with white background & rounded capsule (e.g. 500x320)
# NTT DATA on top, subtle divider, MAPFRE on the bottom
capsule_w = 480
capsule_h = 300

# Target logo dimensions to fit harmoniously
# NTT DATA original: 885 x 346 (ratio ~ 2.56)
# MAPFRE original: 1024 x 281 (ratio ~ 3.64)
target_logo_w = 340
h_ntt = int(target_logo_w * img_ntt.size[1] / img_ntt.size[0])
h_mapfre = int(target_logo_w * img_mapfre.size[1] / img_mapfre.size[0])

resized_ntt = img_ntt.resize((target_logo_w, h_ntt), Image.Resampling.LANCZOS)
resized_mapfre = img_mapfre.resize((target_logo_w, h_mapfre), Image.Resampling.LANCZOS)

# Create white capsule image with transparency around it
stacked_logo = Image.new("RGBA", (capsule_w, capsule_h), (255, 255, 255, 255))
draw = ImageDraw.Draw(stacked_logo)

# Top logo (NTT DATA) centered vertically in top half
y_ntt = int((capsule_h / 2 - h_ntt) / 2) + 10
x_ntt = int((capsule_w - target_logo_w) / 2)
stacked_logo.paste(resized_ntt, (x_ntt, y_ntt), resized_ntt)

# Divider line
draw.line([(60, int(capsule_h / 2)), (capsule_w - 60, int(capsule_h / 2))], fill=(203, 213, 225, 255), width=2)

# Bottom logo (MAPFRE) centered vertically in bottom half
y_mapfre = int(capsule_h / 2 + (capsule_h / 2 - h_mapfre) / 2) - 10
x_mapfre = int((capsule_w - target_logo_w) / 2)
stacked_logo.paste(resized_mapfre, (x_mapfre, y_mapfre), resized_mapfre)

# Save standalone stacked logo
out_stacked = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_stacked.png"
stacked_logo.save(out_stacked, "PNG")
print("Saved", out_stacked)

# 2. Create Square (600x600) Card for WhatsApp / Teams 1:1 Link Preview Box
def make_square_preview(product_title, product_sub, out_file):
    sq = Image.new("RGBA", (600, 600), (255, 255, 255, 255))
    sq_draw = ImageDraw.Draw(sq)
    
    # Border
    sq_draw.rounded_rectangle([(10, 10), (590, 590)], radius=24, outline=(226, 232, 240, 255), width=3)
    
    # Paste stacked logo in top/middle
    # Let's resize stacked_logo slightly to fit nicely
    st_w = 440
    st_h = int(st_w * capsule_h / capsule_w)
    st_resized = stacked_logo.resize((st_w, st_h), Image.Resampling.LANCZOS)
    sq.paste(st_resized, (int((600 - st_w) / 2), 70), st_resized)
    
    # Bottom section divider
    sq_draw.line([(50, 410), (550, 410)], fill=(226, 232, 240, 255), width=2)
    
    # Bottom brand label
    # Draw simple clean text if font available, or geometric badge
    sq_draw.rounded_rectangle([(70, 440), (530, 530)], radius=12, fill=(7, 10, 19, 255))
    
    sq.save(out_file, "PNG")
    print("Saved", out_file)

# 3. Create Standard OpenGraph (1200x630) Rich Preview Card
def make_og_preview(title, subtitle, tag, out_file):
    og = Image.new("RGBA", (1200, 630), (7, 10, 19, 255))
    og_draw = ImageDraw.Draw(og)
    
    # Gradient / background accent
    og_draw.rectangle([(0, 0), (1200, 630)], fill=(7, 10, 19, 255))
    # Top border glow
    og_draw.rectangle([(0, 0), (1200, 6)], fill=(0, 102, 255, 255))
    
    # White capsule on the left (420x460) with stacked logos
    c_w = 380
    c_h = 420
    cap = Image.new("RGBA", (c_w, c_h), (255, 255, 255, 255))
    cap_draw = ImageDraw.Draw(cap)
    
    t_w = 300
    h_n = int(t_w * img_ntt.size[1] / img_ntt.size[0])
    h_m = int(t_w * img_mapfre.size[1] / img_mapfre.size[0])
    
    r_ntt = img_ntt.resize((t_w, h_n), Image.Resampling.LANCZOS)
    r_map = img_mapfre.resize((t_w, h_m), Image.Resampling.LANCZOS)
    
    y_n = int((c_h / 2 - h_n) / 2) + 15
    cap.paste(r_ntt, (int((c_w - t_w) / 2), y_n), r_ntt)
    
    cap_draw.line([(40, int(c_h / 2)), (c_w - 40, int(c_h / 2))], fill=(203, 213, 225, 255), width=2)
    
    y_m = int(c_h / 2 + (c_h / 2 - h_m) / 2) - 15
    cap.paste(r_map, (int((c_w - t_w) / 2), y_m), r_map)
    
    # Paste capsule onto OG image
    og.paste(cap, (80, 105))
    og_draw.rounded_rectangle([(78, 103), (462, 527)], radius=16, outline=(0, 102, 255, 120), width=3)
    
    # Save
    og.save(out_file, "PNG")
    print("Saved", out_file)

make_square_preview("ACDC", "Cockpit", "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_square_acdc.png")
make_square_preview("AXET", "NeuralGraph 3D", "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_square_neuralgraph.png")

make_og_preview("ACDC Platform", "Cockpit Atuarial & IA", "MAPFRE & NTT DATA", "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_preview_acdc.png")
make_og_preview("AXET-NeuralGraph 3D", "Plataforma Cognitiva Desktop", "MAPFRE & NTT DATA", "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_preview_neuralgraph.png")

