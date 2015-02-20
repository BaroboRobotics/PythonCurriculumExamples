# File: 01_music.py
import linkbot

robotID = input('Enter Linkbot ID: ')
robot = linkbot.Linkbot(robotID) 
robot.connect()
import time # imports the Python "time" module because we want to use 
            # "time.sleep()" later.
key = 34  # Set key=34 which is the 34th key on a piano keyboard.
while key < 74:  # While the key number is less than 74.
    # The next line plays the frequency corresponding to the note stored in
    # the variable "key"
    robot.setBuzzerFrequency(2 ** ((key - 49) / 12.0) * 440) 
    time.sleep(.25)  # Play the note for 0.25 seconds.
    robot.setBuzzerFrequency(0)  # Turn off the note
    key = key + 1   # Increase the key number by 1. This is the end of the loop. 
                    # At this point, Python will check to see if the condition 
                    # in the "while" statement, "key < 74", is true. If it is 
                    # still true, Python will go back to the beginning of the 
                    # loop. If not, the program exits the loop.
