from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

    def move_ball(self):
        newx = self.xcor() + 10
        newy = self.ycor() + 10
        self.goto(newx, newy)

