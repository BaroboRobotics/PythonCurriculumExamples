# File: 01_reaction_time.py

import time
import linkbot
import random
import sys

robotID = input('Enter robot ID: ')
robot = linkbot.Linkbot(robotID) #enter the linkbot ID
time_start=0
button_pressed=False
game_start=False

def callback(buttons, event, timestamp):                                  # 01
    if (buttons & 0x02) and event:                                        # 02
        global game_start                                                 # 03
        global time_start
        global button_pressed
        button_pressed=True                                               # 04
        if game_start==False:                                             # 05
            print("You pressed the button to soon")
        else:
            print("your  reaction time is :", time.time()-time_start)
        global robot
        robot.setBuzzerFrequency(0)
 
robot.enableButtonEvents(callback)                                        # 06
input("Press enter to begin")                                             # 07
robot.setLedColor(255, 0, 0)                                              # 08
time.sleep(random.random()*7+3)                                           # 09
if button_pressed:                                                        # 10
    sys.exit()
time_start=time.time()                                                    # 11
game_start=True                                                           # 12
robot.setBuzzerFrequency(440)                                             # 13
robot.setLedColor(0, 255, 0)                                              # 14
while True:                                                               # 15
    time.sleep(1)
    if button_pressed:
        sys.exit()