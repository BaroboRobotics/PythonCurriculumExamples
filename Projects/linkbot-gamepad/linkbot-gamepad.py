#!/usr/bin/env python3

import pygame
import linkbot
import sys
import math

def main():
    serialID = input(
        'Please enter the serial ID of the Linkbot you want to control: ')
    try:
        robot = linkbot.Linkbot(serialID)
    except:
        print('Could not connect to robot.')
        sys.exit(-1)

    print('Press "CTRL-C" to quit.')

    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key.unicode == 'q':
                    done = True

        # The following block of commented code can be used to print information
        # about all connected joysticks and their current states.
        for i in range (pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            print('Joystick {}:'.format(i))

            for i, axis in enumerate( 
                    map(joystick.get_axis, range(joystick.get_numaxes()))):
                print('Axis {} value: {:>6.3f}'.format(i, axis))

            for i, button in enumerate(
                    map(joystick.get_button, range(joystick.get_numbuttons()))):
                print('Button {:>2} value: {}'.format(i,button))

        # For my setup, I want to use joystick 0 to control the robot.
        # Axis 1 controls forward-backward (but is negative), and axis 0
        # controls left/right.
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        drive_axis = joystick.get_axis(1)
        turn_axis = joystick.get_axis(0)
        motorpower1 = (-255*drive_axis) + (255*turn_axis)
        motorpower3 = (255*drive_axis) + (255*turn_axis)
        robot.setMotorPowers(int(motorpower1), 0, int(motorpower3))
        
        # Make button A make a siren sound
        if joystick.get_button(0):
            omega = 2*math.pi
            amplitude = 30
            f = amplitude*math.sin(omega * (pygame.time.get_ticks()/1000)) + 440
            robot.setBuzzerFrequency(f)
        else:
            robot.setBuzzerFrequency(0)


        clock.tick(20)

    pygame.quit()

if __name__ == '__main__':
    main()
