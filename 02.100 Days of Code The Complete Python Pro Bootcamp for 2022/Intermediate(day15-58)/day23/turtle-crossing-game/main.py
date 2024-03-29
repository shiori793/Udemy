import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
loop = 1
while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    loop += 1
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.check_finish():
        player.got_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
