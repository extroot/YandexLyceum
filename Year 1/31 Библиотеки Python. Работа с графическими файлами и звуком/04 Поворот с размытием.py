from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open("image.jpg")
    im2 = im.transpose(Image.ROTATE_270)
    im2 = im2.filter(ImageFilter.GaussianBlur(radius=n))
    im2.save('res.jpg')


motion_blur(10)
