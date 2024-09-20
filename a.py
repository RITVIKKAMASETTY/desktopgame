from turtle import Turtle,Screen
a=Turtle()
Screen=Screen()
a.speed("fastest")
def move1():
    a.forward(10)
def move2():
    a.backward(10)
def move3():
    c=a.heading()-10
    a.setheading(c)
def move4():
    b=a.heading()+10
    a.setheading(b)
def move5():
    a.clear()
    a.penup()
    a.home()
    a.pendown()
Screen.listen()
Screen.onkey(key="w",fun=move1)
Screen.onkey(key="s",fun=move2)
Screen.onkey(key="a",fun=move4)
Screen.onkey(key="d",fun=move3)
Screen.onkey(key="c",fun=move5)
Screen.exitonclick()
