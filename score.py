from turtle import Turtle
class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 20, "bold"), align = "center")


    def game_over(self):
        self.clear()
        self.write(f"GAME OVER", font=("Arial", 20, "bold"), align = "center")

    def increase_score(self):
        self.score += 1
        self.update_score()
