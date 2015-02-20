# File: 03_linkbot_freefall_detector.py

import math  # for math.sqrt()                                                                      
                                                                                 
def accelMag(accel):                                                             
    return math.sqrt( accel[0]**2 + accel[1]**2 + accel[2]**2 )                  
                                                                                 
import linkbot                                                                 
import time  # for time.sleep()                                                                      
                                                             
myLinkbot = linkbot.Linkbot('ABCD')  # Replace 'ABCD' with your Linkbot's Serial ID                                                 
                                                                                 
print('Gently toss your Linkbot into the air. Type Ctrl-C to quit the program.') 
                                                                                 
while True:                                                                      
    accel = myLinkbot.getAccelerometer()                                     
    if accelMag(accel) < 0.2:                 # 1                                    
        myLinkbot.setBuzzerFrequency(440)     # 2                                   
        print('Wheeee!')                                                         
        time.sleep(1)                                                            
        myLinkbot.setBuzzerFrequency(0)