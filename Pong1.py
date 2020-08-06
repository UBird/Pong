# Simple Pong in Python 3

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle Modifiers
Awidth = 5
Bwidth = 5

#Score
scoreA = 0
scoreB = 0

#Paddle A 
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=Awidth, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

#Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=Bwidth, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))



#Functions
def paddleA_up():
    y = paddleA.ycor()
    y +=30
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -=30
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y +=30
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -=30
    paddleB.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350  and (ball.ycor() < paddleB.ycor() + (8 * Bwidth) and ball.ycor() > paddleB.ycor() - (8 * Bwidth)):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350  and (ball.ycor() < paddleA.ycor() + (8 * Awidth) and ball.ycor() > paddleA.ycor() - (8 * Awidth)):
        ball.setx(-340)
        ball.dx *= -1

    #Paddle modifications
    if(scoreA > scoreB +4 and Bwidth == 5):
        Bwidth += 2
        paddleB.shapesize(stretch_wid=Bwidth, stretch_len=1)
    
    if(scoreB > scoreA +4 and Awidth == 5):
        Awidth +=2
        paddleA.shapesize(stretch_wid=Awidth, stretch_len=1)

    if(scoreA <= scoreB +4 and Bwidth > 5):
        Bwidth -= 2
        paddleB.shapesize(stretch_wid=Bwidth, stretch_len=1)
    
    if(scoreB <= scoreA +4 and Awidth > 5):
        Awidth -= 2
        paddleA.shapesize(stretch_wid=Awidth, stretch_len=1)