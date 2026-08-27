from PIL import Image
import os

INPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')
INPUT_DIR = os.path.normpath(INPUT_DIR)
SIZES = [480, 800, 1200]

print('Image dir:', INPUT_DIR)

for fname in os.listdir(INPUT_DIR):
    if not fname.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        continue
    src_path = os.path.join(INPUT_DIR, fname)
    try:
        img = Image.open(src_path)
    except Exception as e:
        print('Skipping', fname, 'error:', e)
        continue
    basename, _ = os.path.splitext(fname)
    for w in SIZES:
        out_name = f"{basename}-{w}.jpg"
        out_path = os.path.join(INPUT_DIR, out_name)
        # Avoid upscaling: use min(w, img.width)
        new_w = min(w, img.width)
        new_h = int(img.height * new_w / img.width)
        try:
            rgb = img.convert('RGB')
            resized = rgb.resize((new_w, new_h), Image.LANCZOS)
            resized.save(out_path, quality=85)
            print('Wrote', out_name)
        except Exception as e:
            print('Failed to write', out_name, 'error:', e)

print('Done.')
