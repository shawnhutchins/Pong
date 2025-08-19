from turtle import Turtle

STRETCH_WIDTH = 1
STRETCH_HEIGHT = 5
SPEED = 20

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(350, 0)
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_HEIGHT, outline=0)

    def move_up(self):
        self.forward(SPEED)

    def move_down(self):
        self.back(SPEED)