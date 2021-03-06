import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
# add a new segment to the snake.
        snake.extend()
# create a scoreboard
        scoreboard.increase_score()
# detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
# detect collision with on tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
