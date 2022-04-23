# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:23:17 2022

@author: ophidian
"""

from gpiozero import LED 
from gpiozero import MotionSensor

green_led = LED(17) #I believe that the number is in reference to either the GPIO pin connecting to the LED or the breadboard slot
pir = MotionSensor(4) #Unfortunately, idk what the '4' is referring to

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    green_led.on()
    pir.wait_for_no_motion()
    green_led.off()
    print("Motion Stopped")