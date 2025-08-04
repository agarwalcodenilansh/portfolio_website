from PIL import Image, ImageEnhance

# Load images
profile = Image.open('profile.jpg').convert('RGBA').resize((600, 600))
watermark = Image.open('watermark.png').convert('RGBA').resize((600, 600))

# Fade the watermark further for subtlety
wm_faded = watermark.copy()
alpha = wm_faded.split()[3]
alpha = ImageEnhance.Brightness(alpha).enhance(0.4)  # 40% opacity
wm_faded.putalpha(alpha)

# Composite: watermark as background, profile on top
composite = Image.alpha_composite(wm_faded, profile)

# Save result
composite.save('profile_with_watermark.png')
print('Created profile_with_watermark.png with watermark background.') 