#!/usr/bin/env python

## Controller for a Mindstorms NXT robotic car.
## (C)2012 Terje Norderhaug <terje@in-progress.com>
## Open source license to be determined.
##
## Requires nxt-python-2.2.1

from time import sleep

import nxt.locator
from nxt.motor import *
from nxt.sensor import Light, Sound, Touch, Ultrasonic
from nxt.sensor import PORT_1, PORT_2, PORT_3, PORT_4


class Car:

    brick = None
    left = None
    right = None
    
    def __init__ (self):  
        brick = nxt.locator.find_one_brick()
        self.brick = brick
        self.left = Motor(brick, PORT_A)
        self.right = Motor(brick, PORT_C)
        self.light = Light(brick, PORT_3)
        self.ultrasonic = Ultrasonic(brick, PORT_4)
        print "Connection established."

    def turn (self, angle=100, speed = 30):
        if angle > 0:
            self.left.turn(angle, speed)
        elif angle < 0:
            self.right.turn(-angle, speed)

    def forward (self, distance=50, speed=30):
        self.left.run(power=speed)
        self.right.run(power=speed)
        sleep(distance/speed)
        self.left.idle()
        self.right.idle()
    
    def range(self):
        return self.ultrasonic.get_sample()

    def surface(self):
        return self.light.get_sample()




