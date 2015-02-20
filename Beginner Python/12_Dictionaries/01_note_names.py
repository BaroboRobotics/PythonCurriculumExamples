# File: 01_note_names.py

import time  # for time.sleep()                                                  
import linkbot                                                                   
                                                                
myLinkbot = linkbot.Linkbot('ABCD')  # Replace 'ABCD' with your Linkbot's ID   
 
def playNote(linkbot, note):  # 1                                                
    notes = { 'Do' : 261.63,  # 2                                                    
              'Re' : 293.66,                                                     
              'Mi' : 329.63,                                                     
              'Fa' : 349.23,                                                     
              'Sol': 392.00,                                                     
              'La' : 440,                                                        
              'Ti' : 493.88 }                                                    
    linkbot.setBuzzerFrequency( notes[note] )                                    
    time.sleep(0.5)                                                              
    linkbot.setBuzzerFrequency(0)                                                
 
mySong = [         # 3                                                           
    'Do', 'Do',                                                                  
    'Sol', 'Sol',                                                                
    'La', 'La',                                                                  
    'Sol', 'Sol',                                                                
    'Fa', 'Fa',                                                                  
    'Mi', 'Mi',                                                                  
    'Re', 'Re',                                                                  
    'Do', 'Do',                                                                  
    ]                                                                            
 
for note in mySong:  # 4                                                         
    playNote(myLinkbot, note)