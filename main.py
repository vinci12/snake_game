from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
game_on = True
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Sanke Game")


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on=False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            score.game_over()

    
        
        









screen.exitonclick()