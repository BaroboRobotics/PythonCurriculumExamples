#!/usr/bin/env Python3

# Filename: Lesson01.py

import linkbot
import time

robot = linkbot.Linkbot()

robot.setBuzzerFrequency(1046.5)
time.sleep(1.5)
robot.setBuzzerFrequency(0)
time.sleep(3)
robot.setLedColor(255,0,0)