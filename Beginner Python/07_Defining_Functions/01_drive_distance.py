# File: 01_driveDistance.py
import linkbot
import math # So that we can use math.pi

myLinkbot = linkbot.Linkbot('abcd') # Change abcd to your Linkbot's serial ID

def driveDistance(linkbot, distance):
    r = 3.5 / 2 # If you have a wheel that's not 3.5 inches in diameter, change
                # "3.5" to the diameter of your wheel
                
    # Next: Calculate degrees we have to turn the Linkbot's wheels to go a 
    # distance of "distance".
    degrees = (360) / (2 * math.pi * r) * distance
    # Finally, we turn the Linkbot's wheels that number of degrees.
    linkbot.move(degrees, 0, -degrees)

driveDistance(myLinkbot, 10) # Drives the Linkbot 10 inches forward
driveDistance(myLinkbot, -5) # Drives the Linkbot 5 inches backward              
