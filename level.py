from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(330, 270)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=("Arial", 20, 'bold'))

    def increase_level(self):
        self.level +=1
        self.update_level()
        