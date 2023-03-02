import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


timmy = Player()
screen.listen()
screen.onkey(timmy.move_forward,"Up")
car = CarManager()
score = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for i in car.cars:
        if timmy.distance(i) < 25:
            timmy.goto(0,0)
            timmy.write("GAME OVER", move=False, align='center', font=("Courier", 20, "bold"))
            game_is_on = False
    score.create_level()
    if timmy.ycor() == 280:
        timmy.goto(0, -280)
        score.increase_level()


screen.exitonclick()       
            
            
       
