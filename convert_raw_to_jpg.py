from PIL import Image
from pathlib import Path


for p in Path('./raw').iterdir():
    img = Image.open(p)
    new_size = [x // 10 for x in img.size]
    img.resize(new_size).save(f'img/{p.stem}.small.jpg')
