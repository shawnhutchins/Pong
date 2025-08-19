from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.onkeypress(fun=paddle1.move_up, key="Up")
screen.onkeypress(fun=paddle1.move_down, key="Down")

screen.onkeypress(fun=paddle2.move_up, key="w")
screen.onkeypress(fun=paddle2.move_down, key="s")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()