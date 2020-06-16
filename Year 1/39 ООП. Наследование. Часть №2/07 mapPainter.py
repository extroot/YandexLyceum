from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.d = dict(map(
            lambda x: (x, 'black'),
            set.union(*map(set, self.draw_map))
        ))
        self.cell_size = cell_size

    def numbers(self):
        res = set()
        for row in self.draw_map:
            res |= set(row)
        return sorted(res)

    def set_color(self, number, color):
        self.d[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        return tuple(map(
            lambda x: len(x) * self.cell_size,
            (
                self.draw_map[0],
                self.draw_map
            )
        ))

    def draw(self):
        img = Image.new('RGB', self.size(), 'black')
        draw = ImageDraw.Draw(img)
        for j, row in enumerate(self.draw_map):
            for i, cell in enumerate(row):
                x, y = map(lambda k: k * self.cell_size, (i, j))
                draw.rectangle(
                    (x, y, x + self.cell_size, y + self.cell_size),
                    fill=self.d[cell]
                )
        return img
