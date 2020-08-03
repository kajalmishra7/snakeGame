import turtle
import time
import random

delay=0.1
window = turtle.Screen()
window.title("Snake Game by rjl")
window.bgcolor("cyan")
window.setup(width = 600,height = 600)
window.tracer(0)
#turns of animation on the screen

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
#keep the pen up so that it does not draw anything
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
#keep the pen up so that it does not draw anything
food.goto(0,100)

#body
segments=[]

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
score=0
high_sc=0
pen.write("Score: {} High Score: {}".format(score,high_sc),align ="center",font=('Courier',20,'normal'))
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")

    
def move():
    if(head.direction == "up"):
       y = head.ycor()
       head.sety(y+20)
    if(head.direction == "down"):
       y = head.ycor()
       head.sety(y-20)
    if(head.direction == "left"):
       x = head.xcor()
       head.setx(x-20)
    if(head.direction == "right"):
       x = head.xcor()
       head.setx(x+20)
       
while True:
    window.update()
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction= "stop"
        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_sc),align ="center",font=('Courier',20,'normal'))

    if(head.distance(food)<20):
       #move food to another random spot
       x= random.randint(-290,290)
       y= random.randint(-290,290)
       food.goto(x,y)     
       
       new_segment=turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("yellow")
       new_segment.penup()
       segments.append(new_segment)

       
       score += 10
       if score>high_sc :
           high_sc = score
       pen.clear()
       pen.write("Score: {} High Score: {}".format(score,high_sc),align ="center",font=('Courier',20,'normal'))

    #move ends
    for index in range(len(segments)-1,0,-1):
               x = segments[index-1].xcor()
               y = segments[index-1].ycor()
               segments[index].goto(x,y)
    #move seg 0 to where head is
    if(len(segments)>0):
           x = head.xcor()
           y = head.ycor()
           segments[0].goto(x,y)
             
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            score=0
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
    time.sleep(delay)
window.mainloop()
