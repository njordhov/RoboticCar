

from Tkinter import *
from math import *
import random
from copy import copy

from Robot import Robot
from landscape import Landscape
import Sampling


class Particle_Filter:
    
    turn_noise = 0.04
    forward_noise = 0.3
    sense_noise = 10.0
    
    def __init__ (self, N = 1000, width=1000, height=1000):
        self.N = N
        self.particles = [Robot(random.random() * float(width), 
                                random.random() * float(height), 
                                random.random() * 2.0 * pi) 
                          for i in range(N)]

    def display(self, canvas):
        for particle in self.particles:
            particle.display(canvas)
    
    def erase(self, canvas):
        for particle in self.particles:
            particle.erase(canvas)
    
    def update (self, rotation, distance, Z, measure):
        for particle in self.particles:
            particle.move(random.gauss(rotation, self.turn_noise), random.gauss(distance, self.forward_noise))
            if measure(particle.x, particle.y):
                particle.color = "blue" 
            else:
                particle. color = "red"
        
        w = [random.gauss(100.0, self.sense_noise) if measure(particle.x, particle.y) == Z else abs(random.gauss(0.0, self.sense_noise)) 
             for particle in self.particles]
                                                    
        self.particles = [copy(sample) for sample in Sampling.roulette(self.particles, w)]
 


        


  