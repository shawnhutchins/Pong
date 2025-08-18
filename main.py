from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")

paddle = Paddle()

screen.exitonclick()