#!/usr/bin/env python3

# Filename: Lesson05.py

import linkbot
import time
import random
import sys

robot = linkbot.Linkbot() 

robot.setLedColor(255,0,0)  #set the LED to red on “robot”.

def callback(button, event, timestamp): # defines a function “callback”
    print(button, event)
    if button == 1:
        global robot
        robot.setLedColor(0,255,0)

robot.enableButtonEvents(callback) # Register the callback function with the 
                                       # robot
while True:
    time.sleep(1)