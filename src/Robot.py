

from Tkinter import *
from landscape import Landscape
from math import *
import random


class Robot:
    
    size = 2
    color = "red"
    widget = None
    
    def __init__ (self, x=0, y=0, orientation = 2 * pi):
        self.x = x
        self.y = y
        self.orientation = orientation
    
    def display (self, canvas):
        size = self.size
        color = self.color
        if self.widget:
            canvas.delete(self.widget)
        self.widget = canvas.create_rectangle(self.x - size, self.y - size, self.x + size, self.y + size, fill=color)
    
    def move (self, rotation, distance):
        self.orientation += rotation
        self.orientation %= 2* pi
        self.x += (cos (self.orientation) * distance)
        self.y += (sin (self.orientation) * distance)
    
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (self.x, self.y, self.orientation)


        


  