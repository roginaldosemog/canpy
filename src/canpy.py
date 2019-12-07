#!/usr/bin/python3

from PIL import Image, ImageFilter
import sys

def loadImage(directory):
    try:
        image = Image.open(directory)
        
    except IOError:
        print("loadImage: Unable to load image")    
        sys.exit(1)

    return image

def resizeImage(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

def showImage(image):
    image.show()

if __name__ == "__main__":
    art = loadImage('img/background.jpg')
    art = resizeImage(art, 512, 512)
    showImage(art)