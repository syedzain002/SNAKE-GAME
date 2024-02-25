from turtle import Turtle

ANGLES = [270,180,90,360]
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.width=600
        self.height=600
        self.hideturtle()
        self.color("red")
        self.pensize(5)
        self.starting_point=(self.height/2,self.width/2)
        self.penup()
        self.goto(self.starting_point)
        self.pendown()
        for _ in ANGLES:
            self.setheading(_)
            if _ == 270 or _ == 90:
                self.forward(self.height)
            elif _ == 180 or _ == 360:
                self.forward(self.width)

