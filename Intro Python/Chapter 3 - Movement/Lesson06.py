#!/usr/bin/env python3

# Filename: Lesson06.py

import linkbot

robot = linkbot.Linkbot() 
robot.setJointSpeeds(90,0,1.89*90)
robot.move(240,0,-1.89*240)