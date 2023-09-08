import board # type: ignore
import time
import digitalio # type: ignore


RedLED = digitalio.DigitalInOut(board.GP13)
BlueLED = digitalio.DigitalInOut(board.GP18)

for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT
    
for x in range(10):
    RedLED.value = True
    time.sleep(.5)
    RedLED.value = False
    time.sleep(.5)

BlueLED.value = True
time.sleep(2.5)
BlueLED = False

  