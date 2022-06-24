from turtle import Turtle

FONT = ("Arial",50,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()            
        self.penup()
        self.goto(-100, 200)
        self.score_1 = 0
        self.score_2 = 0
        self.write(self.score_1, align="center",font=FONT)
        self.goto(100,200)
        self.write(self.score_2, align="center", font= FONT)
        
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_1, align="center",font=FONT)
        self.goto(100,200)
        self.write(self.score_2, align="center", font= FONT)
