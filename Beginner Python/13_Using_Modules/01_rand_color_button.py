# File: 01_rand_color_button.py

# This program changes the Robots LED color every time you press the "B" button 
# on the robot.

import linkbot  #imports the module with the Linkbot commands
import time     #imports the module to use time.sleep
import random   #imports a random integer generator

robotID = input('Enter robot ID: ') #prompts user to enter Linkbot ID
robot = linkbot.Linkbot(robotID) 

def callback(buttons, event, timestamp):
    global robot
    if buttons & 0x02:
        robot.setLedColor(           #calls setLEDColor from 'barobo' module
            random.randint(0, 255),  #uses the 'random' integer generator from
            random.randint(0, 255),  #the random module to set colors
            random.randint(0, 255)
            )
        
robot.enableButtonEvents(callback)
while True:
    time.sleep(1)   #uses the 'time' module to call time.sleep command