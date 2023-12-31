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
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.go_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()


    #Detect turtle collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    #Detect successful crossing
    if player.is_at_the_end():
        player.reset_position()
        car_manager.level_up()
        score_board.new_level()


screen.exitonclick()

