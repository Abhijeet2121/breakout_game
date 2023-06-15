from turtle import Turtle

class Life(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color('red')
        self.penup()
        self.goto(x , y)

    def hide(self):
        self.hideturtle()

        