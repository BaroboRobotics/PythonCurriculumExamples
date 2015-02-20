#File: 01_for_loop_notes.py

import linkbot

robot = linkbot.Linkbot('abcd') # Replace 'abcd' with the ID of your Linkbot
import time     # For time.sleep()
t=0.5           # Set a value to be used for the duration of the note
for i in range (33,43):         # Select which keys on a piano keyboard to use 
    k=pow(2,(i-49)/12)*440      # Find the frequency of the note to be played
    robot.setBuzzerFrequency(k) # Directs the Linkbot to play this frequency   
    time.sleep(t)               # Pauses the program while the note is played

robot.setBuzzerFrequency(0)     # Turn off the speaker at the end of the program