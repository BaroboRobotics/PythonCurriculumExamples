#!/usr/bin/env python3 

# Filename: Lesson08b.py 

import linkbot
import time
robot1 = linkbot.Linkbot('HJBP')#ID for first Linkbot
robot2 = linkbot.Linkbot('7ZZL')#ID for second Lnkbot
for i in range (1,8): #does the following block 7 times
    robot1.setLedColor(255,0,0)#changes LED on robot1 to red
    robot2.setLedColor(0,0,0)#turns LED on robot2 to off
    time.sleep(.5) #waits half a second
    robot1.setLedColor(0,0,0) #turns LED on robot1 off
    robot2.setLedColor(255,0,0)#turns LED on robot2 red
    time.sleep(.5)# waits half a second
robot1.setLedColor(0,0,255) #turns LED to blue
robot2.setLedColor(0,0,255) #turns LED to blue