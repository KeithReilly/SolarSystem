from tkinter import *
import turtle
import math

class sphere(object):
    def __init__(self,radius=100,mass=100):
        self.radius = radius
        self.mass = mass

    def __str__(self):
        return "Planet: {}| Radius: {}|  Mass: {}| Velocity: {}|"\
        .format(self.name,self.radius,self.mass,self.Velocity)
    
    def __repr__(self):
        return self.__str__()

class star(sphere):
    def __init__(self,radius=100,mass=100,name="Random Star",colour="yellow"):

        super().__init__(radius,mass)

        # Turtle settings
        self.t = turtle.Turtle()
        self.t.ht()
        
        self.t.down()
        self.radius = radius
        self.mass = mass
        self.name = name
        self.colour = colour
        self.t.up()
        self.t.dot(self.radius,self.colour)
        

    def __str__(self):
        return "Star: {}| Radius: {}| Mass:{}| Colour:{}|"\
               .format(self.name,self.radius,self.mass,self.colour)

    def __repr__(self):
        return self.__str__()

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

        #Turtle settings
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
        
        #  ax = (g*starmass*self.dx)/(self.dis**3)
        ax = (G*star_mass*(-self.dis_x))/(self.dis**3)
        
        #  ay = (g*starmass*self.dy)/(self.dis**3)
        ay = (G*star_mass*(-self.dis_y))/(self.dis**3)

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
               "X-Pos: {:.2} Y-Pos: {:.2}\n"
               .format(self.x_velocity,self.y_velocity,self.HV,self.LV,self.dis_x,self.dis_y))


# Functions when buttons are pressed
def plusgrav(GravList):
    GravList.append(G + .05)
    
def minusgrav(GravList):
    GravList.append(G - .05)

def ChgTime(Time_List):
    Time_List.append(float(EntT.get()))

def ChgMass(Mass_List):
    Mass_List.append(float(EntM.get()))

def ChgVal(Mass_List):
    Mass_List.append(float(EntM.get()))
    

#Turtle settings and pics for planets 
turtle.bgcolor("black")

# Making global varibles
G = 0.1
time = 1

# Creating Lists to hold users choices 
GravList = [.1]
Time_List = []
Mass_List = []
Vel_List = []


# Creating the star 
s1 = star(50,5000,"Sun","yellow")

# Planet pic-name radius  mass  name  color  x_vel y_vel dis 
p1 = planet(1,1000,"Hera","red",0.0,2.0,80)
p2 = planet(1.1,5000,"Zeus","blue",0.0,1.25,160)
p3 = planet(1.2,9000,"Rhea","orange",0.0,0.80,240)
p4 = planet(1.3,49000,"Eros","purple",0.0,.8,320)

#Gui menu interface also 
menu = Tk()
label = Label(menu,text= "Change Programe")
label.grid()

# --------------------Change Gravity-------------------------------#
B1 = Button(menu,text="+ .1 Gravity:",command=lambda:plusgrav(GravList))
B1.grid(row=1,column=0)

B2 = Button(menu,text="- .1 Gravity:",command=lambda:minusgrav(GravList))
B2.grid(row=2,column=0)
#------------------------------------------------------------------#

#-------------------------Change Mass------------------------------------#
B3 = Button(menu,text="Encrypt:",command=lambda:ChgMass(Mass_List))
B3.grid(row=3,column=0)

EntM = Entry(menu,bd=5)
EntM.grid(row=3,column=1)
#------------------------------------------------------------------------#

#--------------------------Change Time-----------------------------------#
B4 = Button(menu,text="Change Time:",command=lambda:ChgTime(Time_List))
B4.grid(row=4,column=0)

EntT = Entry(menu,bd=5)
EntT.grid(row=4,column=1)
#------------------------------------------------------------------------#

#--------------------Main Loop--------------------------#
while True:

    if len(GravList)> 0:
        G = GravList.pop()

        #This prints out the gravity beside the button#
        GravPlus = Label(menu,text="{0:.2%}".format(G))
        GravPlus.grid(row=1,column=1)
        GravMinus = Label(menu,text="{0:.2%}".format(G))
        GravMinus.grid(row=2,column=1)

    if len(Time_List)> 0:
        time = Time_List.pop()

    if len(Mass_List)> 0:
        s1.mass= Mass_List.pop()

    if len(Vel_List)> 0:
        p1.mass= Vel_List.pop()
        
    p1.Move(s1.mass,G,time)
    p2.Move(s1.mass,G,time)
    p3.Move(s1.mass,G,time)
    p4.Move(s1.mass,G,time)

menu.mainloop()

#--------------------------------------------------------#
