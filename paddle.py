from turtle import Turtle

class Paddel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.speed(0)

    def go_right(self):
        x = self.xcor()
        if x < 350:
            x += 20
        self.setx(x) 

    def go_left(self):
        x = self.xcor()
        if x > -350:
            x -= 20
        self.setx(x)
    
    def reset_position(self):
        self.goto((0, -260))