from turtle import Turtle

class Brick(Turtle):
    def __init__(self,colors, x, y):
        super().__init__()
        self.shape('square')
        self.color(colors)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(x,y)