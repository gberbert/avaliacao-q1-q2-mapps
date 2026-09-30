import os
from PIL import Image, ImageDraw, ImageFont

# Assets
ntt_path = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_nttdata.png"
mapfre_path = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_mapfre.png"

img_ntt = Image.open(ntt_path).convert("RGBA")
img_mapfre = Image.open(mapfre_path).convert("RGBA")

# Font helpers
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 46)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
    font_tag = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
    font_lead = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
    font_btn = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
except:
    font_title = font_sub = font_tag = font_lead = font_btn = ImageFont.load_default()

def create_stacked_capsule(c_w, c_h, target_w):
    # White rounded capsule containing NTT on top, divider, MAPFRE on bottom
    cap = Image.new("RGBA", (c_w, c_h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(cap)
    
    h_n = int(target_w * img_ntt.size[1] / img_ntt.size[0])
    h_m = int(target_w * img_mapfre.size[1] / img_mapfre.size[0])
    
    r_ntt = img_ntt.resize((target_w, h_n), Image.Resampling.LANCZOS)
    r_map = img_mapfre.resize((target_w, h_m), Image.Resampling.LANCZOS)
    
    # NTT on top
    y_n = int((c_h / 2 - h_n) / 2) + 8
    x_n = int((c_w - target_w) / 2)
    cap.paste(r_ntt, (x_n, y_n), r_ntt)
    
    # Divider
    draw.line([(30, int(c_h / 2)), (c_w - 30, int(c_h / 2))], fill=(203, 213, 225, 255), width=2)
    
    # MAPFRE on bottom
    y_m = int(c_h / 2 + (c_h / 2 - h_m) / 2) - 8
    x_m = int((c_w - target_w) / 2)
    cap.paste(r_map, (x_m, y_m), r_map)
    
    return cap

# 1. Generate 800x800 Square Preview (Perfect for Teams / WhatsApp 1:1 box)
def make_square_og(product_name, subtitle, badge_text, out_path, bg_glow_color):
    sq = Image.new("RGBA", (800, 800), (7, 10, 19, 255))
    draw = ImageDraw.Draw(sq)
    
    # Outer subtle glow border
    draw.rounded_rectangle([(16, 16), (784, 784)], radius=36, outline=(0, 102, 255, 180), width=4)
    
    # Top Tag Badge
    badge_box = [(220, 50), (580, 96)]
    draw.rounded_rectangle(badge_box, radius=24, fill=(0, 102, 255, 40), outline=(0, 192, 243, 200), width=2)
    draw.text((250, 62), badge_text, fill=(0, 192, 243, 255), font=font_tag)
    
    # Stacked Capsule in Center (width 560, height 360)
    cap = create_stacked_capsule(560, 360, 420)
    sq.paste(cap, (120, 130))
    
    # Subtle frame around capsule
    draw.rounded_rectangle([(118, 128), (682, 492)], radius=24, outline=(0, 192, 243, 100), width=3)
    
    # Product Name & Subtitle
    # Calculate text position
    draw.text((400, 550), product_name, fill=(255, 255, 255, 255), font=font_title, anchor="mm")
    draw.text((400, 615), subtitle, fill=(148, 163, 184, 255), font=font_sub, anchor="mm")
    
    # Footer governance line
    draw.text((400, 710), "AS - MAPPS Brasil  •  NTT DATA & MAPFRE", fill=(0, 192, 243, 220), font=font_lead, anchor="mm")
    
    sq.save(out_path, "PNG")
    print("Created Square OG:", out_path)

# 2. Generate 1200x630 Standard OpenGraph Banner (Facebook, LinkedIn, Twitter, Teams wide)
def make_banner_og(product_name, subtitle, lead_desc, out_path):
    og = Image.new("RGBA", (1200, 630), (7, 10, 19, 255))
    draw = ImageDraw.Draw(og)
    
    # Accent top line
    draw.rectangle([(0, 0), (1200, 6)], fill=(0, 102, 255, 255))
    
    # Stacked Capsule on Left (380 x 420)
    cap = create_stacked_capsule(380, 420, 300)
    og.paste(cap, (80, 105))
    draw.rounded_rectangle([(78, 103), (462, 527)], radius=20, outline=(0, 102, 255, 140), width=3)
    
    # Right Side Content
    # Badge
    draw.rounded_rectangle([(520, 110), (960, 150)], radius=20, fill=(0, 102, 255, 40), outline=(0, 192, 243, 180), width=2)
    draw.text((540, 120), "APRESENTAÇÃO EXECUTIVA OFICIAL", fill=(0, 192, 243, 255), font=font_tag)
    
    # Title
    draw.text((520, 180), product_name, fill=(255, 255, 255, 255), font=font_title)
    
    # Subtitle
    draw.text((520, 250), subtitle, fill=(0, 192, 243, 255), font=font_sub)
    
    # Lead description
    draw.text((520, 320), lead_desc, fill=(148, 163, 184, 255), font=font_lead)
    
    # Leadership badge card at bottom right
    draw.rounded_rectangle([(520, 430), (1120, 520)], radius=14, fill=(15, 23, 42, 220), outline=(255, 255, 255, 30), width=1)
    draw.text((545, 450), "LIDERANÇA & GOVERNANÇA: AS - MAPPS BRASIL", fill=(255, 255, 255, 255), font=font_tag)
    draw.text((545, 480), "Leandro Bruzzese  |  Gustavo Costa Berbert  |  Marcio Miguel", fill=(148, 163, 184, 255), font=font_lead)
    
    og.save(out_path, "PNG")
    print("Created Banner OG:", out_path)

# Build for ACDC
make_square_og(
    "ACDC Platform",
    "Cockpit Actuarial e Inteligencia Artificial",
    "MAPFRE & NTT DATA",
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_square_acdc.png",
    (0, 102, 255)
)
make_banner_og(
    "ACDC Platform",
    "Cockpit de Configuración Actuarial e IA",
    "Modernización de la Capa MongoDB (DUP y RTE Tronador)\ncon Gobernanza PECA e IA Generativa Especializada.",
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_preview_acdc.png"
)

# Build for NeuralGraph
make_square_og(
    "AXET-NeuralGraph 3D",
    "Plataforma Cognitiva Desktop (Reef.core)",
    "MAPFRE & NTT DATA",
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_square_neuralgraph.png",
    (0, 192, 243)
)
make_banner_og(
    "AXET-NeuralGraph 3D",
    "Plataforma Cognitiva Desktop & Grafo 3D",
    "RAG Local-First Estricto, Neuroplasticidad en Tiempo Real,\nMalla Encefálica WebGL a 60 FPS y Cero Fuga de Datos.",
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/og_preview_neuralgraph.png"
)

