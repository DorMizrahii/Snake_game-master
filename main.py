import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

scoreboard.display_score()

screen.listen()

screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.left, key="Left")


def mistake(text):
    screen.clear()
    screen.tracer(0)
    turtle.color("black")
    style = ('Courier', 25, 'italic')
    turtle.write(text, font=style, align='center')
    turtle.penup()
    turtle.goto(snake.mistake_coordinates())
    turtle.color("red")
    turtle.shape("circle")
    screen.update()


game_is_on = True
while game_is_on:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.display_score()
        snake.extend()
    elif not snake.out_of_bound():
        game_is_on = False
        mistake("You've lost! out of bound!\U0001F62A ")

    elif snake.is_touching():
        game_is_on = False
        mistake("You've lost! you collided with yourself!\U0001F62A ")

    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
