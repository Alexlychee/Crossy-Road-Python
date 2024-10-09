from idlelib.multicall import MC_ENTER
from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_HUD = (-200, 260)


class Scoreboard(Turtle):
    """
    A scoreboard that keeps track of which level the user is on.
    Every time the turtle player does a successful crossing, the level should increase.
    When the turtle hits a car, GAME OVER should be displayed in the centre.
    """
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(LEVEL_HUD)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def new_level(self):
        self.score += 1
        self.update_scoreboard()

