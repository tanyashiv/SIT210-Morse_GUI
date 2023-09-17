# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO #Import the RPi.GPIO library for Raspberry Pi GPIO control
import time # Import the time library for creating delays
GPIO.setmode(GPIO.BOARD)    # Set the GPIO pin numbering mode to use the physical pin numbers
GPIO.setup(19, GPIO.OUT)    # Set up GPIO pin 19 as an output pin

try:
    while 1:       # Run an infinite loop 
        GPIO.output(19, GPIO.HIGH)     # Run an infinite loop 
        time.sleep(0.25)    # Sleep for 0.25 seconds
        GPIO.output(19, GPIO.LOW)    # Turn the GPIO pin 19 OFF
        time.sleep(0.25)     # Sleep for another 0.25 seconds
        print("blinking")    # Print a message to indicate that the LED is blinking
except KeyboardInterrupt:   # Catch the KeyboardInterrupt exception
    GPIO.cleanup()      # Clean up and reset GPIO configuration
