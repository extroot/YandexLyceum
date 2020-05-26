from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.sort = sorted(set([y for x in draw_map for y in x]))
        self.d = {x: "black" for x in self.sort}

    def set_color(self, number, color):
        self.d[number] = color

    def size(self):
        return len(self.draw_map) * self.cell_size, len(self.draw_map[0]) * self.cell_size

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def numbers(self):
        return self.sort

    def draw(self):
        im = Image.new("RGB", self.size(), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        for i in range(len(self.draw_map)):
            for j in range(len(self.draw_map[i])):
                draw.rectangle(((i * self.cell_size, j * self.cell_size),
                                (i * self.cell_size + self.cell_size,
                                 j * self.cell_size + self.cell_size)), self.d[self.draw_map[i][j]])
        return im


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