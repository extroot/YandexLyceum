from PIL import Image


def transparency(ﬁlename1, ﬁlename2):
    im1 = Image.open(ﬁlename1)
    im2 = Image.open(ﬁlename2)
    pixels1 = im1.load()
    pixels2 = im2.load()

    x, y = im1.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels1[i, j]
            r1, g1, b1 = pixels2[i, j]
            pixels1[i, j] = int(0.5 * r + 0.5 * r1), int(0.5 * g + 0.5 * g1), int(0.5 * b + 0.5 * b1)
    im1.save('res.jpg')
