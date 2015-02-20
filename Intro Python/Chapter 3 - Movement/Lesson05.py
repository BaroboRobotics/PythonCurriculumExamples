#!/usr/bin/env python3

# Filename: Lesson05.py

import linkbot

robot = linkbot.Linkbot()
robot.setJointSpeeds(90,0,90)    #sets joint speed on Linkbot to 90 degrees per second.
robot.move(190,0,190)    #runs Linkbot motors 1 and 3, through 190 degrees.