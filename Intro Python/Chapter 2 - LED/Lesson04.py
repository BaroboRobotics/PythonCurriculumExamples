#!/usr/bin/env python3

# Filename: Lesson04.py 

import linkbot
import time

robot = linkbot.Linkbot()

mph=float(input("mph="))
print(mph)
yellow_time=(1.467*mph/15.0+1.5)
print(yellow_time)
time.sleep(3.0)
robot.setLedColor(0,255,0)
time.sleep(3)
robot.setLedColor(255,255,0)
time.sleep(yellow_time)
robot.setLedColor(255,0,0)