

from landscape import Landscape
from Simulator import Simulator
from math import pi
from Tkinter import *

world = Landscape (terrain = [[200,200,400,400], [400,400,600,600], [600,200,800,400]])
demo = Simulator(world)

right = pi/2
straight = 0

demo.explore(400, 400, moves=
            [[straight, 100],
             [right, 100],
             [right, 250],
             [right, 250],
             [right, 400],
             [right, 300],
             [right, 200],
             [right, 200],
             [right, 250],
             [right, 100],
             [right, 250],
             [straight, 150],
             [right, 80],
             [right, 150],
             [straight, 150]])

demo.interactive()





        


  