from PIL import Image, ImageDraw


def fruits(size, bg_color, *houses):
    im = Image.new("RGB", size, bg_color)
    drawer = ImageDraw.Draw(im)
    for house in houses:
        x, y, r = house
        color = (((r * 123) % 256), ((r * 123) % 256), ((r * 123) % 256))
        drawer.ellipse(((x - r, y - r), (x + r, y + r)), fill=color)
    return im
