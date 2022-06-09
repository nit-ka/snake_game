from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

scoreboard.start_message()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def start_game():
    game_is_on = True
    scoreboard.clear()
    scoreboard.show_score()
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 18:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            game_is_on = False
            scoreboard.game_over_message()

        # Detect collision with the tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over_message()


screen.onkey(start_game, "space")

screen.exitonclick()
