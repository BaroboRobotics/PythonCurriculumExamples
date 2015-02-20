#!/usr/bin/env python3

# Filename: Lesson03.py

import linkbot

robot = linkbot.Linkbot()
robot.setJointSpeeds(90,90,90)      #sets all joint speeds to 90 degrees per second.
robot.move(190,0,0)    #runs joint 1 for 190 degress counter clockwise.