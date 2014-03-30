'''
This is the sphere class everything
will inherit this planets and stars
Only takes the radius and mass
'''

class sphere(object):
    def __init__(self,radius=100,mass=100):
        self.radius = radius
        self.mass = mass

    def __str__(self):
        return "Planet: {}| Radius: {}|  Mass: {}| Velocity: {}|"\
        .format(self.name,self.radius,self.mass,self.Velocity)
    
    def __repr__(self):
        return self.__str__()

