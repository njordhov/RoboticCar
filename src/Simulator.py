

from Tkinter import *
from math import *

from Particle_Filter import Particle_Filter
from Robot import Robot


class Simulator:
    
    robot = None
    
    def __init__ (self, world, width=1000, height=800):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=width, height=height)
        canvas = self.canvas
        canvas.pack()
        self.world = world
        world.display(canvas)
        self.localizer = Particle_Filter(N=3000, width=width, height=height)
        localizer = self.localizer
        localizer.display(canvas)

    def interactive (self):
        """Start interactive mode (doesn't return)"""
        print "Click anywhere on the canvas to place the robot"
        
        def callback (event):
            self.move_robot(event.x, event.y)
    
        self.canvas.bind("<Button-1>", callback)
        mainloop()
    
    def move_robot(self, x, y):
        """Move the robot to the given position on the canvas"""
        if not self.robot:
            self.robot = Robot (x, y)
            self.robot.color = None
            self.robot.size = 5

        robot = self.robot
        canvas = self.canvas
        localizer = self.localizer
        Z = self.world.surface (x, y)
        print "@", x, ",", y, "->", Z 
        bearing = atan2((y - robot.y), (x - robot.x))
        rotation = bearing - robot.orientation
        distance = sqrt((robot.x - x) ** 2 + (robot.y - y) ** 2)
        canvas.create_line(robot.x, robot.y, x, y)
        robot.move(rotation, distance)
        robot.display(canvas)
        self.localizer.erase(canvas)
        localizer.update(rotation, distance, Z, lambda x, y: self.world.surface (x, y))
        localizer.display(canvas)

        


  