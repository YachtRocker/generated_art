from PIL import Image, ImageFilter
import numpy as np

#creates a random pixel picture
def random_img(output, width, height):

    #array = np.random.random_integers(0,255, (height,width,3))  
    array = np.random.randint(0,255, (height,width,3))
    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(array)
    #img = img.filter(ImageFilter.SMOOTH)
    img.save(output)

# returns the pixel information  
def pixel_info(input):
    img = Image.open(input, 'r')
    width, height = img.size

    pixel_values = list(img.getdata())
    newPixValues = np.array(pixel_values)  #converts list to array

    #return pixel_values
    return newPixValues

#create a new image just using a range from a previous image
def create_image_range(pix_values):
    for rgb in pix_values:
        if rbg[0] > 200 and rgb[0] < 230:
            print(rgb)

#random_img('random3.png', 50, 150)
image = pixel_info("random.png")
print(image)
