from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, brickrow, color):
        self.canvas = canvas
        self.hit_bottom = False
        self.paddle = paddle
        self.brickrow = brickrow
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width= self.canvas.winfo_width()

    def draw(self):
        # self.canvas.move(self.id, 0, -1)
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        print(self.canvas.coords(self.id))
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

        for brick in brickrow:
            if not brick.destroyed() and self.hit_brick(brick, pos) == True:
                self.y = 3
                brick.destroy()

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos [2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_brick(self, brick, pos):
        brick_pos = self.canvas.coords(brick.id)
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[3] <= brick_pos[3]:
                return True
        return False


class Brick:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        starts = ['green', 'purple', 'cyan', 'pink', 'black']
        random.shuffle(starts)
        self.id = canvas.create_rectangle(0, 0, 35, 35, fill=starts[0])
        self.canvas.move(self.id, x, y)
        self.is_destroyed = False
        self.x = starts[0]

    def destroyed(self):
        return self.is_destroyed

    def destroy(self):
        canvas.delete(self.id)
        self.is_destroyed = True


class Paddle:
    def __init__(self, canvas, color):
        self.canvas =canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width= self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)





    def turn_left(self, evt):
        self.x = -5

    def turn_right(self, evt):
        self.x = 5

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

tk = Tk()
tk.title("game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", )
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')

brickrow = []

for i in range(1,11):
    brick = Brick(canvas,5+(40*i),20)
    brickrow.append(brick)

for i in range(1,11):
    brick = Brick(canvas,5+(40*i),75)


    brickrow.append(brick)



ball = Ball(canvas, paddle, brickrow, 'red')

while 1:
    if ball.hit_bottom == True:
        ball = Ball(canvas, paddle, brickrow, 'red')

    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)






