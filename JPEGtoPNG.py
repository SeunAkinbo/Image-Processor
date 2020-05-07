import os
import sys
from PIL import Image


# old_file_path = '/Users/mac/PycharmProjects/imageProcessing/venv/Pokedex'
# new_file_path = '/Users/mac/PycharmProjects/imageProcessing/venv/newPokedex'

old_file_path = sys.argv[1]
new_file_path = sys.argv[2]

# Gets a System argument sys.argv from the terminal
# 1. Containing the file name
# 2. The directory of the source images
# 3. The directory where the images will be stored


if not os.path.exists(new_file_path):
    os.makedirs(new_file_path)
# Verifies if the new directory exists, and creates one if it doesn't


try:
    with os.scandir(old_file_path) as entries:
        for entry in entries:
            if os.path.isfile(entry):
                file = entry.name
                new_file = file.strip('.jpg') + '.png'
                base_fp = os.path.join(old_file_path, file)
                with Image.open(base_fp) as img:
                    new_fp = os.path.join(new_file_path, new_file)
                    if img.format == 'JPEG':
                        img.save(new_fp, 'png')
except IOError as err:
    print(f'The filepath is incorrect - {err}')
