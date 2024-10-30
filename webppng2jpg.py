import os
from PIL import Image

def convert_images_in_folder(folder_path):
    # run all in the folder
    for entry in os.listdir(folder_path):
        entry_path = os.path.join(folder_path, entry)

        if os.path.isdir(entry_path):  # if we find a folder, open it and do again
            convert_images_in_folder(entry_path)
        elif os.path.isfile(entry_path):  # if we find a file
            if entry.lower().endswith(('.webp', '.png')):  # find the WEBP and PNG
                # open the file and change
                with Image.open(entry_path) as img:
                    # create the path of the JPG file
                    jpg_path = os.path.splitext(entry_path)[0] + '.jpg'
                    # change and save as JPG
                    img.convert('RGB').save(jpg_path, 'JPEG')

                # delete the WEBP nad PNG
                os.remove(entry_path)
                print(f'Converted: "{entry_path}" to "{jpg_path}" and deleted the original file.')

# 获setting for the path of the first folder (the example is the folder of this file.py)
initial_folder = os.path.dirname(os.path.abspath(__file__))
convert_images_in_folder(initial_folder)

print('HAVE CHANGED ALL FILES TO JPG')
