# File: 02_callbacks.py

import linkbot

def myCallback(button, event, timestamp):
    print("Buttons: ", button)
    print("Event: ", event)
    print("Timestamp:", timestamp)
    print()

robotID = input('Enter robot ID: ')
robot = linkbot.Linkbot(robotID)
robot.enableButtonEvents(myCallback)

input('Try pressing some buttons on the robot. Press "Enter" to quit.')
