from PIL import Image
import numpy as np
from conv import *

def convolutePictureRGB(path, kernel:np.ndarray):
    image = np.asarray(Image.open(path))
    sh = image.shape
    image = np.moveaxis(image, -1, 0)
    output = [np.zeros(1),np.zeros(1),np.zeros(1)]
    for colorChannel in range(len(image)):
        print(f"Calculating Channel {colorChannel}\n")
        output[colorChannel] = convolve2D(image[colorChannel], kernel)
        #output[colorChannel] = np.zeros((1087, 1918))
        print("Calcualtion done\n")
    output = np.moveaxis(np.asarray(output),0,-1)
    output = np.asarray(output)
    print(sh)
    print(output.shape)
    output = Image.fromarray(np.uint8(output))
    output.save("src/Outputs/Img.bmp", "BMP")

convolutePictureRGB("src/img.jpg",list2)