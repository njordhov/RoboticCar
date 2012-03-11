

from math import *
import random

def roulette (samples, weights = None , count = None):
    """Sampling with replacement, using the roulette wheel algorithm described in Udacity CS373 unit 3.20"""
    # http://www.udacity.com/view#Course/cs373/CourseRev/feb2012/Unit/182001/Nugget/215003
    
    if not count:
        count = len(samples)
    if not weights:
        weights = [1.0 for i in range(samples)]

    biggest = max(weights)
    beta = 0.0 
    index = random.randint(0, count - 1)
                
    for i in range(count):  
        beta += random.random() * biggest * 2.0
        while weights[index] < beta: 
            beta -= weights[index]
            index += 1
            index %= count
        yield samples[index]


        


  