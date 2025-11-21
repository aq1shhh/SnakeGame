from turtle import Turtle
from snake import Snake


class Score(Turtle):
    def __init__(self):

        super().__init__()
        self.update = 0
        self.color("white")
        self.penup()
        self.highscore=0
        self.goto(0, 220)

        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.update}, High Score {self.highscore}", align="center", font=("Verdana", 15, "normal"))

    def increase_score(self):
        self.update+=1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.color("white")
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Arial", 30, "normal"))


    def reset(self):
        if self.update>self.highscore:
            self.highscore=self.update
            with open("data.txt",mode="w") as file:
                file.write(f"{self.highscore}")
        self.update=0
        self.update_scoreboard()




