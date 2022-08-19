#Creating a pong game in python using Turtle Module

import turtle #using the turtle module for graphics
import winsound 

#Creating the basic output screen
wn = turtle.Screen()
wn.title("Pong Game By Tulip Aggarwal")
wn.bgcolor("Yellow")
wn.setup(width=800, height=600)
wn.tracer(0)

#Creating Bar-1
bar1 = turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("black")
bar1.shapesize(stretch_wid=5, stretch_len=1)
bar1.penup()
bar1.goto(-350,0)

#Creating Bar-2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("black")
bar2.shapesize(stretch_wid=5, stretch_len=1)
bar2.penup()
bar2.goto(350,0)

#Creating the Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25

#The score calculate function
score1 = 0
score2 = 0

#The score display function
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 16, "normal"))

#Functions for moving the paddles up and down
def bar1_up():
    y = bar1.ycor()
    y +=20
    bar1.sety(y)

def bar1_down():
    y = bar1.ycor()
    y -=20
    bar1.sety(y)

def bar2_up():
    y = bar2.ycor()
    y +=20
    bar2.sety(y)

def bar2_down():
    y = bar2.ycor()
    y -=20
    bar2.sety(y)

#Keyboard winding
wn.listen()
wn.onkeypress(bar1_up, "w")
wn.onkeypress(bar1_down,"s")
wn.onkeypress(bar2_up, "Up")
wn.onkeypress(bar2_down,"Down")

#Main game loop
while True:
    wn.update()

#Moving the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 

#Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1  
    

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1 
        score1 +=1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

    if ball.xcor()<-390:
        ball.setx(390)
        ball.dx *= -1 
        score2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

#Bar and ball collision
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor() < bar2.ycor() + 40 and ball.ycor()>bar2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)
    
    if ball.xcor() < -340 and ball.xcor()> -350 and (ball.ycor() < bar1.ycor() + 40 and ball.ycor()>bar1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)