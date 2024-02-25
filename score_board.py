from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.SCORE_COUNT = 0
        #self.score_update()
        self.write(f"Score: {self.SCORE_COUNT}", move=False, align='center', font=('Arial', 15, 'normal'))


    def score_update(self):
        self.SCORE_COUNT += 1
        self.clear()
        self.write(f"Score: {self.SCORE_COUNT}", move=False, align='center', font=('Arial', 15, 'normal'))