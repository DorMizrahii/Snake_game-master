from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-0, 265)

    def display_score(self):
        file = open(file="high_score.txt")
        self.clear()
        self.high_score = file.read()
        self.high_score = int(self.high_score)
        if self.score > self.high_score:
            self.update_file_score()
            self.high_score = self.score
        style = ('Courier', 15, 'italic')
        self.write(f"Score: {self.score} || High score: {self.high_score}", font=style, align='center')
        self.score += 1
        file.close()

    def update_file_score(self):
        file = open(file="high_score.txt", mode="w")
        file.write(str(self.score))
        file.close()


