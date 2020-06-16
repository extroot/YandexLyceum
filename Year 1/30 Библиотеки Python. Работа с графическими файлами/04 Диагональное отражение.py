from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    pixels = im.load()
    x, y = im.size
    for j in range(y):
        for i in range(x - j):
            pixels[j, i], pixels[x - 1 - i, x - 1 - j] = pixels[x - 1 - i, x - 1 - j], pixels[j, i]
    im.save('res.jpg')
