from Sphere_Class import *
import math
import turtle

class planet(sphere):
    def __init__(self,radius=100,mass=100,name="Random Planet",colour="yellow",x_velocity=0,y_velocity=10,dis=0):

        super().__init__(radius,mass)
        
        self.radius = radius
        self.mass = mass
        self.name = name
        self.colour = colour
        self.dis_x =  dis
        self.dis_y =  0
        self.dis = dis
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.HV = 0 
        self.LV = 0


        #setting turtle settings
        self.t = turtle.Turtle()
        self.t.speed(100)
        self.t.up()
        self.t.color(self.colour)
        self.t.shape("circle")
        self.t.shapesize(self.radius,self.radius,2)
        self.t.goto(self.dis_x,self.dis_y)
        self.t.down()
        

    def __str__(self):
        return "Planet: {}| Radius: {}| Mass:{}| Colour:{}|"\
               .format(self.name,self.radius,self.mass,self.colour)

    def __repr__(self):
        return self.__str__()    
        
    def Move(self,star_mass,G,time):       

        #  G*Mass of sun*distance in x or y direction
        G*star_mass*self.dis_x
        G*star_mass*self.dis_y
        
        #  ax = (g*starmass*self.dx)/(self.dis**3)
        ax = (G*star_mass*self.dis_x)/(self.dis**3)
        
        #  ay = (g*starmass*self.dy)/(self.dis**3)
        ay = (G*star_mass*self.dis_y)/(self.dis**3)

        #  vel_x  = (ax*time) + vel_x
        self.x_velocity += (ax*time)
        #  vel_y  = (ax*time) + vel_y
        self.y_velocity += (ay*time)

        #  self.dx += (time*self.vx)
        self.dis_x += (time*self.x_velocity)
        
        #  self.dy += (time*self.vy)
        self.dis_y += (time*self.y_velocity)

        #  self.dis=math.sqrt(self.dx**2+self.dy**2)
        self.dis=math.sqrt(self.dis_x**2+self.dis_y**2)

        self.t.goto(self.dis_x,self.dis_y)

        #Getting the highest Vel and the lowest
        if self.x_velocity > self.HV:
            self.HV = self.x_velocity 

        if self.y_velocity > self.HV:
            self.HV = self.y_velocity 

        if self.x_velocity < self.LV:
            self.LV = self.x_velocity

        if self.y_velocity < self.LV:
            self.LV = self.y_velocity 

        print ("Planet:{} ".format(self.name))
        print ("X-Vel:{:.2f}   Y-Vel:{:.2} \nHighest-Vel:{:.2} Lowest-Vel:{:.2} \n"\
               .format(self.x_velocity,self.y_velocity,self.HV,self.LV))
        
