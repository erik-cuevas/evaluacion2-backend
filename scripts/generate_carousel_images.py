"""Script auxiliar para generar variantes responsivas del carrusel.

Este script toma tres imágenes fuente (en market/static/market/) y genera
versiones PNG y WebP en tres tamaños (800, 1280, 1920). Utiliza Pillow para
hacer fit/crop y guardar imágenes optimizadas.

Ejemplo de uso (desde la raíz del repo):
python scripts/generate_carousel_images.py

Nota: este script es auxiliar y no se ejecuta en tiempo de ejecución de Django.
"""

from PIL import Image, ImageOps
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / 'market' / 'static' / 'market'

mapping = [
    ('gestionrapidacarrusel.png', 'slide1'),
    ('interfazseguracarrusel.png', 'slide2'),
    ('responsivecarrusel.png', 'slide3'),
]

sizes = [ (800,450), (1280,720), (1920,1080) ]

def ensure_rgb(img: Image.Image) -> Image.Image:
    if img.mode in ('RGBA', 'LA'):
        bg = Image.new('RGB', img.size, (255,255,255))
        bg.paste(img, mask=img.split()[-1])
        return bg
    return img.convert('RGB')

def main():
    print('Base path:', BASE)
    for src_name, dst_prefix in mapping:
        src = BASE / src_name
        if not src.exists():
            print('Source not found:', src)
            continue
        with Image.open(src) as im:
            for w,h in sizes:
                print(f'Processing {src_name} -> {dst_prefix}-{w}.png')
                # crop/fit to target aspect and size
                img = ImageOps.fit(im, (w,h), Image.LANCZOS)
                img = ensure_rgb(img)
                out_png = BASE / f'{dst_prefix}-{w}.png'
                out_webp = BASE / f'{dst_prefix}-{w}.webp'
                img.save(out_png, format='PNG', optimize=True)
                # save webp
                img.save(out_webp, format='WEBP', quality=85)
    print('Done.')

if __name__ == '__main__':
    main()
