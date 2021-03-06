﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareAt(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks

def drawSquareFrom():
    t1.penup()
    t1.home()
    t1.pendown()
    tracks=({0:(0,0),1:(50,0),2:(50,50),3:(0,50),4:(0,0)})
    
    for i in range(1,5):
        t1.goto(tracks[i])
    for i in range(1,5):
        print tracks[i]

def lap7():
    mytrack=drawSquareAt(100,(20,30))
    print mytrack
    drawSquareFrom()
    
def main():
    lap7()


if __name__=="__main__":
    main()

wn=raw_input()
