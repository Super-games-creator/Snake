import tkinter as tk
import random
from .conf import MX, MY, H_PANEL, W, ROWS, COLS, H
from .helper import get_x, get_y


class Board:
    def __init__(self, canvas):  # это конструктор класса
        self.canvas = canvas  # это поле класса
        self.food = []
        self.restart = tk.IntVar()  # для рестарта
        self.image = tk.PhotoImage(file="./images/apple.png")
        self.score = 0

    def draw(self):  # это метод класса
        self.canvas.create_rectangle(MX, MY, W - MX, H - MY, fill="light goldenrod", tag="board")

    def hide_food(self, cx, cy):
        self.canvas.delete(f"food{cx}x{cy}")

    def draw_food(self, cx, cy):
        x = get_x(cx)
        y = get_y(cy)
        # self.canvas.create_oval(x, y, x + CW, y + CH, fill="red", tag=f"food{cx}x{cy}")
        self.canvas.create_image(x, y, image=self.image, anchor=tk.NW, tag=f"food{cx}x{cy}")

    def draw_panel(self):
        self.canvas.delete("panel")
        self.canvas.create_rectangle(MX, MY, W - MX, H_PANEL, fill="gray", tag="panel")
        self.canvas.create_text(13 * MX, 4 * MY, text="SCORE:", font=("Arial", 20), anchor="e", tag="panel")
        self.canvas.create_text(15 * MX, 4 * MY, text=f"{self.score}", font=("Arial", 20), anchor="w", tag="panel")

    def game_over(self, window):
        self.canvas.create_rectangle(get_x(COLS // 2 - 15), get_y(ROWS // 2 - 6),
                                     get_x(COLS // 2 + 15), get_y(ROWS // 2 + 6), fill="gray", tag="game_over")
        self.canvas.create_rectangle(get_x(COLS // 2 - 14), get_y(ROWS // 2 - 5),
                                     get_x(COLS // 2 + 14), get_y(ROWS // 2 + 5), fill="lime", tag="game_over")
        self.canvas.create_text(get_x(COLS // 2), get_y(ROWS // 2 - 4),
                                text="!!GAME OVER!!", font=("Arial", 40), fill="red", anchor="c", tag="game_over")
        self.restart.set(0)  # подготовка к рестарту
        button = tk.Button(window, text="RESTART", width=150, height=60, fg="red", command=self.on_restart)
        button.place(relx=0.5, rely=0.5, anchor="c", width=130, height=50, )
        self.canvas.create_text(get_x(COLS // 2 + -10), get_y(ROWS // 2 + 3),
                                text="SCORE:", font=("Arial", 20), tag="game_over")
        self.canvas.create_text(get_x(COLS // 2 + -7), get_y(ROWS // 2 + 3),
                                text=f"{self.score}", font=("Arial", 20), anchor="w", tag="game_over")
        button.wait_variable(self.restart)  # ждём нажатия на кнопку
        button.destroy()
        self.canvas.delete("game_over")  # сотрём окно рестарта

    def on_restart(self):
        self.restart.set(1)

    def add_food(self):
        rx = random.randint(0, COLS - 1)
        ry = random.randint(0, ROWS - 1)
        self.draw_food(rx, ry)
        self.food.append((rx, ry))  # добавляем в конец массива

    def add_score(self, value):
        self.score += value
        self.draw_panel()

    def generate_food(self, n):
        for _ in range(n):
            self.add_food()

    def in_food(self, cx, cy):
        for n, (fx, fy) in enumerate(self.food):  # пронумеровать массив - enumerate
            if (fx, fy) == (cx, cy):
                return n
        return -1  # -1 значит не найдено
