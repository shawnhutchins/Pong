from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.position = (0, 0)
        self.goto(self.position)

    def move_ball(self):
        newx = self.position[0] + 1
        newy = self.position[1] + 1
        self.position = (newx, newy)
        self.goto(self.position)
