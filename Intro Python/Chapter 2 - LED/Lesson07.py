#!/usr/bin/env python3

# Filename: Lesson07.py

import linkbot

robot = linkbot.Linkbot()
robot.stop()

for _ in range(100):
    joint_one = robot.getJointAngle(1) # Get the angle for joint 1
    intensity=abs(int(joint_one*255/180)) # Convert from degrees to an integer
    robot.setLedColor(intensity,0,0) # Set the intensity of the red LED