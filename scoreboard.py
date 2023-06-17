from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscores = int(data.read())
        self.color('black')
        self.penup()
        self.goto(-270, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscores}", align = 'center', font=('Arial', 20, 'bold'))

    def increace_score(self):
        self.score += 10
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscores:
            self.highscores = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscores}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align='center', font=("Arial", 24, 'bold'))
