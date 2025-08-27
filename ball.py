from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.direction = [1, 1]
        self.move_speed = 0.1

    def move(self):
        newxcor = self.xcor() + (10 * self.direction[0])
        newycor = self.ycor() + (10 * self.direction[1])
        self.goto(newxcor, newycor)

    def bounce_x(self):
        self.direction[0] *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.direction[1] *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
