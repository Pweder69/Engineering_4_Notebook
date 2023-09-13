import board # type: ignore
import time
import digitalio # type: ignore
import pwmio # type: ignore
from adafruit_motor import servo # type: ignore
import math

pwm_servo    = pwmio.PWMOut(board.GP21, duty_cycle=2 ** 15, frequency=50)
pwm_servo.angle = 0

RedLED = digitalio.DigitalInOut(board.GP19)
BlueLED = digitalio.DigitalInOut(board.GP13)
button = digitalio.DigitalInOut(board.GP20)

button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP



for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT
    

while True:
    if not button.value():
        
        for x in range(7):
            RedLED.value = True
            time.sleep(.25)
            RedLED.value = False
            time.sleep(.25)
        
        for x in range(180):
            time.sleep(3/180)
            servo.angle = x
            
            if x % 60 == 0:
                BlueLED.value = not BlueLED.value
                