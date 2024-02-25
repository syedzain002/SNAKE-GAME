import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        self.speed("fastest")
        self.color("blue")
        random_x=random.randint(-250,250)
        random_y=random.randint(-250,250)
        self.goto(random_x,random_y)
        self.clear()

    def get_food(self):
        self.clear()
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)



