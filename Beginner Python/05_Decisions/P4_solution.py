import linkbot
import time # So we can use time.sleep() later
 
myLinkbot = linkbot.Linkbot('4qfs') # Replace abcd with your Linkbot's serial ID
 
while True: # This is an infinite loop. Get out by using the "break" statement
    command = input('Please enter a robot command or "quit" to exit the program: ')
    if command == 'forward':
        # Rotate the wheels 180 degrees to move the robot forward
        myLinkbot.move(180, 0, -180) # Motor 3 has to spin in the negative direction to move the robot forward
    elif command == 'backward':
        myLinkbot.move(-180, 0, 180)
    elif command == 'turnright':
        myLinkbot.move(180, 0, 180)
    elif command == 'turnleft':
        myLinkbot.move(-180, 0, -180)
    elif command == 'beep':
        myLinkbot.setBuzzerFrequency(440)
        time.sleep(1)
        myLinkbot.setBuzzerFrequency(0)
    elif command == 'quit':
        break
    else:
        print('I\'m sorry. I don\'t understand that command.')
 
print('Goodbye!')

