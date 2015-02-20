# File: 01_melody.py

import linkbot

robot = linkbot.Linkbot('abcd') # Replace 'abcd' with the serial ID on your Linkbot)

import time     # Need to "import time" so we can use time.sleep()
myNotes = [ 44, 42, 40, 42, 44, 44, 44 ] # Put some notes into a list
t=0.5          # Set a value to be used for the duration of the note
for i in myNotes:         # Select which keys on a piano keyboard to use for the tones
    k=pow(2,(i-49)/12)*440      # Determines the frequency of the note to be played
    robot.setBuzzerFrequency(k) # Directs the Linkbot to play this frequency   
    time.sleep(t)               # Pauses the program while the note is played
    robot.setBuzzerFrequency(0) # Turns off the piezo speaker at the end of each note

