from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.update_level()

    def update_level(self):
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def upper_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="Game over!", align="center", font=FONT)

