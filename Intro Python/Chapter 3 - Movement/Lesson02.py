#!/usr/bin/env python3

# Filename: Lesson02.py

import linkbot

robot = linkbot.Linkbot()
robot.setJointSpeeds(90,90,90)  #sets all joint speed to 90 degrees per second.
robot.move(0,0,-190)    #runs joint 3 clockwise 190 degrees.