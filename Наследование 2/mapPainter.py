from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.sort = sorted(set([y for x in draw_map for y in x]))
        self.d = {x: "black" for x in self.sort}
        self.sort = sorted(set([y for x in draw_map for y in x]))

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


dr = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20)
dr.d = {1: 'black', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'lightblue', 7: 'blue', 8: 'violet', 9: 'white'}
print(dr.numbers())
print(dr.draw())
