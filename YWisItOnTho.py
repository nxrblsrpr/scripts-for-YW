# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:45:49 2022

@author: ophidian
"""

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) #I believe that the '26' refers to the GPIO slot 26
#GPIO.output(26, GPIO.HIGH)
#GPIO.output(26, GPIO.LOW)

"""
Be cautious with the following code; it outputs voltage to the specified GPIO pin


for i in range(5):
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.3) #I believe that the '0.3' is 0.3 seconds
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.3)
    
"""


while True:
    if GPIO.input(26) == 0:
        # Turn off
        #GPIO.output(26, GPIO.LOW)

#You can "uncomment" the line above ONLY once you fully understand how your Pi will respond to the command

        print("something different") #Consider this as response option A
    else:
        # Turn on
        #GPIO.output(26, GPIO.HIGH)

#You can "uncomment" the line above ONLY once you fully understand how your Pi will respond to the command

        print("something else") #Consider this as response option B