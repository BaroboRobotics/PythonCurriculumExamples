#!/usr/bin/env python3

# Filename: Lesson07.py

import linkbot
import math

robot = linkbot.Linkbot()

tracklength = 3.6975    # The "track length" is the distance between the two 
                        # wheels
wheel_diameter = 3.5    # The wheel diameter
wheel_radius = wheel_diameter/2 # Calculate the wheel radius based on diameter

radius=float(input('radius:')) #Convert the string returned by input() to float

outer_radius = radius + (tracklength/2) # This is the radius of the circle the 
                                        # outside wheel will trace
inner_radius = radius - (tracklength/2) # This is the radius of the circle that 
                                        # the inside wheel will trace

outer_distance = outer_radius * 2 * math.pi # Find the distances the outside and 
                                            # inside wheel will need to travel
inner_distance = inner_radius * 2 * math.pi

ratio = outer_distance / inner_distance

# If we know how far a wheel needs to go, we can figure out how many degrees the 
# wheel needs to turn in order to travel that far. The equation is:
# r * theta = distance
# where r is the radius of the wheel, theta is an angle in "radians", and 
# distance is how far the wheel will travel in the same units as "r". If we
# solve for theta, we get
# theta = distance / r
# Note that we have to convert theta to degrees before passing it into the 
# "move()" function.
outer_wheel_radians = outer_distance / wheel_radius
outer_wheel_degrees = outer_wheel_radians * 180 / math.pi # Convert to degrees
inner_wheel_radians = inner_distance / wheel_radius
inner_wheel_degrees = inner_wheel_radians * 180 / math.pi

robot.setJointSpeeds(90,0,int(90*ratio)) # speed of wheels
robot.move(inner_wheel_degrees,0,-outer_wheel_degrees) # runs wheels the number of degrees to complete a circle