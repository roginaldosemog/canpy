#!/usr/bin/python3

from PIL import Image, ImageFont, ImageDraw
import sys

WIDTH = 1080
FEED_HEIGHT = 1080
STORIES_HEIGHT = 1920

# Cria uma imagem
def createImage(width, height, color):
    image = Image.new('RGB', (width, height), color)
    return image

# Carrega uma imagem
def loadImage(directory):
    try:
        image = Image.open(directory)
        
    except IOError:
        print("loadImage: Unable to load image")    
        sys.exit(1)

    return image

# Redimensiona a imagem
def resizeImage(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

# Abre a imagem na aplicação padrão do sistema
def showImage(image):
    image.show()

# Salva a imagem na pasta img
def saveImage(image, name, extension):
    image.save('img/' + name, extension)

# center image
def imageToImage(image, background):
    img_w, img_h = image.size
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(image, offset, image)
    return background

# Adiciona texto à imagem
def textToImage(image, text, size, color):
    img_w, img_h = image.size
    font = ImageFont.truetype('src/fonts/Montserrat/Montserrat-Bold.ttf', size=size)
    w,h = font.getsize(text)
    draw = ImageDraw.Draw(image)
    draw.text(((img_w-w)/2, (img_h-h)/2), text, font=font, fill=color)
    return image

# Código teste
if __name__ == "__main__":
    feed = createImage(WIDTH, FEED_HEIGHT, '#406040')
    # feed = loadImage('img/background.jpg')
    logo = loadImage('img/logo.png')
    feed = imageToImage(logo, feed)
    feed = textToImage(feed, 'UMIC MOOVE', 120, 'white')
    saveImage(feed, 'feed.png', 'JPEG')
    feed = resizeImage(feed, 512, 512)
    showImage(feed)