from turtle import Screen, Turtle
from paddle import Paddel
from ball import Ball
from bricks import Brick
import random
import time

screen = Screen()
screen.bgcolor('lightblue')
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)


paddle = Paddel((0, -260))
ball = Ball((0, -230))

# create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
brick_rows = 5
brick_columns = 10
brick_width = 65
brick_height = 20
brick_start_x = -350
brick_start_y = 250

for row in range(brick_rows):
    row_colors = random.choices(colors, k=brick_columns)
    for column, color in enumerate(row_colors):
        brick_x = brick_start_x + column * (brick_width + 10)
        brick_y = brick_start_y - row * (brick_height + 10)
        brick = Brick(color, brick_x, brick_y)
        bricks.append(brick)

# create lives
lives = 3
life_turtles = []
life_pos_x = -330
life_pos_y = -270

for l in range(lives):
    life =  Turtle()
    life.shape("turtle")
    life.setheading(90)
    life.color('red')
    life.penup()
    life.goto(life_pos_x, life_pos_y)
    life_turtles.append(life)
    life_pos_x += 30

#keybord setting 
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

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
    if (ball.ycor() < -250) and (paddle.xcor() - 30 < ball.xcor() < paddle.xcor() + 30):
        ball.bounce_y()

    # ball misses the paddel
    if ball.ycor() < -300:
        ball.reset_position()
        paddle.reset_position()
        lives -= 1
        life_turtles[lives].hideturtle()
    
        if lives == 0:
            game_is_on = False
            ball.reset_position()

    # collision with brcks
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.bounce_y()

screen.exitonclick()