#----------------------------------------------------------------------
#SIMPLE PONG IN PYTHON 
#My First Game
#----------------------------------------------------------------------


#“Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it!
#works good for basic games
import turtle
import winsound

wn= turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width= 800, height=600)
wn.tracer(0)                         #stops the window from updating, so we have to manually do it

#Score
score_A=0
score_B=0


#Paddle A
paddle_A =turtle.Turtle() #turtle=module name, Turtle=class name
paddle_A.speed(0)         #speed of animation--> sets the speed to the max possible speed
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()          #as turtle module draw lines
paddle_A.goto(-350,0)     #paddle to start from x= -350, y = 0--> 0,0 is the center of the screen

#paddles are 20 pixels wide and 100 pixels tall

#Paddle B
paddle_B =turtle.Turtle() 
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("blue")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)


#Ball
ball =turtle.Turtle() 
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
max_dx = 6
max_dy = 6
ball.goto(0,0)

ball.dx=0.1             #everytime the ball moves it will move by 0.1 pixels
ball.dy=-0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)            #animation speed = 0 not object speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))



#----------------------------------------------------------------------
#FUNCTIONS
#----------------------------------------------------------------------

#Paddle A Commands
def paddle_A_up ():
    y=paddle_A.ycor()        #ycor () returns the y coordinate
    y +=20                   #as we go up y increases and as we go down y decreases
    paddle_A.sety(y)

def paddle_A_down ():
    y=paddle_A.ycor() 
    y -=20                   #everytime paddle_a moves down, it will move by 20 pixels
    paddle_A.sety(y)

#Paddle B Commands
def paddle_B_up ():
    y=paddle_B.ycor() 
    y +=20
    paddle_B.sety(y)

def paddle_B_down ():
    y=paddle_B.ycor() 
    y -=20
    paddle_B.sety(y)



#----------------------------------------------------------------------
#Keybord binding
#----------------------------------------------------------------------
wn.listen()                         #commands to listen to the keyboard input

#Paddle A inputs
wn.onkeypress(paddle_A_up, "w")     #on pressing w paddle_a_up function gets called
wn.onkeypress(paddle_A_down, "s")

#Paddle B inputs
wn.onkeypress(paddle_B_up, "Up")
wn.onkeypress(paddle_B_down, "Down")


#----------------------------------------------------------------------
#MAIN GAME LOOP
#----------------------------------------------------------------------
while True:
    wn.update()                 # everytime the loop runs it updates the screen

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1           # reverses the direction of the ball
       # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)      # winsound.SND_ASYNC used to avoid lag while the sound plays
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1  
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_A +=1         #if ball goes to the right player a scores
        pen.clear()         #clears the  screen before updating the new score
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))   #updation of scores on screen

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_B +=1
        pen.clear() 
        pen.write("Player A: {}   Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350):
        if ball.ycor() < paddle_B.ycor() + 40 and ball.ycor() > paddle_B.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1 #-1.1  # increase speed each time we hit the ball

    if (ball.xcor() < -340 and ball.xcor() > -350):
        if ball.ycor() < paddle_A.ycor() + 40 and ball.ycor() > paddle_A.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1 #-1.1  # increase speed each time we hit the ball


    