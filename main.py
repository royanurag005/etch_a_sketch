import turtle
from turtle import Turtle,Screen
timmy=Turtle()
screen=Screen()
def move_fwd():
    timmy.forward(10)
def move_bwd():
    timmy.back(10)
def move_lft():
    new_direction=timmy.heading()+10
    timmy.setheading(new_direction)
    # timmy.setheading()
def move_rt():
    new_direction=timmy.heading()-10
    timmy.setheading(new_direction)

# def clr():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
def clear():
    turtle.resetscreen()


screen.listen()

screen.onkey(fun=move_fwd,key="w")
#In this case the move_fwd function is not called but is rather passed as argument

screen.onkey(fun=move_bwd,key="s")
screen.onkey(fun=move_rt,key="d")
screen.onkey(fun=move_lft,key="a")
screen.onkey(fun=clear,key="c")
# screen.onkey(fun=clr,key="Escape")


screen.exitonclick()
