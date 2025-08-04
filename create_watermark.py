from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Load and process the profile image
img = Image.open('profile.jpg').convert('L').resize((600, 600))
img = img.convert('RGBA')

# Create a transparent overlay for the watermark text
watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(watermark)

# Try to use a system font, fallback to default if not found
try:
    font = ImageFont.truetype('arial.ttf', 48)
except:
    font = ImageFont.load_default()

text = 'Nilansh Agarwal'
# Use textbbox for accurate text size
bbox = draw.textbbox((0, 0), text, font=font)
textwidth = bbox[2] - bbox[0]
textheight = bbox[3] - bbox[1]

# Position text in the center
x = (img.width - textwidth) // 2
y = (img.height - textheight) // 2 + 120

# Draw the text with semi-transparent white
text_color = (255, 255, 255, 80)  # 80/255 ~ 30% opacity
draw.text((x, y), text, font=font, fill=text_color)

# Combine the watermark with the image
watermarked = Image.alpha_composite(img, watermark)

# Optionally, fade the whole image for a more subtle watermark effect
alpha = watermarked.split()[3]
alpha = ImageEnhance.Brightness(alpha).enhance(0.7)
watermarked.putalpha(alpha)

# Save as PNG to preserve transparency
watermarked.save('watermark.png')
print('Watermark image saved as watermark.png') 