from turtle import Turtle

BALL_SPEED = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.direction = [1, 1]

    # noinspection SpellCheckingInspection
    def move(self):
        newxcor = self.xcor() + (BALL_SPEED * self.direction[0])
        newycor = self.ycor() + (BALL_SPEED * self.direction[1])
        self.goto(newxcor, newycor)

    def bounce(self):
        self.direction[1] *= -1
