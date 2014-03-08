import turtle

class myStar:
    GravityForce = 0.1
    def __init__(self):

        #---Set Stats---#
        self.Radius = 500
        self.Mass = 15000
        #---------------#

        #-Set Turtle settings-# 
        t = turtle.Turtle()
        turtle.bgcolor("black") # Set background colour
        self.t = t
        size = 100
        self.size = size
        self.t.ht() # Hide arrows
        self.t.speed(100) # Set sped to max
        self.t.dot(size,'yellow') # Set the color and size
        #---------------------#
        self.t.up()# Raise pen so it doesent draw

class star(myStar):
    def __init__(self,name,r,m,c,d):
        myStar.__init__(self)

        self.name = name
        self.r = r
        self.m = m
        self.c = c
        self.d = d

        self.t.goto(0,self.size+d)
        self.t.down() # Put pen down to draw
        self.t.dot(r,c)
        
        

        
        

game = myStar()

p1=star('P1', 19.5, 1000.0, "green", 0.25)
