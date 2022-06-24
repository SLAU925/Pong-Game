from hashlib import new
from turtle import Turtle, pos

STARTING_POS = [(0,20),(0,0),(0,-20)]

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position,0)
    
    def up(self):
        self.goto(self.position,self.ycor()+20)

    def down(self):
        self.goto(self.position,self.ycor()-20)

