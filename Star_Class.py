from Sphere_Class import *
import turtle

class star(sphere):
    def __init__(self,radius=100,mass=100,name="Random Star",colour="yellow"):

        super().__init__(radius,mass)

        # setting turtle settings
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

    
        

        
    
