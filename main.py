from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
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
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(right_paddle.position()) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(left_paddle.position()) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    #Detect collision with scoring zone
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.restart()

screen.exitonclick()