import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()

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

screen.exitonclick()


# TODOS


"""
Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
When this happens, return the turtle to the starting position and increase the speed of the cars. 
Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.
"""

"""
Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. 
hen the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
"""