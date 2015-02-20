# File: 02_debug.py
import linkbot

myLinkbot = linkbot.Linkbot('ABCD') # Change 'ABCD' to your Linkbot's Serial ID
myLinkbot.connect()

print("Moving forward...")
myLinkbot.moveNB(360, 0, -360)    # Roll Forward
print("Done. Setting LED to green...")
myLinkbot.setLedColor(0, 255, 0)  # Set LED to green
print("Done. Moving backward...")
myLinkbot.moveNB(-360, 0, 360)    # Roll Backward
print("Done. Setting LED to red...")
myLinkbot.setLedColor(255, 0, 0)  # Set the LED color to red
print("Done.")