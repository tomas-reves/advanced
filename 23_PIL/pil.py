from PIL import Image
import glob

# im = Image.open("random_logo_1.png")
# box = (0, 28, 128, 100)
# region = im.crop(box)
# region.save('random_logo_cropped.png')
#
#
# im = Image.open("random_logo_cropped.png")
# im.show()

input_catalog = input("Paste path to photo gallery:")

image_list = []
for filename in glob.glob(input_catalog):
    im=Image.open(filename)
    image_list.append(im)

print(image_list)
