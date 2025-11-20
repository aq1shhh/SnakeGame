import turtle

from snake import Snake
from turtle import Screen
from Food import Food
import time
from Scoreboard import Score

screen=Screen()

screen.setup(height=500, width=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score = Score()
snake.create_snake()

screen.listen()
screen.onkey(key="Up", fun=snake.w)
screen.onkey(key="Down", fun=snake.s)
screen.onkey(key="Left", fun=snake.a)
screen.onkey(key="Right", fun=snake.d)


   








game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #detecting food cxolison
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detecting collision with the wall
    if snake.head.xcor()>243 or snake.head.xcor()<-243 or snake.head.ycor()>243 or snake.head.ycor()<-243:

        score.reset()
        snake.reset()

    #detecting with tail collison
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<15:
            game_is_on=False
            score.game_over()




screen.exitonclick()

