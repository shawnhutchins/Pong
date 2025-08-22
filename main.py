from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()