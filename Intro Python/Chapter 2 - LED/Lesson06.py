#!/usr/bin/env python3

# File: Lesson06.py

import time
import linkbot
import random
import sys

robotID = input('Enter robot ID: ')
robot = linkbot.Linkbot(robotID) #enter the linkbot ID
time_start=0
button_pressed=False
game_start=False

def callback(buttons, event, timestamp):
    if (buttons & 0x02) and event:
        global game_start
        global time_start
        global button_pressed
        button_pressed=True
        if game_start==False:
            print("You pressed the button to soon")
        else:
            print("your  reaction time is :", time.time()-time_start)
        global robot
        robot.setBuzzerFrequency(0)
 
robot.enableButtonEvents(callback)
input("Press enter to begin")
robot.setLedColor(255, 0, 0)
time.sleep(random.random()*7+3)
if button_pressed:
    sys.exit()
time_start=time.time()
game_start=True
robot.setBuzzerFrequency(440)
robot.setLedColor(0, 255, 0)
while True:
    time.sleep(1)
    if button_pressed:
        sys.exit()