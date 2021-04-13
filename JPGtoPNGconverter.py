import sys
import os
from PIL import Image

#grab first (Pokedex) and second (new folder) arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)
#after these we can write in terminal: python  JPGtoPNGconverter.py Pokedex/ new/
# we get back: Pokedex/ new/

#check if new folder exist if not, create it
if not os.path.exists(output_folder):
  os.makedirs(output_folder)

#loop trough Pokedex and convert imagaes to PNG
for filname in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filname}')
  clean_name = os.path.splitext(filname)[0]
  # print(clean_name)
  img.save(f'{output_folder}{clean_name}.png', 'png')
  print('all done!')

#save them to the new folder