import board # type: ignore
import time
import digitalio # type: ignore
import pwmio # type: ignore
from adafruit_motor import servo # type: ignore
import math

pwm   = pwmio.PWMOut(board.GP21, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

servo1.angle = 0

RedLED = digitalio.DigitalInOut(board.GP19)
BlueLED = digitalio.DigitalInOut(board.GP13)
button = digitalio.DigitalInOut(board.GP20)

button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP



for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT
    

while True:
    if not button.value:
        
        
        for x in range(7): # Traditional countdown loop that doesnt use servo
            RedLED.value = True
            time.sleep(.5)
            RedLED.value = False
            time.sleep(.5)
    
        for x in range(1,181): # counts through 180 degrees of the servo
            time.sleep(3/180) # sleep for 3/180 of a second every loop to make it take 3 seconds
            
            servo1.angle = x # sets the servo angle to aproach 180 degrees at the end of the loop

            if x % 30 == 0: # flip every 30 degrees which is every second 
                print("Blink")
                RedLED.value = not RedLED.value
                
        BlueLED = True
    