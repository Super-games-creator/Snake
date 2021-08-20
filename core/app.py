import tkinter as tk
import sched
import time
from .conf import W, COLS, H, INI_SNAKE_LEN, ROWS
from .board import Board
from .snake import Snake


class App:
    def __init__(self):
        self.window = tk.Tk()  # названия модуля.имя класса(с большой буквы)
        self.window.title("Snake2")
        self.canvas = tk.Canvas(self.window, width=W, height=H)
        self.canvas.pack()
        self.s = sched.scheduler(time.time, time.sleep)  # название модуля.имя функции(с маленькой буквы)
        self.restart = tk.IntVar()  # для рестарта
        self.s = sched.scheduler(time.time, time.sleep)  # название модуля.имя функции(с маленькой буквы)
        self.board = Board(self.canvas)
        self.snake = Snake(self.canvas)
        self.close = False

    def on_key(self, event):
        if self.snake.d != 2:
            if event.keysym == "Right":  # условия
                self.snake.d = 1
        if self.snake.d != 1:
            if event.keysym == "Left":
                self.snake.d = 2
        if self.snake.d != 4:
            if event.keysym == "Down":
                self.snake.d = 3
        if self.snake.d != 3:
            if event.keysym == "Up":
                self.snake.d = 4

    def on_closing(self):
        self.restart.set(1)  # это для сброса окна рестарта
        if self.close:
            self.window.quit()
        self.close = True

    def restart_game(self):
        for cx, cy in self.snake.cells:  # для каждого элемента массива
            self.snake.hide_cell(cx, cy)
        for fx, fy in self.board.food:  # для каждого элемента массива
            self.board.hide_food(fx, fy)
        self.board.food = []
        self.snake.cells = []
        self.snake.snake_len = INI_SNAKE_LEN
        hx = 10
        hy = 10
        self.snake.d = 1
        self.board.draw_panel()
        self.snake.draw_head(hx, hy)
        self.board.generate_food(5)

    def on_time(self):

        self.snake.hide_head()
        self.snake.draw_cell(self.snake.hx, self.snake.hy)
        self.snake.cells.append((self.snake.hx, self.snake.hy))  # добавляем в конец массива
        if len(self.snake.cells) > self.snake.snake_len:  # проверяем хвост змии
            cx, cy = self.snake.cells[0]  # взять из массива первый элемент
            del self.snake.cells[0]  # удалить из массива первый элемент(0)
            self.snake.hide_cell(cx, cy)
        if self.snake.d == 1:
            self.snake.hx = (self.snake.hx + 1) % COLS
        if self.snake.d == 2:
            self.snake.hx = (self.snake.hx - 1) % COLS
        if self.snake.d == 3:
            self.snake.hy = (self.snake.hy + 1) % ROWS
        if self.snake.d == 4:
            self.snake.hy = (self.snake.hy - 1) % ROWS
        self.board.draw_panel()

        self.snake.draw_head(self.snake.hx, self.snake.hy)
        # домашнее задания
        n = self.snake.in_snake(self.snake.hx, self.snake.hy)
        if n:  # проверяем змейку
            self.board.game_over(self.window)
            self.restart_game()
        n = self.board.in_food(self.snake.hx, self.snake.hy)
        if n >= 0:  # проверяем еду
            self.snake.snake_len += 2
            self.board.add_score(2)
            fx, fy = self.board.food[n]
            self.board.hide_food(fx, fy)
            self.board.draw_panel()
            del self.board.food[n]
            self.board.add_food()

        self.window.update()
        if not self.close:
            self.s.enter(0.2, 1, self.on_time)  # для продолжения анимации

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.bind('<Key>', self.on_key)
        self.board.draw()
        self.board.generate_food(5)
        self.board.draw_panel()
        # window.mainloop()
        self.s.enter(0.2, 1, self.on_time)  # для движения
        self.s.run()  # для движения
