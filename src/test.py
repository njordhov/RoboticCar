

from landscape import Landscape
from Simulator import Simulator
from math import pi, sqrt

world = Landscape (terrain = [[150,200,350,400], [400,400,600,600], [600,200,800,400]])
demo = Simulator(world)

right = pi/2
left = -pi/2
straight = 0

demo.explore(401, 401, moves=
            [[right, 5],
             [left, 100],
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
             [straight, 150],
             [straight, 100],
             [pi/4, 30],
             [right, 100],
             [right, 50],
             [right, 250],
             [right, 200],
             [right, 300],
             [right, 200],
             [right, 200],
             [right, 250],
             [right, 100],
             [right, 250],
             [straight, 150],
             [right, 80],
             [right, 150],
             [straight, 150],
             [right, 100],
             [right, 100],
             [right, 200],
             [left, 20],
             [right, 20],
             [left, 20],
             [right, 20],
             [left, 20],
             [right, 20],
             [left, 25],
             [left, sqrt(200**2+200**2)],
             [right, 20],
             [right, 20],
             [right, 20]])


demo.interactive()





        


  