from Sphere_Class import *
from Planet_Class import *
from Star_Class import *
import turtle

#Turtle settings and pics for planets 
turtle.bgcolor("black")
turtle.register_shape("p1.gif")
turtle.register_shape("p2.gif")
turtle.register_shape("p3.gif")
turtle.register_shape("p4.gif")
turtle.register_shape("s1.gif")

# Making global varibles
G = -0.1
time = 1

# Creating the star 
s1 = star(50,5000,"Sun","yellow")

# Planet pic-name radius  mass  name  color  x_vel y_vel dis 
p1 = planet(1,1000,"Hera","red",0.0,2.0,80)
p2 = planet(1.1,5000,"Zeus","blue",0.0,1.25,160)
p3 = planet(1.2,9000,"Rhea","orange",0.0,0.80,240)
p4 = planet(1.3,49000,"Eros","purple",0.0,.8,320)

while True:
    p1.Move(s1.mass,G,time)
    p2.Move(s1.mass,G,time)
    p3.Move(s1.mass,G,time)
    p4.Move(s1.mass,G,time)
