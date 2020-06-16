from PIL import ImageDraw
# 1: 2:34:40
# 2: 2:31


class BeeImageDraw(ImageDraw.ImageDraw):
    def __init__(self, img):
        super().__init__(img)

    def bee(self, xy, fill):
        x, y, w, h = xy
        super().ellipse((
            (x + 3 * h // 5 - w // 2, y + h // 8),
            (x + 3 * h // 5 + w // 2, y + h + h // 8)),
            fill[0])
        super().ellipse((
            (x + 3 * h // 5 - h // 8, y),
            (x + 3 * h // 5 + h // 8, y + h // 4)),
            fill[1])
        super().polygon((
            (x, y + w),
            (x + h // 2, y + w),
            (x, y + w + h // 4)),
            fill[2])
        super().polygon((
            (x + 3 * h // 5 + 3 * h // 5, y + w),
            (x + 3 * h // 5 + 3 * h // 5, y + w + h // 4),
            (x + 3 * h // 5 + 3 * h // 5 - h // 2, y + w)),
            fill[2])


from PIL import Image

img = Image.new('RGB', (200, 200), '#000000')
drw = BeeImageDraw(img)
drw.bee((15, 10, 60, 140), ('#ffffff', '#999999', '#666666'))
img.save('result.png')