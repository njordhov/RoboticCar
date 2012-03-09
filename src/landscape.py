

from Tkinter import *


class Landscape:

    def __init__ (self, terrain=[], obstacles=[]):
        self.obstacles = obstacles
        self.terrain = terrain
    

    def display (self, canvas):
        
        for item in self.terrain:
            canvas.create_rectangle(item[0], item[1], item[2], item[3], fill="gray")

        for item in self.obstacles:
            canvas.create_rectangle(item[0], item[1], item[2], item[3], fill="blue")

                
    def surface (self, x, y):
        
        for item in self.terrain:
            if (item[0] < x and item[1] < y and x < item[2] and y < item[3]):
                return True
        return False
        

        


  