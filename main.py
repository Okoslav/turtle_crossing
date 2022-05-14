import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard()

player = Player()
car_manager = CarManager()


screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # hráč úspěšně dorazil na konec silnice
    if player.is_at_finish():
        player.restart_level()
        car_manager.move_faster()
        score.upper_level()

    # hráč narazil do auta
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False






screen.exitonclick()