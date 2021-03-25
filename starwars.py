import turtle
from random import randint
from time import sleep


# funkciók majd ide
def balra():
    ship.setx(ship.xcor()-20)


def jobbra():
    ship.setx(ship.xcor()+20)


def fel():
    ship.sety(ship.ycor()+20)


def le():
    ship.sety(ship.ycor()-20)


def move_meteor():
    if meteor.xcor() < -400:
        meteor.setx(400)
        meteor.sety(randint(-280, 280))
    meteor.setx(meteor.xcor()-10)


def kiX():
    newX = round(ship.xcor() / 400, 0) * -400
    ship.setx(newX)


def kiY():
    newY = round(ship.ycor() / 300, 0) * -300
    ship.sety(newY)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("images/space.png")
space.addshape("images/sprite.gif")
space.addshape("images/meteor2.gif")

space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")

space.tracer(0)
space.listen()

ship = turtle.Turtle()
ship.shape("images/sprite.gif")
ship.penup()

meteor = turtle.Turtle()
meteor.shape("images/meteor2.gif")
meteor.penup()
meteor.setx(400)

while True:
    if abs(ship.xcor()) > 420:
        kiX()
    if abs(ship.ycor()) > 300:
        kiY()
    move_meteor()
    space.update()
    sleep(0.05)
