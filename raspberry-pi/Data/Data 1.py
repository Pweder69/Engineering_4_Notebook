import time
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore



sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = adafruit_mpu6050.MPU6050(i2c)

led = digitalio.DigitalInOut(board.LED)
tiltLED = digitalio.DigitalInOut(board.GP16)


for x in [led, tiltLED]:
    x.direction = digitalio.Direction.OUTPUT


with open("/data.csv", "a") as datalog:
    #this line opens the file data.txt and appends info to the end of it
    datalog.write(f" -----, ------, ------, -------, ------ \n")
    while True:
        curTime = time.monotonic() # type: ignore
        
        acc = mpu.acceleration

        added = [round(x,3) for x in acc ] 
        
       
        if abs(acc[0]) > 9.3 or abs(acc[1]) > 9.3:
            tiltLED.value = True
        else:
            tiltLED.value = False
       
        datalog.write(f" {curTime}, {added[0]}, {added[1]}, {added[2]}, {tiltLED.value} \n")
        
        datalog.flush()
        led.value = True
        time.sleep(0.25)
        led.value = False
        time.sleep(0.25)