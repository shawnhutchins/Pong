from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle = Paddle()

screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()