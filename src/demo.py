

from Tkinter import *
from math import *
import random

from landscape import Landscape
from Particle_Filter import Particle_Filter
from Robot import Robot


def start_robot(x, y, landscape):
    
    master = Tk()
    canvas = Canvas(master, width=1000, height=800)
    canvas.pack()
    
    world.display(canvas)
    robot = Robot (x, y)
    robot.color = None
    robot.size = 5
    filter = Particle_Filter(N=1000)
    filter.display(canvas)
    robot.display(canvas)
    
    def callback (event):
        Z = landscape.surface (event.x, event.y)
        print "@", event.x, ",", event.y, "->", Z 
        bearing = atan2((event.y - robot.y), (event.x - robot.x))
        rotation = bearing - robot.orientation
        distance = sqrt((robot.x - event.x) ** 2 + (robot.y - event.y) ** 2)
        canvas.create_line(robot.x, robot.y, event.x, event.y)
        robot.move(rotation, distance)
        robot.display(canvas)
        filter.update(rotation, distance, Z, lambda x, y: landscape.surface (x, y))
        filter.display(canvas)
        
    canvas.bind("<Button-1>", callback)


# ------------------------------

world = Landscape (terrain = [[200,200,400,400], [400,400,600,600], [600,200,800,400]])

start_robot(500, 400, world)

mainloop()




        


  