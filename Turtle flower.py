import turtle 
import random

def circle (turtle):
    for i in range(30):
        turtle.forward(10)
        turtle.left(25)


def spiral(turtle):
    for i in range(100):
        turtle.forward(10)
        turtle.left(i)

def random_color(my_turtle):
    r = random.random()
    g = random.random()
    b = random.random()
    my_turtle.color(r,g,b)


def random_spirals(turtle):
    r = random.random()
    if r < 0.5:
        for i in range(100):
            turtle.forward(10)
            turtle.left(i)

    else:
        for i in range(50):
            turtle.forward(i)
            turtle.left(15)


def make_spirals(my_turtle):
    odie.forward(10)
    for i in range(13):
        size = random.randint(1, 10)
        random_color(my_turtle)
        my_turtle.pensize(size)
        random_spirals(odie)


def make_flower(t,func):
    petals = 7
    for i in range(petals):
        random_color(t)
        t.home()
        t.left(360/petals*i)
        t.forward(15)
        func(t)

if __name__ == '__main__':
    odie = turtle.Turtle()
    odie.shape('turtle')
    odie.speed(0)
    odie.hideturtle()
    make_flower(odie,spiral)
    make_flower(odie,circle)
    odie.showturtle()
    odie.home()
    turtle.exitonclick()





