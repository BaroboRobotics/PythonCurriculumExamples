# File: 02_set_speed.py

import linkbot
import math # So that we can use math.pi
 
myLinkbot = linkbot.Linkbot('ABCD') # Change ABCD to your Linkbot's serial ID

# Set the Linkbot's wheel radius
r = 3.5 / 2 # If you have a wheel that's not 3.5 inches in diameter, change 
            # "3.5" to the diameter of your wheel
 
def driveDistance(linkbot, distance):
    global r
    degrees = (360) / (2 * math.pi * r) * distance
    linkbot.move(degrees, 0, -degrees)
 
def setSpeed(linkbot, speed):
    global r
    omega = (speed/r) * (180/math.pi)
    if omega > 200:
        raise Exception('The speed is too high!')
    linkbot.setJointSpeed(1, omega)
    linkbot.setJointSpeed(3, omega)
 
setSpeed(myLinkbot, 1000)     # Sets the speed to 2.5 inches/sec
driveDistance(myLinkbot, 10) # Drives the Linkbot 10 inches forward
driveDistance(myLinkbot, -5) # Drives the Linkbot 5 inches backward