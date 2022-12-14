from PIL import Image
from os import listdir
from os.path import isfile, join

TELEGRAM_MAX_SIZE = 512
INPUT_PATH = 'images'
OUTPUT_PATH = 'stickers'


def make_path(path):
    return '/'.join(path)


def upsize(image):
    width = image.size[0]
    height = image.size[1]
    ratio = width/height
    if width > height:
        new_size = (TELEGRAM_MAX_SIZE, TELEGRAM_MAX_SIZE/ratio)
    else:
        new_size = (TELEGRAM_MAX_SIZE*ratio, TELEGRAM_MAX_SIZE)
    image.resize(new_size)


def downsize(image):
    image.thumbnail((TELEGRAM_MAX_SIZE, TELEGRAM_MAX_SIZE))


def resize(name):
    image = Image.open(make_path([INPUT_PATH, name]))
    print(f'----------------')
    print(f'Starting image {name}')
    if image.size[0] >= TELEGRAM_MAX_SIZE or image.size[1] >= TELEGRAM_MAX_SIZE:
        print(f'Downsizing image')
        downsize(image)
    else:
        print(f'Upsizing image')
        upsize(image)
    image.save(make_path([OUTPUT_PATH, name]), quality=20, optimize=True)
    print(f'Saved')


def fetch_files():
    return [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]


if __name__ == '__main__':
    files = fetch_files()
    print(f'Found {len(files)} files')
    for file in files:
        resize(file)
