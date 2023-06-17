from turtle import Screen, Turtle
from paddle import Paddel
from ball import Ball
from bricks import Brick
from lifes import Life
from scoreboard import Scoreboard
from level import Level
from restart import Restart
import random
import time

# creates screen
screen = Screen()
screen.bgcolor('lightblue')
screen.setup(width=800, height=700)
screen.title("Breakout Game")
screen.tracer(0)

# create paddle
paddle = Paddel((0, -260))

# create ball
ball = Ball((0, -240))

# create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
brick_rows = 5
brick_columns = 10
brick_width = 65
brick_height = 20
brick_start_x = -350
brick_start_y = 250

# create lives
lives = 3
life_turtles = []
life_pos_x = -330
life_pos_y = -270

#  scoreboard 
scoreboard = Scoreboard()

# set initial levels
level = Level()

# creates restart button
# button = Restart()
# button.setup()

def create_bricks():
    for row in range(brick_rows):
        row_colors = random.choices(colors, k=brick_columns)
        for column, color in enumerate(row_colors):
            brick_x = brick_start_x + column * (brick_width + 10)
            brick_y = brick_start_y - row * (brick_height + 10)
            brick = Brick(color, brick_x, brick_y)
            bricks.append(brick)

for l in range(lives):
    life =  Life(life_pos_x, life_pos_y)
    life_turtles.append(life)
    life_pos_x += 30

#keybord setting
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

#create initial bricks
create_bricks()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle) < 22:
        print(paddle.distance(ball))
        ball.bounce_y()

    # collision with brcks
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            scoreboard.increace_score()
            ball.bounce_y()

    # ball misses the paddel
    if ball.ycor() < -300:
        ball.reset_position()
        paddle.reset_position()
        scoreboard.reset()
        lives -= 1
        life_turtles[lives].hideturtle()
    
        if lives == 0:
            game_is_on = False
            # button.showturtle()
            ball.reset_position()
            scoreboard.game_over()
            

    # check the bricks
    if len(bricks) == 0:
        level.increase_level()
        brick.clear()
        create_bricks()
        paddle.reset_position()
        ball.reset_position()
        ball.x_move *= 0.4
        ball.y_move *=0.4
    
    # Restart the game
    # if button.is_clicked:
    #     paddle.reset_position()
    #     ball.reset_position()
    #     ball.x_move = 3
    #     ball.y_move = 3
    #     ball.move_speed = 0

    #     for brick in bricks:
    #         brick.reset()

    #     for life in life_turtles:
    #         life.showturtle()

    #     button.hideturtle()
    #     game_is_on = True

screen.exitonclick()