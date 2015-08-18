# File: 03_event_callbacks.py

import linkbot

def accelCallback(x, y, z, timestamp):
    print("Accel Event!", x, y, z, timestamp)

def encoderCallback(joint, angle, timestamp):
    print("Encoder Event!", joint, angle, timestamp)

robotID = input('Enter robot ID: ')
robot = linkbot.Linkbot(robotID)
robot.enableAccelerometerEvents(accelCallback)
# enableEncoderEvents() expects 2 arguments: A granularity (in degrees) and
# a callback function. The granularity specifies the minimum amount a 
# Linkbot's joint needs to move before the encoder callback is called.
# Setting it to "5" means that the callback will only be called if the joint
# moves 5 degrees or more.
robot.enableEncoderEvents(5, encoderCallback)

input("Try moving the robot around and moving the robot's joints." 
      "Press 'Enter' to quit.")
