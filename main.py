import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
carmanager = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.go_up, "up")


player = Player()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.at_finish():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()



