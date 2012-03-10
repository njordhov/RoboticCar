

from landscape import Landscape
from Simulator import Simulator
import random


def ground (left, top, right, bottom, minsize = 20, maxsize=200): 
    w = random.randint(minsize, maxsize)
    h = random.randint(minsize, maxsize)
    x = random.randint(left, right - w)
    y = random.randint(top, bottom - h)
    return [x, y, x+w, y+h]


class Game:
    
    def __init__ (self, complexity = 8, width=1000, height=800, margin=100):
        world = Landscape (terrain = [ground(margin, margin, width-margin, height-margin) for i in range(complexity)])
        self.board = Simulator(world, width=width, height=height)
        self.board.interactive() 


if __name__ == "__main__":
    
    import sys
    if len(sys.argv) > 1:
        complexity = int(sys.argv[1])
    else:
        complexity = 7

    game = Game(complexity = complexity)


    



        


  