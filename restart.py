from turtle import Turtle

class Restart(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(280,-280)
        self.hideturtle()
        self.write("Click Here to Restart", align='center', font=("Arial", 18, 'bold'))

    def setup(self):
        self.showturtle()

    def is_clicked(self, x, y):
        button_left = self.xcor() - 100
        button_right = self.xcor() + 100
        buttton_top = self.ycor() + 20
        button_bottom = self.ycor() - 20
        if button_left <= x <= button_right and button_bottom <= y <= buttton_top:
            return True
        return False
    
