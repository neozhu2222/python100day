from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
turtle = Turtle()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()
paddle = Turtle()
paddle.penup()
paddle.goto(350,0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_win=5, stretch_len=1)


rp = Paddle((350, 0))
lp = Paddle((-350, 0))
ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(rp) < 50 and ball.xcor > 320 or ball.distance(lp) < 50 and ball.xcor < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.r()
        scoreboard.lp
    if ball.xcor() < -380:
        ball.r()
        scoreboard.rp


screen.onkey(rp.go_up, "up")
screen.onkey(rp.go_down, "down")

screen.onkey(lp.go_up, "w")
screen.onkey(lp.go_down, "s")


screen.exitonclick()