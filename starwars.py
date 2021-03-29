import turtle
from random import randint
from time import sleep
from datetime import datetime, timedelta
import simpleaudio as sa

# funkciók majd ide


def balra():
    ship.setx(ship.xcor()-20)


def jobbra():
    ship.setx(ship.xcor()+20)


def fel():
    ship.sety(ship.ycor()+20)


def le():
    ship.sety(ship.ycor()-20)


def move_meteors():
    for one_meteor in meteors:
        if one_meteor.xcor() < -400:
            one_meteor.setx(400)
            one_meteor.sety(randint(-280, 280))
        one_meteor.setx(one_meteor.xcor()-10)


def add_meteor():
    new_meteor = turtle.Turtle()
    new_meteor.shape("images/meteor2.gif")
    new_meteor.penup()
    new_meteor.setx(400)
    meteors.append(new_meteor)


def roll_new_time():
    curr_time = datetime.now()
    seconds = randint(5, 30)
    roll_new_time.next_meteor_time = curr_time + timedelta(seconds=seconds)


def kiX():
    newX = round(ship.xcor() / 400, 0) * -400
    ship.setx(newX)


def kiY():
    newY = round(ship.ycor() / 300, 0) * -300
    ship.sety(newY)


def eletek():
    lives.clear()
    hearts = "❤"*life
    lives.write(f"{hearts}", font=("Arial", 35, "bold"), align="center")


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("images/space.png")
space.addshape("images/sprite.gif")
space.addshape("images/meteor2.gif")
space.addshape("images/rocket.gif")
# audio importalasa
# használat: explosion.play() ez async, ha sync kell akkor a .wait_done()-t mögé lehet írni, de nem fontos
# ha a while trueba rakjátok be bugos
explosion = sa.WaveObject.from_wave_file("sounds/explosion-01.wav")

space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.tracer(0)
space.listen()

ship = turtle.Turtle()
ship.shape("images/sprite.gif")
ship.penup()

meteors = []
add_meteor()

life = 3
lives = turtle.Turtle()
lives.hideturtle()
lives.color("red")
lives.goto(-250, 240)
lives.clear()
eletek()

roll_new_time()

while True:
    if abs(ship.xcor()) > 420:
        kiX()
    if abs(ship.ycor()) > 300:
        kiY()
    for meteor in meteors:
        if(ship.distance(meteor.xcor(), meteor.ycor()) < 50):
            meteor.goto(-500, 0)
            life -= 1
            explosion.play()
            eletek()
    move_meteors()
    if datetime.now() >= roll_new_time.next_meteor_time:
        add_meteor()
        roll_new_time()
    space.update()
    sleep(0.05)
