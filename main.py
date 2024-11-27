from turtle import Turtle, Screen
import random
screen = Screen()
is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color (red, green, blue, yellow, orange, purple): ")
print(user_bet)

all_turtles = []

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [150, 100, 50, 0, -50, -100, -150]

for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color[i])
        new_turtle.penup()
        new_turtle.goto(x= -240, y = y[i])
        all_turtles.append(new_turtle)
        
print(new_turtle)

if user_bet:
        is_race_on = True

while is_race_on:
        
        for turtle in all_turtles:
                if turtle.xcor() > 230:
                        is_race_on = False
                        winning_color = turtle.pencolor()
                        if winning_color == user_bet:
                                print(f"You won! The {winning_color} turtle is the winner.")
                        else:
                                print(f"You loose! The {winning_color} turtle is the winner.")
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)


  
screen.exitonclick()