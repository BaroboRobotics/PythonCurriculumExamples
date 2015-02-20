# File: 01_debug.py
import linkbot

myLinkbot = linkbot.Linkbot('ABCD') # Change 'ABCD' to your Linkbot's Serial ID
myLinkbot.connect()
 
myLinkbot.moveNB(360, 0, -360)    # Roll Forward
myLinkbot.setLedColor(0, 255, 0)  # Set LED to green
myLinkbot.moveNB(-360, 0, 360)    # Roll Backward
myLinkbot.setLedColor(255, 0, 0)  # Set the LED color to red