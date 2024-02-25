from turtle import Turtle,Screen
from snake import Snake
from Food import Food
from score_board import Score
from border import Border
import random
import time

def game_over():
    a = Turtle()
    a.color("white")
    a.hideturtle()
    a.penup()
    a.write(f"GAME OVER! \n YOUR SCORE: {score.SCORE_COUNT}", move=False, align='center', font=('Arial', 20, 'normal'))


screen = Screen()
screen.setup(width=700,height=700)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)
game_is_on = True

#declaring different elements of game
snake = Snake()
food = Food()
score = Score()
border= Border()

while game_is_on is True:
    screen.update()
    time.sleep(.1)
    snake.move()
    snake.update_cord()
    screen.listen()
    screen.onkey(key='Left', fun=snake.left)
    screen.onkey(key='Right', fun=snake.right)
    screen.onkey(key='Up', fun=snake.up)
    screen.onkey(key='Down', fun=snake.down)

    if snake.head.distance(food) < 15:
        food.get_food()
        snake.add_segment()
        score.score_update()
    head_cordinate=snake.head.pos()
    limit = 300
    if head_cordinate[0]>limit or head_cordinate[0]<(-limit) or head_cordinate[1] > limit or head_cordinate[1] < (-limit):
        game_over()
        game_is_on=False

    if snake.head.pos() in snake.segment_cordinates[1:]:
        game_over()
        game_is_on= False

screen.exitonclick()