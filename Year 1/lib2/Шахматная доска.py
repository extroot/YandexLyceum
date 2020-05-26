from PIL import Image, ImageDraw


def board(num, size):
    new_color = (255, 255, 255)
    new_image = Image.new("RGB", (size * num, size * num,), new_color)
    x = size * num
    y = x
    draw = ImageDraw.Draw(new_image)
    for i in range(0, x, size):
        if i % (size * 2) == 0:
            for j in range(0, y, size):
                if j % (size * 2) == 0:
                    draw.rectangle([i, j, i + size - 1, j + size - 1], fill='black')
        else:
            for j in range(size, y, size):
                if j % (size * 2) != 0:
                    draw.rectangle([i, j, i + size - 1, j + size - 1], fill='black')
    new_image.save('res.png', "PNG")
