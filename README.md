# Robotic Car

Welcome to the Robotic Car project of the San Diego Artificial Intelligence study group.

This is a hands-on complement to the Udacity 373 class "Programming a Robotic Car".

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

## Controlling the Robot

Download nxt-python from:

http://code.google.com/p/nxt-python/

    $ cd src
    $ python car.py

## License

Open source license to be determined.