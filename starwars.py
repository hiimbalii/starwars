import turtle


# funkciók majd ide
def balra():
    ship.setx(ship.xcor()-20)


def jobbra():
    ship.setx(ship.xcor()+20)


def fel():
    ship.sety(ship.ycor()+20)


def le():
    ship.sety(ship.ycor()-20)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("images/space.png")
space.addshape("images/sprite.gif")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.listen()

ship = turtle.Turtle()
ship.shape("images/sprite.gif")

while True:

    space.update()
