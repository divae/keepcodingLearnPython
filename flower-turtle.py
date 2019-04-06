import turtle

def square(side):
    angle = 90
    myTurle.forward(side)
    myTurle.left(angle)
    myTurle.forward(side)
    myTurle.left(angle)
    myTurle.forward(side)
    myTurle.left(angle)
    myTurle.forward(side)
    myTurle.left(angle)
    myTurle.left(angle)

def paint_flower():
    side = 10
    for incremental_value in range(0, 13):
        square(side)
        side += incremental_value

    
myTurle = turtle.Turtle()

paint_flower()