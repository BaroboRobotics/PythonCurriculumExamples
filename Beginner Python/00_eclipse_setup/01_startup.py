# File: 01_startup.py
import linkbot
 
myLinkbot = linkbot.Linkbot()
myLinkbot.connect()
print("Setting a Linkbot's LED color to red...")
myLinkbot.setLedColor(255, 0, 0)
print('done.')