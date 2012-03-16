# Robotic Car

Welcome to the Robotic Car project of the San Diego Artificial Intelligence study group.

This is a hands-on complement to the UDACITY CS 373 class "Programming a Robotic Car".

We're implementing a controller for Mindstorms NXT models of self driven cars, with a matching simulator to test our algorithms.

We will apply various AI methods similar to those used for full size self driven cars, such as probabilistic inference, computer vision, machine learning, and planning.

The code is implemented in Python, as this is the language used for the class. Other languages may also be used.

## Community

URL: http://www.meetup.com/SanDiegoAI/

## Description

The first version of our robot can drive forward, turn, and sense the surface under it (binary, e.g. if it is dark or not).

The file "car.py" contains the interface to control the robot and read its sensors.

We've made a simulator to test the robot virtually, and experiment with various localization algorithms.

There is an implementation of a particle filter to localize the robot.

## Running the Simulator

    $ cd src
    $ python demo.py

## Game

Can you control the robot to get all particles to cloud around it?

    $ cd src
    $ python game.py 7

The numerical argument determines the complexity of the landscape.

## Manual Simulation

    $ cd src
    $ python
    >>> import game
    >>> game = game.Game(complexity = 4)

Place a hidden robot in a random location:

    >>> game.board.place_robot(x = None, y = None, color = "None")

Set directions:

    >>> import math; right = math.pi/2; left = - math.pi/2

Move:

    >>> game.board.move_robot(right, 100)
    >>> game.board.move_robot(left, 100)

Repeat until the robot is localized!


## Controlling the Robot

Download nxt-python from:

http://code.google.com/p/nxt-python/

Place the nxt-python directory in src folder of this repository, then:

    $ cd src
    $ python car.py

## Troubleshooting

If Bluetooth doesn't connect:

1. Make sure the NXT display is not in the bluetooth configuration mode.

If you see the following error:

    nxt.locator.NoBackendError: No selected backends are available! Did you install the comm modules?

Potential fixes:

1. export the PYTHONPATH from the shell to the directory of the installed lightblue

## License

Open source license to be determined.