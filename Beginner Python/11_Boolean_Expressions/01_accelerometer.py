# File: 01_accelerometer.py

import linkbot

myLinkbot = linkbot.Linkbot('abcd') # Replace "abcd" with our Linkbot's ID

accel = myLinkbot.getAccelerometer()
print(accel)