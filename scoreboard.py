import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.new_game()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.write(f"Game Over\nScore: {self.score}", align=ALIGNMENT, font=FONT)
        self.new_game()

    def new_game(self):
        self.clear()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score: {self.score} | Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)