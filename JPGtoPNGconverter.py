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

#loop trough Pokedex and convert imagaes to PNG

#save them to the new folder