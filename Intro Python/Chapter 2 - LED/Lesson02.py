#!/usr/bin/env python3

# Filename: Lesson02.py

import linkbot
import time

robot = linkbot.Linkbot()

for i in range (1,10):
    robot.setLedColor(255,0,0)
    time.sleep(.25)
    robot.setLedColor(0,0,0)
    time.sleep(.25)