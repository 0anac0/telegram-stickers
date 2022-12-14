from PIL import Image
from os import listdir
from os.path import isfile, join

TELEGRAM_MAX_SIZE = 512
INPUT_PATH = 'images'
OUTPUT_PATH = 'stickers'


def make_path(path):
    return '/'.join(path)


def resize(name):
    image = Image.open(make_path([INPUT_PATH, name]))
    image.thumbnail((TELEGRAM_MAX_SIZE, TELEGRAM_MAX_SIZE))
    image.save(make_path([OUTPUT_PATH, name]), quality=20, optimize=True)
    print(f'Saved {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def fetch_files():
    return [f for f in listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]


if __name__ == '__main__':
    files = fetch_files()
    print(f'Found {len(files)} files')
    for file in files:
        resize(file)
