from PIL import Image


def twist_image(input_ﬁle_name, output_ﬁle_name):
    im = Image.open(input_ﬁle_name)
    x, y = im.size
    out = Image.new('RGB', (x, y), (0, 0, 0))
    half1 = im.crop((0, 0, x // 2, y))
    half2 = im.crop((x // 2, 0, x, y))
    out.paste(half1, (x // 2, 0))
    out.paste(half2, (0, 0))
    out.save(output_ﬁle_name)
