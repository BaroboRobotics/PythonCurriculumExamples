#!/usr/bin/env python3

# Filename: Lesson08c.py

import linkbot
import time

robot1 = linkbot.Linkbot('HJBP')#ID for first Linkbot
robot2 = linkbot.Linkbot('7ZZL')#ID for second Lnkbot
for i in range (1,5): #does the following block 4 times
    for k in range (1,4): #does the following block 3 times
        robot1.setLedColor(255,0,0)#changes LED on robot1 to red
        robot2.setLedColor(0,0,0)#turns LED on robot2 to off
        time.sleep(.5) #waits half a second
        robot1.setLedColor(0,0,0) #turns LED on robot1 off
        robot2.setLedColor(0,0,0)#turns LED on robot2 off
        time.sleep(.5)# waits half a second
    robot1.setLedColor(255,0,0)
    time.sleep(2)
    for k in range (1,3):  #does the following block 2 times
        robot2.setLedColor(255,0,0)#turns LED on robot2 to red
        time.sleep(.5) #waits half a second
        robot2.setLedColor(0,0,0)#turns LED on robot2 off
        time.sleep(.5)# waits half a second
    time.sleep(1)
robot1.setLedColor(0,0,255) #returns LED to blue
robot2.setLedColor(0,0,255) #returns LED to blue