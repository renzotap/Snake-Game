from turtle import Turtle
from food import Food
ALIGNMENT="center"
FONT=("Arial",22,"bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_n=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score ={self.score_n}", align=ALIGNMENT, font=FONT)


    def scored(self):
        self.score_n+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

