from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        score_str = "score:" + str(self.score) + " | High Score: " + str(self.high_score)
        self.clear()
        self.write(score_str, align="center", font=("Arial", 18))
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score - 1
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    def over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 18))
