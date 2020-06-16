from PIL import Image


def make_preview(size, n_colors):
    im = Image.open("image.jpg")
    im2 = im.resize(size)
    im2 = im2.quantize(n_colors)
    im2.save('res.bmp')
