# File: 01_play_music_file.py

import time                                                                      
import linkbot                                                                   
                                                                 
myLinkbot = linkbot.Linkbot('ABCD') # Replace 'ABCD' with your Linkbot's ID                                                 
 
def noteToFreq(note):                                                            
    # First, we need to figure out where the note is relative to 'A'.            
    # For instance, 'B' is 2 half-steps above A, 'C' is 9 half-steps             
    # below 'A'. Lets create a dictionary called "note-offset" and store         
    # all of our offsets from A in the dictionary.                               
    noteOffsets = {                                                              
        'C' : -9,                                                                
        'D' : -7,                                                                
        'E' : -5,                                                                
        'F' : -4,                                                                
        'G' : -2,                                                                
        'A' : 0,                                                                 
        'B' : 2 }                                                                
    # Find our offset                                                            
    offset = noteOffsets[ note[0].upper() ]  # 1                                      
    # See if there is a sharp or flat                                            
    if note[1] == '#':                                                           
        offset += 1                                                              
    elif note[1] == 'b':                                                         
        offset -= 1                                                              
    # Calculate the offset based on the octave                                   
    octave = int(note[-1])  # 2                                                       
    offset += (octave)*12                                                        
 
    # Calculate the note frequency                                                                                              
    freq = 2**((offset)/12)*27.5                                                 
    return freq                                                                                                  
 
musicFile = open('fur_elise.txt', 'r')                                                                           
for line in musicFile:  # 3                                                                                           
    data = line.split()  # 4                                                                                         
    myLinkbot.setBuzzerFrequency(noteToFreq(data[0]))                                                            
    time.sleep( float(data[1]) )                                                                                 
    myLinkbot.setBuzzerFrequency(0)