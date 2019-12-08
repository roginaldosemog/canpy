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

# center image
def imageToImage(position, image, background):
    img_w, img_h = image.size
    bg_w, bg_h = background.size
    offset = getPositionFeed(position, bg_w, bg_h, img_w, img_h)
    background.paste(image, offset, image)
    return background

# Adiciona texto à imagem
def textToImage(position, image, text, size, color, font):
    img_w, img_h = image.size
    font = ImageFont.truetype('src/fonts/Montserrat/{}.ttf'.format(font), size=size)
    w,h = font.getsize(text)
    draw = ImageDraw.Draw(image)
    draw.text(getPositionFeed(position, img_w, img_h, w, h), text, font=font, fill=color)
    return image

# Abre a imagem na aplicação padrão do sistema
def showImage(image):
    image.show()

# Salva a imagem na pasta img
def saveImage(image, name, extension):
    image.save('img/' + name, extension)

# Funções que retornam posicionamento de imagem
def getPositionFeed(mode, img_w, img_h, width, height):
    if (mode == 'top-left'):
        return (44, 44)
    elif (mode == 'top-center'):
        return (((img_w-width)//2), 44)
    elif (mode == 'top-right'):
        return (((img_w-width)-44), 44)
    elif (mode == 'center-left'):
        return (44, (img_h-height)//2)
    elif (mode == 'center'):
        return (((img_w-width)//2), (img_h-height)//2)
    elif (mode == 'center-right'):
        return (((img_w-width)-44), (img_h-height)//2)
    elif (mode == 'bottom-left'):
        return (44, (img_h-height)-44)
    elif (mode == 'bottom-center'):
        return (((img_w-width)//2), (img_h-height)-44)
    elif (mode == 'bottom-right'):
        return (((img_w-width)-44), (img_h-height)-44)
    else:
        return ((img_w-width)//2, (img_h-height)//2)

# Código teste
if __name__ == "__main__":
    # feed = createImage(WIDTH, FEED_HEIGHT, '#406040')
    feed = loadImage('img/background.jpg')
    logo = loadImage('img/logo.png')
    logo = resizeImage(logo, 96, 96) # TODO: aspect-ratio && transparency
    feed = imageToImage('bottom-center', logo, feed)
    feed = textToImage('center', feed, 'UMIC MOOVE', 120, 'white', 'Montserrat-Bold')
    saveImage(feed, 'feed.png', 'JPEG')
    feed = resizeImage(feed, 512, 512)
    showImage(feed)