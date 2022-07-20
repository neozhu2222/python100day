from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("my snake game")


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "up")
screen.onkey(snake.left, "left")
screen.onkey(snake.down, "down")
screen.onkey(snake.right, "right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.placed()
        scoreboard.increase_score()
        snake.extend()

    if snake.segments[0].xcor > 280 or snake.segments[0].xcor < -280 or snake.segments[0].ycor > 280 or snake.segments[0].ycor < -280:
        scoreboard.game_over()
        game_on = False

    for s in snake.segments:
        if s == snake.position[0]:
            pass
        elif snake.position[0].distance(s) < 10:
            game_on = False
            scoreboard.game_over()
