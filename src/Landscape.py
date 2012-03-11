

from Tkinter import *
from math import *


class Landscape:

    def __init__ (self, terrain=[], obstacles=[]):
        self.obstacles = obstacles
        self.terrain = terrain
    

    def display (self, canvas):
        
        for item in self.terrain:
            canvas.create_rectangle(item[0], item[1], item[2], item[3], fill="forest green", tags="ground")

        for item in self.obstacles:
            canvas.create_rectangle(item[0], item[1], item[2], item[3], fill="red", tags="obstacle")

                
    def surface (self, x, y):
        
        for item in self.terrain:
            if (item[0] < x and item[1] < y and x < item[2] and y < item[3]):
                return True
        return False


    def binary_loss (self, particle, Z):
        x = particle.x
        y = particle.y
        measure = self.surface (x, y)
        if measure == Z:
            return 1.0
        else:
            return 0.0


    def deviation_loss (self, particle, Z):
        """Loss value depends on how far away the particle is from a position that matches the measurement"""
        x = particle.x
        y = particle.y
        measure = self.surface (x, y)
        
        def deviation (x, y, rectangle):
            # better: distance to edge closest to x,y
            center_x = (rectangle[2] + rectangle[0]) / 2
            center_y = (rectangle[3] + rectangle[1]) / 2
            distance_to_center = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            center_to_edge = min([abs (x - center_x), abs (y - center_y)])
            return (distance_to_center - center_to_edge)
        
        if measure == Z:
            return 1.0
        elif measure:   
            # inverse square minimum distance to first matching edge 
            for item in self.terrain:
                if (item[0] < x and item[1] < y and x < item[2] and y < item[3]):
                    distance = min ([abs (x - item[0]), abs (y - item[1]), abs ( x - item[2]), abs (y - item[3])])
                    return 1 / (1 + distance / 100) ** 2
        else:
            # sum of inverse square distance to ground
            weight = 0.0
            for ground in self.terrain:
                distance = deviation (x, y, ground)
                weight += 1 / (1 + distance / 20 ) ** 2  
            weight = min([weight, 0.9])
            return weight   


        

        


  