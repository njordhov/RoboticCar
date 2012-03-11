

from Tkinter import *
from math import *

from ParticleFilter import ParticleFilter
from Robot import Robot
import time


class Simulator:
    
    robot = None
    
    def __init__ (self, world, width=1000, height=800):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=width, height=height)
        canvas = self.canvas
        canvas.pack()
        self.world = world
        world.display(canvas)
        self.localizer = ParticleFilter(N=3000, width=width, height=height)
        localizer = self.localizer
        localizer.display(canvas)
    

    def interactive (self):
        """Start interactive mode (doesn't return)"""
        print "Click anywhere on the canvas to place the robot"
        
        def callback (event):
            print "@", event.x, ",", event.y
            self.place_robot(event.x, event.y)
    
        self.canvas.bind("<Button-1>", callback)
        mainloop()

    
    def explore (self, x, y, moves, delay = 1/2):
        self.place_robot(x, y)
        for (x, y) in moves:
            self.move_robot(x, y)
            time.sleep(delay)
    

    def measurement_probabilty (self, particle, Z):
        loss = self.world.binary_loss(particle, Z)
        if loss:
            particle.color = "blue"
        else:
            particle. color = "gray"
        return loss

                
    def move_robot(self, rotation, distance):
        robot = self.robot
        canvas = self.canvas
        localizer = self.localizer
        if not robot:
            raise ValueError, "Need to place robot in simulator before moving it" 
        
        original_x = robot.x
        original_y = robot.y
        robot.move(rotation, distance)
        
        canvas.create_line(original_x, original_y, robot.x, robot.y)
        Z = self.world.surface (robot.x, robot.y)
        self.localizer.erase(canvas)                                
        localizer.update(rotation, distance, lambda particle: self.measurement_probabilty(particle, Z))
        localizer.display(canvas)
        robot.display(canvas)
        self.master.update()
        print "Sense:", Z

    
    def place_robot(self, x, y, bearing=None):
        """Move the robot to the given position on the canvas"""
        if not self.robot:
            self.robot = Robot (x, y)
            self.robot.display_noise = 0.0
            self.robot.color = "green"
            self.robot.size = 5

        robot = self.robot
        if not bearing:
            bearing = atan2((y - robot.y), (x - robot.x))
        rotation = bearing - robot.orientation
        distance = sqrt((robot.x - x) ** 2 + (robot.y - y) ** 2)
        self.move_robot(rotation, distance)
                

        


  