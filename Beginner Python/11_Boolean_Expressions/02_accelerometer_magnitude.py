# File: 02_accelerometer_magnitude.py

import math  # for math.sqrt(), the square-root function

def accelMag(accel):
    return math.sqrt( accel[0]**2 + accel[1]**2 + accel[2]**2 )

import linkbot

myLinkbot = linkbot.Linkbot('abcd')  # Replace 'ABCD' with your Linkbot's ID

accel = myLinkbot.getAccelerometer()  # Get the accel values
print(accel)            # print accel values
print(accelMag(accel))  # print total magnitude of accel values