from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format) #JPEG
print(img.size)#(640, 640)
print(img.mode)#RGB
print(dir(img))#we get all methods, functions what we can use

#we can have filtered image
filtered_img = img.filter(ImageFilter.BLUR) #we can use SMOOTH or SHARPEN
filtered_img.save('blur.png', 'png') #so saved a new imaage under the name of blur.png which has been blured
#we can convert the image
filtered_img1 = img.convert('L')
filtered_img1.save('grey.png', 'png')

# filtered_img.show() #this can show the image on our screen
crooked = filtered_img1.rotate(90)
crooked.save('grey.png', 'png')
#resize
resize = filtered_img1.resize((300, 300))
resize.save('grey.png', 'png')

#crop
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('blur.png', 'png')

#astro image
img1 = Image.open('./astro.jpg')
print(img1.size)
# new_img = img1.resize((400, 200))
# new_img.save('thumbnail.jpg')
#to keep the aspect ratio
img1.thumbnail((400, 200))
img1.save('thumbnail.jpg')
