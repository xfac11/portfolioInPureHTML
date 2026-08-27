from PIL import Image
import os
p = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')
p = os.path.normpath(p)
for fname in sorted(os.listdir(p)):
    if not fname.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        continue
    path = os.path.join(p, fname)
    try:
        with Image.open(path) as im:
            print(fname, im.width, 'x', im.height, '-', os.path.getsize(path), 'bytes')
    except Exception as e:
        print('ERR', fname, e)
