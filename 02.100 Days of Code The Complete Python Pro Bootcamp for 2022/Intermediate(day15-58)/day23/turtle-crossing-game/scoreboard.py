from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-250, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)