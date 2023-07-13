import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision of snake with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.update_score()
        snake.grow()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        sb.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            sb.game_over()
            game_is_on = False

screen.exitonclick()
