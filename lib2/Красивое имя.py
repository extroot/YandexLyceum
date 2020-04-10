from PIL import Image, ImageDraw

text = ["------------------------------",
        "-00000---0---00000-00000---0--",
        "-0---0--0-0--0---0-0------0-0-",
        "-0---0--000--0000--00000-0---0",
        "-0---0-00-00-0---0-0-----0---0",
        "-0---0-0---0-00000-00000-0---0",
        "------------------------------"]

im = Image.new("RGB", (len(text[0]) * 30, len(text) * 30), (255, 255, 255))
draw = ImageDraw.Draw(im)

for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] == '-':
            continue
        draw.ellipse(((30 * j, 30 * i), (30 * j + 30, 30 * i + 30)), (255, 1, 1))
im.save("out.jpg")
