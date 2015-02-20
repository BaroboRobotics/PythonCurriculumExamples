#!/usr/bin/env python3

import linkbot

robot = linkbot.Linkbot()
robot.setJointSpeeds(45,0,45)     #sets joint speed to 45 degrees per second.
robot.move(-190,0,190)     #the Linkbot will creep backward slowly.