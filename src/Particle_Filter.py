

from Tkinter import *
from math import *
import random

from Robot import Robot
from landscape import Landscape


class Particle_Filter:
    
    def __init__ (self, N = 100, width=1000, height=1000):
        self.N = N
        self.particles = [Robot(random.random() * float(width), 
                                random.random() * float(height), 
                                random.random() * 2 * pi) 
                          for i in range(N)]

    def display(self, canvas):
        for particle in self.particles:
            particle.display(canvas)
    
    def update (self, rotation, distance, Z, measure):
        for particle in self.particles:
            particle.move(rotation + (random.random()-0.5) / 100.0 , distance + (random.random()-0.5) * 2.0)
        
        w = [(random.random() if measure(particle.x, particle.y) == Z else 0.0) 
             for particle in self.particles]
                
        biggest = max(w)
        beta = 0.0
        index = random.randint(0, self.N-1)
        p = []

        for i in range(self.N):  
            beta += random.random() * biggest * 2.0
            while w[index] < beta: 
                beta -= w[index]
                index += 1
                index %= self.N
            p.append(self.particles[index])
        
        self.particles = p
 


        


  