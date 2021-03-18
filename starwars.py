import turtle


# funkciók majd ide


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("images/space.png")
space.addshape("images/sprite.gif")
space.onkeypress(balra, "Left")

ship = turtle.Turtle()
ship.shape("images/sprite.gif")

while True:

    space.update()
