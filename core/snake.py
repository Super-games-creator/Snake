from .conf import INI_SNAKE_LEN, CW, CH
from .helper import get_x, get_y


class Snake:
    def __init__(self, canvas):  # это конструктор класса
        self.canvas = canvas  # это поле класса
        self.hx = 10
        self.hy = 10
        self.cells = []  # пустой массив для змеи
        self.snake_len = INI_SNAKE_LEN
        self.d = 1  # направление

    def draw_head(self, cx, cy):
        x = get_x(cx)
        y = get_y(cy)
        self.canvas.create_rectangle(x, y, x + CW, y + CH, fill="green", tag="head")

    def draw_cell(self, cx, cy):
        x = get_x(cx)
        y = get_y(cy)
        self.canvas.create_rectangle(x, y, x + CW, y + CH, fill="pale green", tag=f"cell{cx}x{cy}")

    def hide_head(self):
        self.canvas.delete("head")

    def hide_cell(self, cx, cy):
        self.canvas.delete(f"cell{cx}x{cy}")

    def in_snake(self, cx, cy):
        for fx, fy in self.cells:
            if (fx, fy) == (cx, cy):
                return True
        return False
