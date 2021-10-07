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

    return pixel_values
    #return newPixValues

#create a new image just using a range from a previous image
def create_image_range(pix_values):
    new_img_array = []
    for rgb in pix_values:
        if rgb[0] > 200 and rgb[0] < 230:
            new_img_array.append(rgb)

    array = np.array(new_img_array, dtype=np.uint8)
    print(array)
    img = Image.fromarray(array)
    img.save("./new_image.png")  



#random_img('./random.png', 50, 150)
image = pixel_info("random.png")
create_image_range(image)



