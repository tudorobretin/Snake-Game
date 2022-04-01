from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.listen()
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(lambda: snake.up(screen), "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.01)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        score.update()
        snake.extend()
        snake.speed_increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for segment in snake.squares_list[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()
