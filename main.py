import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for cars in car_manager.all_cars:
        if player.distance(cars) < 25:
            game_is_on = False


    # Detect when the turtle player has reached the top edge of the screen.
    if player.ycor() > FINISH_LINE_Y:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.new_level()


screen.exitonclick()

