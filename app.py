from turtle import Turtle, Screen

# Create the screen
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off screen updates

# Paddle class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -260)
        self.speed(0)  # Set the paddle's animation speed to the maximum

    def move_left(self):
        x = self.xcor()
        if x > -350:
            x -= 20
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        if x < 350:
            x += 20
        self.setx(x)

# Ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.speed(0)  # Set the ball's animation speed to the maximum
        self.dx = 3  # Ball's x-axis movement speed
        self.dy = -3  # Ball's y-axis movement speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

# Brick class
class Brick(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(x, y)

# Create paddle, ball, and bricks
paddle = Paddle()
ball = Ball()

bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
brick_rows = 5
brick_columns = 10
brick_width = 70
brick_height = 20
brick_start_x = -350
brick_start_y = 250

for row in range(brick_rows):
    for column in range(brick_columns):
        brick_x = brick_start_x + column * (brick_width + 10)
        brick_y = brick_start_y - row * (brick_height + 10)
        brick_color = colors[row % len(colors)]
        brick = Brick(brick_color, brick_x, brick_y)
        bricks.append(brick)

# Keyboard bindings
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

# Game loop
game_on = True
while game_on:
    screen.update()  # Update the screen

    ball.move()

    # Check for collision with the walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()

    # Check for collision with the paddle
    if (ball.ycor() < -250) and (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):
        ball.bounce_y()

    # Check for collision with bricks
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.goto(1000, 1000)  # Move the brick off-screen
            bricks.remove(brick)  # Remove the brick from the list
            ball.bounce_y()

    # Check for game over
    if ball.ycor() < -300:
        game_on = False

# Game over message
game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.goto(0, 0)
game_over.hideturtle()
game_over.write("Game Over", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
