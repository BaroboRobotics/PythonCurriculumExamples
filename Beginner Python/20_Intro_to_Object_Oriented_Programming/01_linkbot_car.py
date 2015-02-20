# File: 01_linkbot_car.py

import linkbot
import math  # for math.pi
import time  # for time.sleep()

class LinkbotCar(linkbot.Linkbot):           # 1
    def driveForwardDistance(self, inches):  # 2
        wheelRadius = 3.5/2.0
        degrees = (360.0/(2.0*math.pi*wheelRadius)) * inches
        self.move(degrees, 0, -degrees)      # 3

myLinkbotCar = LinkbotCar('ABCD')            # 4

myLinkbotCar.driveForwardDistance(5)         # 5
myLinkbotCar.setBuzzerFrequency(440)         # 6
time.sleep(0.5)
myLinkbotCar.setBuzzerFrequency(0)