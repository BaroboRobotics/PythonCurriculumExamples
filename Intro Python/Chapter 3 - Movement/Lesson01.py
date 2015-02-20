#!/usr/bin/env python3

# Filename: Lesson01.py

import linkbot

robot = linkbot.Linkbot()
robot.setJointSpeeds(90,0,90)   #sets joint speed at 90 degrees per second.
robot.move(360,0,-360)    #moves the joints 1 and 3 360 degrees