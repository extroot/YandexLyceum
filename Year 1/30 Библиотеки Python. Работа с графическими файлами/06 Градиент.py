from PIL import Image, ImageDraw


def gradient(color):
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (512, 200), new_color)
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512):
        if color.upper() == "R":
            draw.line((i, 0, i, 200), fill=(int(i / 2), 0, 0), width=1)
        elif color.upper() == "G":
            draw.line((i, 0, i, 200), fill=(0, int(i / 2), 0), width=1)
        else:
            draw.line((i, 0, i, 200), fill=(0, 0, int(i / 2)), width=1)
    new_image.save('res.png', "PNG")
