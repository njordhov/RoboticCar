

from Landscape import Landscape
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

    def play(self):
        self.board.interactive()


if __name__ == "__main__":
    
    import sys
    if len(sys.argv) > 1:
        complexity = int(sys.argv[1])
    else:
        complexity = 7

    game = Game(complexity = complexity)
    world = game.board.world

    def measurement_loss (particle, Z):
        loss = world.deviation_loss (particle, Z)
        if loss == 1.0:
            particle.color = "blue"
        elif loss < 1.0:
            particle.color = "gray%d" % (80 - int(loss * 60))
        else:
            # error
            particle.color = "red"
        return loss
        
    game.board.measurement_probabilty = measurement_loss
    
    game.play()



    



        


  