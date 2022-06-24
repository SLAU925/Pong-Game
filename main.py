from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Welcome to the 80's Pong Game")
screen.bgcolor("black")
screen.tracer(0)

player_1 = Paddle(350)
player_2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(player_1.up,"Up")
screen.onkeypress(player_1.down,"Down")
screen.onkeypress(player_2.up,"w")
screen.onkeypress(player_2.down,"s")

gameOver = False

while not gameOver:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()

    if((ball.distance(player_1)< 50 and ball.xcor()>320) or (ball.distance(player_2)< 50 and ball.xcor()<-320)):
        ball.change_direction()

    if(ball.xcor()>380):
        scoreboard.score_1 += 1
        scoreboard.update()
        ball.reset()
        ball.change_direction()

    if(ball.xcor()<-380):
        scoreboard.score_2 += 1
        scoreboard.update()
        ball.reset()
        ball.change_direction()



screen.exitonclick()
