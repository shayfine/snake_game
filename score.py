from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.my_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.my_score}", align="center", font=("Ariel", 24, "normal"))
        self.hideturtle()
        self.new_score()

    def new_score(self):
        self.clear()
        self.write(f"Score : {self.my_score} High Score : {self.high_score}", align="center", font=("Ariel", 24,
                                                                                                    "normal"))

    def reset(self):
        if self.my_score > self.high_score:
            self.high_score = self.my_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.my_score = 0
        self.new_score()

    def update(self):
        self.my_score += 1
        self.new_score()
