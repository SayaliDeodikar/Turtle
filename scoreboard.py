from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

    def create_level(self):
        self.hideturtle()
        self.penup()
        self.goto(-230,230)
        self.clear()
        self.write(f"Level:{self.level}", move=False, font=FONT)


    def increase_level(self):
        self.level += 1
        self.create_level()
    
        
            
            
            