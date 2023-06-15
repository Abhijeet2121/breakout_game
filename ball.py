from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.shape('circle')
        self.penup()
        self.speed(0)
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.1
        self.goto(position)

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.goto(0, -240)
        self.move_speed =0.1
        self.bounce_y()