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
    def move_ball(self):
        if self.ycor() > 270 or self.ycor() < -270:
            self.direction[1] *= -1
        newxcor = self.xcor() + (BALL_SPEED * self.direction[0])
        newycor = self.ycor() + (BALL_SPEED * self.direction[1])
        self.goto(newxcor, newycor)


