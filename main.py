import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()






"""
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.
"""