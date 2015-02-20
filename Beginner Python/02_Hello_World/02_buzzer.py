# File: 02_buzzer.py

import linkbot   # loads 'linkbot' module
import time     # loads 'time' module

robotID = input('Enter Linkbot ID: ')  # prompts user for a Linkbot ID and 
                                       # stores the result in a variable called
                                       # "robotID"
robot = linkbot.Linkbot(robotID)   # Gets a handle to the robot with the serial
                                   # ID stored in "robotID"
                                   
robot.connect()                    # Connect to the robot              
                                   
robot.setBuzzerFrequency(1047)     # Tells the robot to begin emitting a 1047
                                   # Hz tone.
                                   
time.sleep(0.25)                   # Wait for 0.25 seconds

robot.setBuzzerFrequency(1567)     # Change the tone to 1567 Hz.
time.sleep(0.5)                    # Wait for 0.5 seconds.
robot.setBuzzerFrequency(0)        # Turn off tone.