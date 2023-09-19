import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore

sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    acc = mpu.acceleration
    
    added = [] # created added so i dont have to change the format everytime i want to print
    for x in acc: # loops over acc tuple rounds the value and stores it in a new list.
        added.append(round(x,3)) # rounds to 3 decimal places
        
    print(f"x:{added[0]} y:{added[1]} z:{added[2]}") # prints the values labeled with x y and z.
    