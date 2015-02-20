#!/usr/bin/env python3

# Filename: Lesson03.py

import linkbot
import time

robot1 = linkbot.Linkbot()  #set ID to a certain Linkbot

robot1.setLedColor(0,255,0)     #sets color of LED to green
time.sleep(3)                   #waits 3 seconds
for i in range(1,6):            #runs the block that follows five times
    robot1.setLedColor(255,0,0) #sets color to red
    time.sleep(.5)              #waits half a second
    robot1.setLedColor(0,0,0)   #turns off LED
    time.sleep(.5)              #waits half a second
robot1.setLedColor(0,0,255)     #turns LED to blue