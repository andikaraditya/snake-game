from turtle import Turtle, Screen
from snakes import Snakes
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600) 
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snakes()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.reset()
        # scoreboard.game_over()
        # break

    #Collision with body
    for i in snake.body[1:]:
        if snake.head.distance(i) < 10:
            snake.reset()
            scoreboard.reset()
            # scoreboard.game_over()
            # break
    # else:
    #     continue
    # break



screen.exitonclick()