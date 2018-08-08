import os
import math
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")
wn.bgpic("first.gif")
score =0

turtle.register_shape("player1.gif")
turtle.register_shape("enemy1.gif")
border_pen=turtle.Turtle()

border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("green")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.penup()




#player
player=turtle.Turtle()
player.color("blue")
player.penup()
player.shape("player1.gif")

player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playermove =15 #speed
gunstate="ready"

#move left
def move_left():
    x=player.xcor()
    x=x-playermove
    if x<-280:
        x=-280

    player.setx(x)

def move_right():
    x=player.xcor()
    x=x+playermove
    if x>280:
        x=280
    player.setx(x)

def fire_gun():
    global gunstate

    if gunstate=="ready":

        gunstate="fire"

        x=player.xcor()
        y=player.ycor()
        gun.setposition(x, y+10)
        gun.showturtle()


def iscollison(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance< 15:
        return True
    else:
        return False





#keyboard binding
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_gun,"space")



enemyspeed =2
total_enemies=5

enemies=[]
for i in range(total_enemies):
    enemies.append(turtle.Turtle())
    # crete enemy
for enemy in enemies:

    enemy.color("red")
    enemy.shapesize(1.9, 2.9)
    enemy.shape("enemy1.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(-200, 250)
    enemy.setposition(x,y)

gun=turtle.Turtle()
gun.color("red")
gun.shape("triangle")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(1.5, 1.5)
gun.hideturtle()

gunspeed=20

gunstate="ready"


#main game
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x = x + enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:

                y = e.ycor()
                y = y - 40
                e.sety(y)

            enemyspeed *= -1


        if enemy.xcor() < -280:

            for f in enemies:

                y = f.ycor()
                y = y - 40
                f.sety(y)
            enemyspeed *= -1

        if iscollison(gun, enemy):

            gun.hideturtle()
            gunstate = "ready"
            gun.setposition(0, -300)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(-200, 250)
            score=score+30
            scorestring="score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))





    if gunstate == "fire":
        y = gun.ycor()
        y = y + gunspeed
        gun.sety(y)

    if gun.ycor() > 275:
            gun.hideturtle()
            gunstate = "ready"




delay=input('eneter')
