# File: 01_led_color.py
import linkbot
myLinkbot = linkbot.Linkbot()
myLinkbot.connect()

myLinkbot.setLedColor(0, 255, 0)