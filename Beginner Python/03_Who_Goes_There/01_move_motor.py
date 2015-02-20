# File: 01_move_motor.py
# This program moves Joint 1 on a Linkbot by an amount 
# specified by the user
import linkbot  # Load the "linkbot" package.

robotID = input('Enter Linkbot ID: ')  # Prompt user to enter a Linkbot ID.
myLinkbot = linkbot.Linkbot(robotID)
myLinkbot.connect()

degrees = float(input("Degrees to rotate Joint 1: "))   # Prompt user to enter
                                                        # a value
myLinkbot.moveJoint(1, degrees) # Turn Joint 1 on the Linkbot the number of 
                                # degrees specified earlier by the user.