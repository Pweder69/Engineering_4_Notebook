# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Led Blink](#led_blink)
* [Countdown](#countdown)
* [Countdown 2](#countdown-2)
* [Countdown 3](#countdown-3)
* [Countdown 4](#countdown-4)
* [Crash Avoidance Part 1](#Crash-Avoidance-Part-1)
* [Crash Avoidance Part 2](#Crash-Avoidance-Part-2)
* [Crash Avoidance Part 3](#Crash-Avoidance-Part-3)

&nbsp;


## Led Blink

### Assignment Description
This Assignment was a part of the pico introduction. It was a simple assignment to get us used to the Raspberry Pi and the Python language. The assignment was to make an LED blink on and off.

### Evidence
<img src="images\ezgif-1-d6a6a94ac0.gif" width="300" height="300">


### Code
```python
import time 
import board # type: ignore
import digitalio # type: ignore

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5) 
```

### Reflection 
This assignment was very simple and easy to do and in my opinion was basicaly a settup test for VS code. I had no problems with this assignment and it was a good way to get used to the Raspberry Pi and the Python language. 

## Countdown

### Assignment Description
In this assignment we where tasked with making a countdown timer, counting down from 10 to 0, with a interval of 1 second.

### Evidence
<img src="images\ezgif-3-d1a797db5a.gif" width="300" height="300">

### Code
```python
import time

for x in range(10):
    print(10-x)
    time.sleep(1)
print("Blast Off!")
```

### Reflection
This assignment was again very easy and simple. I had no problems and all i did was use a for loop to countdown. I also used the time.sleep() function to make the program wait for 1 second before printing the next number. It was a good way to refresh on the python syntax.

---

## Countdown 2 


### Assignment Description
In this assignment we where tasked with creating a countdowntime but one that signaled the countdown with an LED. The LED would blink once every second and when the countdown reached 0 another LED would turn on.

### Evidence

### Code
```python
RedLED = digitalio.DigitalInOut(board.GP19)
BlueLED = digitalio.DigitalInOut(board.GP13)
# INNITS 


for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT

    
for x in range(10): # make led blink 10 times to represent countdown
    BlueLED.value = True
    time.sleep(.25)
    BlueLED.value = False
    time.sleep(.25)
    
RedLED.value = True
time.sleep(10) # wait 10 seconds with red LED on
RedLED.value = False
```

## Video



https://github.com/Pweder69/Engineering_4_Notebook/assets/112962227/4ddb7952-9454-4dd3-ae60-19218dd3f250

### Reflection
This assignment was a bit harder but really still very easy. All i had to do is just run a basic for loop that runs the turn led off and then on again 10 times. Then i just had to turn the red led on for 10 seconds. There were no major design choices as this is practically just controlling 2 leds i doubught that two people could come up with a drasticaly diffrent solution for this problem.

---

## Countdown 3
 
### Assignment Description
I did the "spicy" version of this assignment this entailed me to make a system that "aborted" the launch on the second button press. This would then reset the countdown to the original state of waiting for the first button press.


### Evidence


<details>

<summary> CODE</summary>

```python
RedLED = digitalio.DigitalInOut(board.GP19)
BlueLED = digitalio.DigitalInOut(board.GP13)
Button = digitalio.DigitalInOut(board.GP20)

Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP



for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT
    
    
oldval = False


def delayCheck(waitTime):
    global Button,oldval

    
    # print(Button.value, oldval) #DEBUG
    time1 = time.time()
    
    # operates like a sleep but checks for button press and aborts if pressed
    
    
    while time.time() - time1 < waitTime:
        # print(oldval, Button.value) #DEBUG
        if Button.value == False and oldval:
            print("Aborted")
            RedLED.value = False
            BlueLED.value = False
            oldval = True
            # if pressed recursivly call countdown to start the loop in the loop
            countdown()
            
        
        oldval = Button.value
        
    
    
    
def countdown():
    global RedLED, BlueLED, Button,oldval
    
    
    
    while True:
        if Button.value == False and oldval: # false means pressed
            # print(Button.value, oldval) #DEBUG
            
            oldval = False
            
            for x in range(5):

                RedLED.value = True
                delayCheck(1)
                RedLED.value = False
                delayCheck(1)
            
            #
            #DOESNT MATTER For recusion
            #    
            
            BlueLED.value = True
            time.sleep(2.5)
            BlueLED.value = False
        oldval = Button.value
countdown()
```

</details>

#### Video

https://github.com/Pweder69/Engineering_4_Notebook/assets/112962227/c163b2c7-e478-47ed-bc55-8aa9de551932


#### Wiring
<img src = "images/wirin%20countdown%203.png" width =300>

### Reflection
This assignments was by far the hardest specificaly becasue of the spicy. The solution for me was to use recursion to call the loop again on "abort" this was not the hard part as encapsulating was relativly easy. The hardest part by far was getting the debounce loop correct as you have to make sure the debounce enters the loop without imediatly aborting and then after still updating the button and also debouncing abort so it wouldnt infinity loop to crash the whole thing.


---

## Countdown 4 

### Assignment Description
In this assignment we were tasked with creating a countodwn similiarly as last time using a button to start. This time we had to incorporate a servo into the mix. The servo would start at 0 degrees and then move to 180 degrees over the course of the last 3 seconds of the countdown.


### Evidence


#### Video


https://github.com/Pweder69/Engineering_4_Notebook/assets/112962227/b9baa222-bc16-4262-962b-d77aec0a1b0b



#### Wiring
<img src = "images/wirein%204.png" width =300>

#### Code

https://github.com/Pweder69/Engineering_4_Notebook/blob/fc1bf041284bd25b0e908ca2471cf235cd8136b1/raspberry-pi/Countdown4.py

### Reflection

This assignmnet was fun and easy to do as the problem was inivative i thought my solution was good although to complicated and looping over a set of degrees instead of time was overcomplicated. It also was good becaue it allowed me to learn how to use a servo again and all the intricacy of the servo library.

---

## Crash Avoidance Part 1

### Assignment Description
We were tasked with adding a **mpu6050(Accelerometer)** to our board and then printing out the values that it gave us rounded to the third decimal place.

### Evidence

#### Video
<img src = "images/ACC1 vid.gif" width = 400>

#### Wiring
<img src = "images\acc1 Wirein.png" width = 400>



<details open>
<summary>Code</summary>
<br>

```python
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
```
</details>

### Reflection 
This assignment was nice way to get intoduced to more complex components as i have never used a board like this before. The one design choice made was to loop over the tuple and round each value into a new list. That solution is typicaly used for larger data but i did it becasue it would allow me to easily effect the format of the print statement without having to change every print statment if i were to print every value individualy.

---
## Crash Avoidance Part 2

### Assignment Description
In this assignment we were tasked with printing the values of the accelerometer, to turn on an led if the device is rotated $\degree{90}$, and to attach a battery pack to the device to make it run on its own.


### Evidence

#### Video
<img src = "images/ACC2.gif" width = 400>

#### Wiring
<img src =  "images/acc2%20wirin.png" width = 400>

<details open>
<summary>Code</summary>
<br>

```python
led = digitalio.DigitalInOut(board.GP16)

for x in [led]:
    x.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)   

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    acc = mpu.acceleration
    
    roundlist = [] # created roundlist so i dont have to change the format everytime i want to print
    for x in acc: # loops over acc tuple rounds the value and stores it in a new list.
        roundlist.append(round(x,3)) # rounds to 3 decimal places
        
    print(f"x:{roundlist[0]} y:{roundlist[1]} z:{roundlist[2]}") # prints the values labeled with x y and z.
    
    if abs(acc[0]) > 9.3 or abs(acc[1]) > 9.3: # takes the absolute value of the x and y values and if they  
        led.value = True                       # are above 9.3 it turns on the led
    else:
        led.value = False    
```

</details>

### Reflection
I liked this assignment because it let us look at what the values mean and what the change in that value can mean. The value of the accelerometer thats constant when still is its "gravity" therefore if we rotate the device 90 degrees the gravity will be on the x axis and the y axis will be 0. This is why we can use the absolute value of the x and y values to determine if the device is rotated 90 degrees.  

---
## Crash Avoidance Part 3

### Assignment Description
In this assignment we were tasked with ataching an lcd onto the pico and then print the values of the accelerometer to the lcd.

### Evidence

#### Video
<img src = "images/ACC3.gif" width = 400>


#### Wiring
<img src = "images/acc3_bb.png" width =400>

<details open>
<summary>Code</summary>

```python
from adafruit_display_text import label #type: ignore
import adafruit_displayio_ssd1306 #type: ignore
import terminalio #type: ignore
import displayio #type: ignore
import adafruit_mpu6050 # type: ignore  
import busio # type: ignore
import board # type: ignore
import digitalio # type: ignore
import math
displayio.release_displays()



led = digitalio.DigitalInOut(board.GP16)

for x in [led]:
    x.direction = digitalio.Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)   

display_bus = displayio.I2CDisplay(i2c, device_address= 0x3d ,reset=board.GP10)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = adafruit_mpu6050.MPU6050(i2c,address = 0x68 ) # 0x68 is the address of the MPU6050

splash = displayio.Group()

title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

display.show(splash)

while True:
    gyro = mpu.gyro
    
    RL = [] # created roundlist so i dont have to change the format everytime i want to print
    for x in gyro: # loops over acc tuple rounds the value and stores it in a new list.
        RL.append(round(x,3)) # rounds to 3 decimal places
    
    text_area.text = f"{RL[0]} {RL[1]} {RL[2]}"
    
    acc = mpu.acceleration
    
    RL2 = [] # created roundlist so i dont have to change the format everytime i want to print
    for x in acc: # loops over acc tuple rounds the value and stores it in a new list.
        RL2.append(round(x,3)) # rounds to 3 decimal places
        
    print(f"x:{RL2[0]} y:{RL2[1]} z:{RL2[2]}") # prints the values labeled with x y and z.
    
    if abs(acc[0]) > 9 or abs(acc[1]) > 9: # takes the absolute value of the x and y values and if they  
        led.value = True                       # are above 9.3 it turns on the led
    else:
        led.value = False     
```

</details>

### Reflection
This assignments was a into into the annoying lcd class although i dont feel like figuring out the nuance of printing to the lcd i see its aplication as an independant display. Although the display was anoying it was relativly plug and play especially with wiring and code as there is no design just simple printing.

--- 

## Beam part 1

### Assignment Description
In this assignment we were tasked with creating a that would hold the maximum amount of weight possible. The beam had to be 3d printed so no angles over 
$\degree{45}$ could be used. An example of a basic beam would be the beam below
&darr;

<img width = 200 src="images/Idea%201%20Copy%201.png">

### Part 
```stl
solid Mesh
  facet normal 0 0.707107 0.707107
    outer loop
      vertex 15 8.3 0
      vertex 15 7 1.3
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 0 0.707107 0.707107
    outer loop
      vertex 15 7 1.3
      vertex 188.81 7 1.3
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 16.3 -2.22452 2.6
      vertex 16.3 2.22452 2.6
      vertex 16.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 16.3 2.22452 2.6
      vertex 16.3 2.22452 4.40168
      vertex 16.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 24.8 2.22452 12.9017
      vertex 24.8 -2.22452 12.9017
      vertex 23.9854 2.22452 12.0871
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 24.8 -2.22452 12.9017
      vertex 23.9854 -2.22452 12.0871
      vertex 23.9854 2.22452 12.0871
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 23.9854 2.22452 12.0871
      vertex 23.9854 -2.22452 12.0871
      vertex 21.1139 2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 23.9854 -2.22452 12.0871
      vertex 21.1139 -2.22452 9.21554
      vertex 21.1139 2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 21.1139 2.22452 9.21554
      vertex 21.1139 -2.22452 9.21554
      vertex 19.7688 2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 21.1139 -2.22452 9.21554
      vertex 19.7688 -2.22452 7.87045
      vertex 19.7688 2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 19.7688 2.22452 7.87045
      vertex 19.7688 -2.22452 7.87045
      vertex 18.7016 2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 19.7688 -2.22452 7.87045
      vertex 18.7016 -2.22452 6.80323
      vertex 18.7016 2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 18.7016 2.22452 6.80323
      vertex 18.7016 -2.22452 6.80323
      vertex 16.3 2.22452 4.40168
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 18.7016 -2.22452 6.80323
      vertex 16.3 -2.22452 4.40168
      vertex 16.3 2.22452 4.40168
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 33.3 2.22452 4.40168
      vertex 33.3 -2.22452 4.40168
      vertex 30.8984 2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 33.3 -2.22452 4.40168
      vertex 30.8984 -2.22452 6.80323
      vertex 30.8984 2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707106
    outer loop
      vertex 30.8984 2.22452 6.80323
      vertex 30.8984 -2.22452 6.80323
      vertex 29.8312 2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707106
    outer loop
      vertex 30.8984 -2.22452 6.80323
      vertex 29.8312 -2.22452 7.87045
      vertex 29.8312 2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 29.8312 2.22452 7.87045
      vertex 29.8312 -2.22452 7.87045
      vertex 28.4861 2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 29.8312 -2.22452 7.87045
      vertex 28.4861 -2.22452 9.21554
      vertex 28.4861 2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 28.4861 2.22452 9.21554
      vertex 28.4861 -2.22452 9.21554
      vertex 25.6146 2.22452 12.0871
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 28.4861 -2.22452 9.21554
      vertex 25.6146 -2.22452 12.0871
      vertex 25.6146 2.22452 12.0871
    endloop
  endfacet
  facet normal -0.707107 0 -0.707106
    outer loop
      vertex 25.6146 2.22452 12.0871
      vertex 25.6146 -2.22452 12.0871
      vertex 24.8 2.22452 12.9017
    endloop
  endfacet
  facet normal -0.707107 0 -0.707106
    outer loop
      vertex 25.6146 -2.22452 12.0871
      vertex 24.8 -2.22452 12.9017
      vertex 24.8 2.22452 12.9017
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 33.3 -2.22452 4.40168
      vertex 33.3 2.22452 4.40168
      vertex 33.3 -2.22452 2.6
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 33.3 2.22452 4.40168
      vertex 33.3 2.22452 2.6
      vertex 33.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 33.3 -2.22452 2.6
      vertex 33.3 2.22452 2.6
      vertex 16.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 33.3 2.22452 2.6
      vertex 16.3 2.22452 2.6
      vertex 16.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 36.3 -2.22452 2.77245
      vertex 36.3 -2.22452 2.6
      vertex 36.3 2.22452 2.77245
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 36.3 -2.22452 2.6
      vertex 36.3 2.22452 2.6
      vertex 36.3 2.22452 2.77245
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 36.3 -2.22452 2.77245
      vertex 36.3 2.22452 2.77245
      vertex 40.3308 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 36.3 2.22452 2.77245
      vertex 40.3308 2.22452 6.80323
      vertex 40.3308 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 40.3308 -2.22452 6.80323
      vertex 40.3308 2.22452 6.80323
      vertex 41.398 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 40.3308 2.22452 6.80323
      vertex 41.398 2.22452 7.87045
      vertex 41.398 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 41.398 -2.22452 7.87045
      vertex 41.398 2.22452 7.87045
      vertex 42.7431 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 41.398 2.22452 7.87045
      vertex 42.7431 2.22452 9.21554
      vertex 42.7431 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 42.7431 -2.22452 9.21554
      vertex 42.7431 2.22452 9.21554
      vertex 44.8 -2.22452 11.2724
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 42.7431 2.22452 9.21554
      vertex 44.8 2.22452 11.2724
      vertex 44.8 -2.22452 11.2724
    endloop
  endfacet
  facet normal -0.707106 0 -0.707107
    outer loop
      vertex 44.8 -2.22452 11.2724
      vertex 44.8 2.22452 11.2724
      vertex 46.8569 -2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707106 0 -0.707107
    outer loop
      vertex 44.8 2.22452 11.2724
      vertex 46.8569 2.22452 9.21554
      vertex 46.8569 -2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 46.8569 -2.22452 9.21554
      vertex 46.8569 2.22452 9.21554
      vertex 48.202 -2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 46.8569 2.22452 9.21554
      vertex 48.202 2.22452 7.87045
      vertex 48.202 -2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 48.202 -2.22452 7.87045
      vertex 48.202 2.22452 7.87045
      vertex 49.2692 -2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 48.202 2.22452 7.87045
      vertex 49.2692 2.22452 6.80323
      vertex 49.2692 -2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 49.2692 -2.22452 6.80323
      vertex 49.2692 2.22452 6.80323
      vertex 53.3 -2.22452 2.77245
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 49.2692 2.22452 6.80323
      vertex 53.3 2.22452 2.77245
      vertex 53.3 -2.22452 2.77245
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 53.3 -2.22452 2.77245
      vertex 53.3 2.22452 2.77245
      vertex 53.3 -2.22452 2.6
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 53.3 2.22452 2.77245
      vertex 53.3 2.22452 2.6
      vertex 53.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 53.3 -2.22452 2.6
      vertex 53.3 2.22452 2.6
      vertex 36.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 53.3 2.22452 2.6
      vertex 36.3 2.22452 2.6
      vertex 36.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 56.3 -2.22452 3.30614
      vertex 56.3 -2.22452 2.6
      vertex 56.3 2.22452 3.30614
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 56.3 -2.22452 2.6
      vertex 56.3 2.22452 2.6
      vertex 56.3 2.22452 3.30614
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 56.3 -2.22452 3.30614
      vertex 56.3 2.22452 3.30614
      vertex 59.7971 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 56.3 2.22452 3.30614
      vertex 59.7971 2.22452 6.80323
      vertex 59.7971 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.707108 0 -0.707106
    outer loop
      vertex 59.7971 -2.22452 6.80323
      vertex 59.7971 2.22452 6.80323
      vertex 60.8643 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707108 0 -0.707106
    outer loop
      vertex 59.7971 2.22452 6.80323
      vertex 60.8643 2.22452 7.87045
      vertex 60.8643 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0.707106 0 -0.707108
    outer loop
      vertex 60.8643 -2.22452 7.87045
      vertex 60.8643 2.22452 7.87045
      vertex 62.2094 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707106 0 -0.707108
    outer loop
      vertex 60.8643 2.22452 7.87045
      vertex 62.2094 2.22452 9.21554
      vertex 62.2094 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0.707108 0 -0.707105
    outer loop
      vertex 62.2094 -2.22452 9.21554
      vertex 62.2094 2.22452 9.21554
      vertex 62.8 -2.22452 9.80614
    endloop
  endfacet
  facet normal 0.707108 0 -0.707105
    outer loop
      vertex 62.2094 2.22452 9.21554
      vertex 62.8 2.22452 9.80614
      vertex 62.8 -2.22452 9.80614
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 69.3 2.22452 3.30614
      vertex 69.3 -2.22452 3.30614
      vertex 65.8029 2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 69.3 -2.22452 3.30614
      vertex 65.8029 -2.22452 6.80323
      vertex 65.8029 2.22452 6.80323
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 65.8029 2.22452 6.80323
      vertex 65.8029 -2.22452 6.80323
      vertex 64.7357 2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 65.8029 -2.22452 6.80323
      vertex 64.7357 -2.22452 7.87045
      vertex 64.7357 2.22452 7.87045
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 64.7357 2.22452 7.87045
      vertex 64.7357 -2.22452 7.87045
      vertex 63.3906 2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 64.7357 -2.22452 7.87045
      vertex 63.3906 -2.22452 9.21554
      vertex 63.3906 2.22452 9.21554
    endloop
  endfacet
  facet normal -0.707104 0 -0.70711
    outer loop
      vertex 63.3906 2.22452 9.21554
      vertex 63.3906 -2.22452 9.21554
      vertex 62.8 2.22452 9.80614
    endloop
  endfacet
  facet normal -0.707104 0 -0.70711
    outer loop
      vertex 63.3906 -2.22452 9.21554
      vertex 62.8 -2.22452 9.80614
      vertex 62.8 2.22452 9.80614
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 69.3 -2.22452 3.30614
      vertex 69.3 2.22452 3.30614
      vertex 69.3 -2.22452 2.6
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 69.3 2.22452 3.30614
      vertex 69.3 2.22452 2.6
      vertex 69.3 -2.22452 2.6
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 12 10 9
      vertex 12 10 3
      vertex 12 -10 9
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 12 10 3
      vertex 12 -10 3
      vertex 12 -10 9
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 69.3 -2.22452 2.6
      vertex 69.3 2.22452 2.6
      vertex 56.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 69.3 2.22452 2.6
      vertex 56.3 2.22452 2.6
      vertex 56.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 3 -10 3
      vertex 12 -10 3
      vertex 3 10 3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 12 -10 3
      vertex 12 10 3
      vertex 3 10 3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 3 -10 9
      vertex 3 -10 3
      vertex 3 10 9
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 3 -10 3
      vertex 3 10 3
      vertex 3 10 9
    endloop
  endfacet
  facet normal -1 0 -1.73472e-16
    outer loop
      vertex 0 -10 0
      vertex -2.60209e-15 -10 15
      vertex 0 10 0
    endloop
  endfacet
  facet normal -1 0 -1.73472e-16
    outer loop
      vertex -2.60209e-15 -10 15
      vertex -2.60209e-15 10 15
      vertex 0 10 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15 -10 0
      vertex 0 -10 0
      vertex 15 -8.3 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 -10 0
      vertex 0 10 0
      vertex 15 -8.3 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15 -8.3 0
      vertex 0 10 0
      vertex 15 8.3 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0 10 0
      vertex 15 10 0
      vertex 15 8.3 0
    endloop
  endfacet
  facet normal -6.63934e-18 -1.29008e-17 -1
    outer loop
      vertex 186.2 -2.90514e-16 -5.89806e-16
      vertex 186.215 -0.275703 -5.86349e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal -3.80987e-18 -3.85437e-17 -1
    outer loop
      vertex 186.215 -0.275703 -5.86349e-16
      vertex 186.26 -0.548175 -5.76017e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 6.05489e-15 -3.15694e-16 -1
    outer loop
      vertex 191.3 -6.02799e-16 5.89806e-16
      vertex 195 6.89317 2.08167e-14
      vertex 191.285 -0.275703 5.86349e-16
    endloop
  endfacet
  facet normal 2.53186e-15 1.50995e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 195 -6.89317 0
      vertex 191.285 -0.275703 5.86349e-16
    endloop
  endfacet
  facet normal -6.98802e-17 4.93766e-17 -1
    outer loop
      vertex 191.285 -0.275703 5.86349e-16
      vertex 195 -6.89317 0
      vertex 191.24 -0.548175 5.76017e-16
    endloop
  endfacet
  facet normal -3.80987e-18 3.85437e-17 -1
    outer loop
      vertex 186.26 0.548175 -5.76017e-16
      vertex 186.215 0.275703 -5.86349e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal -6.63934e-18 1.29008e-17 -1
    outer loop
      vertex 186.215 0.275703 -5.86349e-16
      vertex 186.2 -2.90514e-16 -5.89806e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 0 7.1061e-17 -1
    outer loop
      vertex 113.493 8.3 0
      vertex 186.2 -2.90514e-16 -5.89806e-16
      vertex 15 8.3 0
    endloop
  endfacet
  facet normal -4.83631e-18 -2.86952e-17 -1
    outer loop
      vertex 186.2 -2.90514e-16 -5.89806e-16
      vertex 113.493 -8.3 0
      vertex 15 8.3 0
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15 8.3 0
      vertex 113.493 -8.3 0
      vertex 15 -8.3 0
    endloop
  endfacet
  facet normal 4.9865e-15 2.57777e-16 -1
    outer loop
      vertex 191.3 -6.02799e-16 5.89806e-16
      vertex 191.285 0.275703 5.86349e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 4.267e-15 6.61688e-16 -1
    outer loop
      vertex 191.285 0.275703 5.86349e-16
      vertex 191.24 0.548175 5.76017e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 3.73976e-15 9.74096e-16 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 191.24 0.548175 5.76017e-16
      vertex 191.167 0.814219 5.58932e-16
    endloop
  endfacet
  facet normal 1.18073e-16 1.88179e-16 -1
    outer loop
      vertex 189.944 -2.25296 2.7627e-16
      vertex 190.181 -2.11061 3.30991e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 1.01183e-16 1.71162e-16 -1
    outer loop
      vertex 190.181 -2.11061 3.30991e-16
      vertex 190.401 -1.94351 3.81832e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 2.43519e-17 3.43945e-16 -1
    outer loop
      vertex 187.556 2.25296 -2.7627e-16
      vertex 187.319 2.11061 -3.30991e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 8.41538e-17 1.55338e-16 -1
    outer loop
      vertex 190.401 -1.94351 3.81832e-16
      vertex 190.601 -1.75363 4.28196e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 6.63527e-17 1.40103e-16 -1
    outer loop
      vertex 190.601 -1.75363 4.28196e-16
      vertex 190.78 -1.54319 4.6954e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 4.70816e-17 1.24902e-16 -1
    outer loop
      vertex 195 -6.89317 0
      vertex 190.78 -1.54319 4.6954e-16
      vertex 190.935 -1.31466 5.05379e-16
    endloop
  endfacet
  facet normal 2.54452e-17 1.09136e-16 -1
    outer loop
      vertex 190.935 -1.31466 5.05379e-16
      vertex 191.064 -1.07072 5.35293e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 2.05636e-19 9.20751e-17 -1
    outer loop
      vertex 191.064 -1.07072 5.35293e-16
      vertex 191.167 -0.814219 5.58932e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal -3.05271e-17 7.26946e-17 -1
    outer loop
      vertex 195 -6.89317 0
      vertex 191.167 -0.814219 5.58932e-16
      vertex 191.24 -0.548175 5.76017e-16
    endloop
  endfacet
  facet normal 3.32781e-15 1.23388e-15 -1
    outer loop
      vertex 191.167 0.814219 5.58932e-16
      vertex 191.064 1.07072 5.35293e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 2.98975e-15 1.46239e-15 -1
    outer loop
      vertex 191.064 1.07072 5.35293e-16
      vertex 190.935 1.31466 5.05379e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 2.69984e-15 1.67364e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 190.935 1.31466 5.05379e-16
      vertex 190.78 1.54319 4.6954e-16
    endloop
  endfacet
  facet normal 7.58373e-18 1.51681e-16 -1
    outer loop
      vertex 186.72 1.54319 -4.6954e-16
      vertex 186.565 1.31466 -5.05379e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal -1.04382e-18 -6.45088e-17 -1
    outer loop
      vertex 186.26 -0.548175 -5.76017e-16
      vertex 186.333 -0.814219 -5.58932e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 1.72685e-18 -9.1469e-17 -1
    outer loop
      vertex 186.333 -0.814219 -5.58932e-16
      vertex 186.436 -1.07072 -5.35293e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 4.57438e-18 -1.202e-16 -1
    outer loop
      vertex 113.493 -8.3 0
      vertex 186.436 -1.07072 -5.35293e-16
      vertex 186.565 -1.31466 -5.05379e-16
    endloop
  endfacet
  facet normal 7.58373e-18 -1.51681e-16 -1
    outer loop
      vertex 186.565 -1.31466 -5.05379e-16
      vertex 186.72 -1.54319 -4.6954e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 1.08646e-17 -1.87237e-16 -1
    outer loop
      vertex 186.72 -1.54319 -4.6954e-16
      vertex 186.899 -1.75363 -4.28196e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 1.45707e-17 -2.28795e-16 -1
    outer loop
      vertex 113.493 -8.3 0
      vertex 186.899 -1.75363 -4.28196e-16
      vertex 187.099 -1.94351 -3.81832e-16
    endloop
  endfacet
  facet normal 4.57438e-18 1.202e-16 -1
    outer loop
      vertex 186.565 1.31466 -5.05379e-16
      vertex 186.436 1.07072 -5.35293e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 1.72685e-18 9.1469e-17 -1
    outer loop
      vertex 186.436 1.07072 -5.35293e-16
      vertex 186.333 0.814219 -5.58932e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal -1.04382e-18 6.45088e-17 -1
    outer loop
      vertex 113.493 8.3 0
      vertex 186.333 0.814219 -5.58932e-16
      vertex 186.26 0.548175 -5.76017e-16
    endloop
  endfacet
  facet normal 3.40638e-16 4.96736e-16 -1
    outer loop
      vertex 188.068 -2.45705 -1.5779e-16
      vertex 188.337 -2.51641 -9.542e-17
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 2.44149e-15 1.87742e-15 -1
    outer loop
      vertex 190.78 1.54319 4.6954e-16
      vertex 190.601 1.75363 4.28196e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 2.20304e-15 2.08151e-15 -1
    outer loop
      vertex 190.601 1.75363 4.28196e-16
      vertex 190.401 1.94351 3.81832e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 1.97482e-15 2.29356e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 190.401 1.94351 3.81832e-16
      vertex 190.181 2.11061 3.30991e-16
    endloop
  endfacet
  facet normal 1.7485e-15 2.52161e-15 -1
    outer loop
      vertex 190.181 2.11061 3.30991e-16
      vertex 189.944 2.25296 2.7627e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 1.51539e-15 2.77558e-15 -1
    outer loop
      vertex 189.944 2.25296 2.7627e-16
      vertex 189.694 2.36889 2.1831e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 1.26534e-15 3.06885e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 189.694 2.36889 2.1831e-16
      vertex 189.432 2.45705 1.5779e-16
    endloop
  endfacet
  facet normal 1.89369e-17 -2.79354e-16 -1
    outer loop
      vertex 187.099 -1.94351 -3.81832e-16
      vertex 187.319 -2.11061 -3.30991e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 2.43519e-17 -3.43945e-16 -1
    outer loop
      vertex 187.319 -2.11061 -3.30991e-16
      vertex 187.556 -2.25296 -2.7627e-16
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 9.99952e-19 -5.7934e-17 -1
    outer loop
      vertex 113.493 -8.3 0
      vertex 187.556 -2.25296 -2.7627e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 7.90436e-16 1.20858e-15 -1
    outer loop
      vertex 187.556 -2.25296 -2.7627e-16
      vertex 187.806 -2.36889 -2.1831e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 4.63161e-16 6.88198e-16 -1
    outer loop
      vertex 195 -6.89317 0
      vertex 187.806 -2.36889 -2.1831e-16
      vertex 188.068 -2.45705 -1.5779e-16
    endloop
  endfacet
  facet normal 2.74357e-16 3.95839e-16 -1
    outer loop
      vertex 188.337 -2.51641 -9.542e-17
      vertex 188.612 -2.54626 -3.19315e-17
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 2.31288e-16 3.32547e-16 -1
    outer loop
      vertex 188.612 -2.54626 -3.19315e-17
      vertex 188.888 -2.54626 3.19315e-17
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 1.99932e-16 2.88459e-16 -1
    outer loop
      vertex 195 -6.89317 0
      vertex 188.888 -2.54626 3.19315e-17
      vertex 189.163 -2.51641 9.542e-17
    endloop
  endfacet
  facet normal 1.75087e-16 2.55322e-16 -1
    outer loop
      vertex 189.163 -2.51641 9.542e-17
      vertex 189.432 -2.45705 1.5779e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 1.54133e-16 2.29023e-16 -1
    outer loop
      vertex 189.432 -2.45705 1.5779e-16
      vertex 189.694 -2.36889 2.1831e-16
      vertex 195 -6.89317 0
    endloop
  endfacet
  facet normal 1.35466e-16 2.0713e-16 -1
    outer loop
      vertex 195 -6.89317 0
      vertex 189.694 -2.36889 2.1831e-16
      vertex 189.944 -2.25296 2.7627e-16
    endloop
  endfacet
  facet normal 1.89369e-17 2.79354e-16 -1
    outer loop
      vertex 187.319 2.11061 -3.30991e-16
      vertex 187.099 1.94351 -3.81832e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 1.45707e-17 2.28795e-16 -1
    outer loop
      vertex 187.099 1.94351 -3.81832e-16
      vertex 186.899 1.75363 -4.28196e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 1.08646e-17 1.87237e-16 -1
    outer loop
      vertex 113.493 8.3 0
      vertex 186.899 1.75363 -4.28196e-16
      vertex 186.72 1.54319 -4.6954e-16
    endloop
  endfacet
  facet normal 9.84374e-16 3.42149e-15 -1
    outer loop
      vertex 189.432 2.45705 1.5779e-16
      vertex 189.163 2.51641 9.542e-17
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 6.51688e-16 3.8652e-15 -1
    outer loop
      vertex 189.163 2.51641 9.542e-17
      vertex 188.888 2.54626 3.19315e-17
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 2.31288e-16 4.4563e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 188.888 2.54626 3.19315e-17
      vertex 188.612 2.54626 -3.19315e-17
    endloop
  endfacet
  facet normal -3.45565e-16 5.30403e-15 -1
    outer loop
      vertex 188.612 2.54626 -3.19315e-17
      vertex 188.337 2.51641 -9.542e-17
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal -1.23386e-15 6.65623e-15 -1
    outer loop
      vertex 188.337 2.51641 -9.542e-17
      vertex 188.068 2.45705 -1.5779e-16
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 3.28153e-16 4.21532e-15 -1
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 188.068 2.45705 -1.5779e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 4.19202e-17 5.62045e-16 -1
    outer loop
      vertex 188.068 2.45705 -1.5779e-16
      vertex 187.806 2.36889 -2.1831e-16
      vertex 113.493 8.3 0
    endloop
  endfacet
  facet normal 3.15249e-17 4.31798e-16 -1
    outer loop
      vertex 113.493 8.3 0
      vertex 187.806 2.36889 -2.1831e-16
      vertex 187.556 2.25296 -2.7627e-16
    endloop
  endfacet
  facet normal 0 -0.707107 0.707107
    outer loop
      vertex 188.81 -7 1.3
      vertex 15 -7 1.3
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal 0 -0.707107 0.707107
    outer loop
      vertex 15 -7 1.3
      vertex 15 -8.3 0
      vertex 113.493 -8.3 0
    endloop
  endfacet
  facet normal -0.998534 -0.0541304 -4.82975e-17
    outer loop
      vertex 191.3 -6.02799e-16 5.89806e-16
      vertex 191.3 -1.22737e-15 0.7
      vertex 191.285 0.275703 5.86349e-16
    endloop
  endfacet
  facet normal -0.998534 -0.0541304 0
    outer loop
      vertex 191.3 -1.22737e-15 0.7
      vertex 191.285 0.275703 0.7
      vertex 191.285 0.275703 5.86349e-16
    endloop
  endfacet
  facet normal -0.986824 -0.161797 0
    outer loop
      vertex 191.285 0.275703 5.86349e-16
      vertex 191.285 0.275703 0.7
      vertex 191.24 0.548175 5.76017e-16
    endloop
  endfacet
  facet normal -0.986824 -0.161797 0
    outer loop
      vertex 191.285 0.275703 0.7
      vertex 191.24 0.548175 0.7
      vertex 191.24 0.548175 5.76017e-16
    endloop
  endfacet
  facet normal -0.963552 -0.267522 0
    outer loop
      vertex 191.24 0.548175 5.76017e-16
      vertex 191.24 0.548175 0.7
      vertex 191.167 0.814219 5.58932e-16
    endloop
  endfacet
  facet normal -0.963552 -0.267522 0
    outer loop
      vertex 191.24 0.548175 0.7
      vertex 191.167 0.814219 0.7
      vertex 191.167 0.814219 5.58932e-16
    endloop
  endfacet
  facet normal -0.928966 -0.370166 0
    outer loop
      vertex 191.167 0.814219 5.58932e-16
      vertex 191.167 0.814219 0.7
      vertex 191.064 1.07072 5.35293e-16
    endloop
  endfacet
  facet normal -0.928966 -0.370166 0
    outer loop
      vertex 191.167 0.814219 0.7
      vertex 191.064 1.07072 0.7
      vertex 191.064 1.07072 5.35293e-16
    endloop
  endfacet
  facet normal -0.883518 -0.468396 0
    outer loop
      vertex 191.064 1.07072 5.35293e-16
      vertex 191.064 1.07072 0.7
      vertex 190.935 1.31466 5.05379e-16
    endloop
  endfacet
  facet normal -0.883518 -0.468396 0
    outer loop
      vertex 191.064 1.07072 0.7
      vertex 190.935 1.31466 0.7
      vertex 190.935 1.31466 5.05379e-16
    endloop
  endfacet
  facet normal -0.8277 -0.561172 0
    outer loop
      vertex 190.935 1.31466 5.05379e-16
      vertex 190.935 1.31466 0.7
      vertex 190.78 1.54319 4.6954e-16
    endloop
  endfacet
  facet normal -0.8277 -0.561172 0
    outer loop
      vertex 190.935 1.31466 0.7
      vertex 190.78 1.54319 0.7
      vertex 190.78 1.54319 4.6954e-16
    endloop
  endfacet
  facet normal -0.762152 -0.647398 0
    outer loop
      vertex 190.78 1.54319 4.6954e-16
      vertex 190.78 1.54319 0.7
      vertex 190.601 1.75363 4.28196e-16
    endloop
  endfacet
  facet normal -0.762152 -0.647398 0
    outer loop
      vertex 190.78 1.54319 0.7
      vertex 190.601 1.75363 0.7
      vertex 190.601 1.75363 4.28196e-16
    endloop
  endfacet
  facet normal -0.687705 -0.72599 0
    outer loop
      vertex 190.601 1.75363 4.28196e-16
      vertex 190.601 1.75363 0.7
      vertex 190.401 1.94351 3.81832e-16
    endloop
  endfacet
  facet normal -0.687705 -0.72599 0
    outer loop
      vertex 190.601 1.75363 0.7
      vertex 190.401 1.94351 0.7
      vertex 190.401 1.94351 3.81832e-16
    endloop
  endfacet
  facet normal -0.605176 -0.796092 0
    outer loop
      vertex 190.401 1.94351 3.81832e-16
      vertex 190.401 1.94351 0.7
      vertex 190.181 2.11061 3.30991e-16
    endloop
  endfacet
  facet normal -0.605176 -0.796092 0
    outer loop
      vertex 190.401 1.94351 0.7
      vertex 190.181 2.11061 0.7
      vertex 190.181 2.11061 3.30991e-16
    endloop
  endfacet
  facet normal -0.515553 -0.856858 0
    outer loop
      vertex 190.181 2.11061 3.30991e-16
      vertex 190.181 2.11061 0.7
      vertex 189.944 2.25296 2.7627e-16
    endloop
  endfacet
  facet normal -0.515553 -0.856858 0
    outer loop
      vertex 190.181 2.11061 0.7
      vertex 189.944 2.25296 0.7
      vertex 189.944 2.25296 2.7627e-16
    endloop
  endfacet
  facet normal -0.419884 -0.907578 0
    outer loop
      vertex 189.944 2.25296 2.7627e-16
      vertex 189.944 2.25296 0.7
      vertex 189.694 2.36889 2.1831e-16
    endloop
  endfacet
  facet normal -0.419884 -0.907578 0
    outer loop
      vertex 189.944 2.25296 0.7
      vertex 189.694 2.36889 0.7
      vertex 189.694 2.36889 2.1831e-16
    endloop
  endfacet
  facet normal -0.319307 -0.947651 0
    outer loop
      vertex 189.694 2.36889 2.1831e-16
      vertex 189.694 2.36889 0.7
      vertex 189.432 2.45705 1.5779e-16
    endloop
  endfacet
  facet normal -0.319307 -0.947651 0
    outer loop
      vertex 189.694 2.36889 0.7
      vertex 189.432 2.45705 0.7
      vertex 189.432 2.45705 1.5779e-16
    endloop
  endfacet
  facet normal -0.21496 -0.976623 0
    outer loop
      vertex 189.432 2.45705 1.5779e-16
      vertex 189.432 2.45705 0.7
      vertex 189.163 2.51641 9.542e-17
    endloop
  endfacet
  facet normal -0.21496 -0.976623 0
    outer loop
      vertex 189.432 2.45705 0.7
      vertex 189.163 2.51641 0.7
      vertex 189.163 2.51641 9.542e-17
    endloop
  endfacet
  facet normal -0.108123 -0.994137 0
    outer loop
      vertex 189.163 2.51641 9.542e-17
      vertex 189.163 2.51641 0.7
      vertex 188.888 2.54626 3.19315e-17
    endloop
  endfacet
  facet normal -0.108123 -0.994137 0
    outer loop
      vertex 189.163 2.51641 0.7
      vertex 188.888 2.54626 0.7
      vertex 188.888 2.54626 3.19315e-17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 188.888 2.54626 3.19315e-17
      vertex 188.888 2.54626 0.7
      vertex 188.612 2.54626 -3.19315e-17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 188.888 2.54626 0.7
      vertex 188.612 2.54626 0.7
      vertex 188.612 2.54626 -3.19315e-17
    endloop
  endfacet
  facet normal 0.108123 -0.994137 0
    outer loop
      vertex 188.612 2.54626 -3.19315e-17
      vertex 188.612 2.54626 0.7
      vertex 188.337 2.51641 -9.542e-17
    endloop
  endfacet
  facet normal 0.108123 -0.994137 0
    outer loop
      vertex 188.612 2.54626 0.7
      vertex 188.337 2.51641 0.7
      vertex 188.337 2.51641 -9.542e-17
    endloop
  endfacet
  facet normal 0.214971 -0.97662 0
    outer loop
      vertex 188.337 2.51641 -9.542e-17
      vertex 188.337 2.51641 0.7
      vertex 188.068 2.45705 -1.5779e-16
    endloop
  endfacet
  facet normal 0.214971 -0.97662 0
    outer loop
      vertex 188.337 2.51641 0.7
      vertex 188.068 2.45705 0.7
      vertex 188.068 2.45705 -1.5779e-16
    endloop
  endfacet
  facet normal 0.319291 -0.947657 0
    outer loop
      vertex 188.068 2.45705 -1.5779e-16
      vertex 188.068 2.45705 0.7
      vertex 187.806 2.36889 -2.1831e-16
    endloop
  endfacet
  facet normal 0.319291 -0.947657 0
    outer loop
      vertex 188.068 2.45705 0.7
      vertex 187.806 2.36889 0.7
      vertex 187.806 2.36889 -2.1831e-16
    endloop
  endfacet
  facet normal 0.419884 -0.907578 0
    outer loop
      vertex 187.806 2.36889 -2.1831e-16
      vertex 187.806 2.36889 0.7
      vertex 187.556 2.25296 -2.7627e-16
    endloop
  endfacet
  facet normal 0.419884 -0.907578 0
    outer loop
      vertex 187.806 2.36889 0.7
      vertex 187.556 2.25296 0.7
      vertex 187.556 2.25296 -2.7627e-16
    endloop
  endfacet
  facet normal 0.515553 -0.856858 0
    outer loop
      vertex 187.556 2.25296 -2.7627e-16
      vertex 187.556 2.25296 0.7
      vertex 187.319 2.11061 -3.30991e-16
    endloop
  endfacet
  facet normal 0.515553 -0.856858 0
    outer loop
      vertex 187.556 2.25296 0.7
      vertex 187.319 2.11061 0.7
      vertex 187.319 2.11061 -3.30991e-16
    endloop
  endfacet
  facet normal 0.605176 -0.796092 0
    outer loop
      vertex 187.319 2.11061 -3.30991e-16
      vertex 187.319 2.11061 0.7
      vertex 187.099 1.94351 -3.81832e-16
    endloop
  endfacet
  facet normal 0.605176 -0.796092 0
    outer loop
      vertex 187.319 2.11061 0.7
      vertex 187.099 1.94351 0.7
      vertex 187.099 1.94351 -3.81832e-16
    endloop
  endfacet
  facet normal 0.687705 -0.72599 0
    outer loop
      vertex 187.099 1.94351 -3.81832e-16
      vertex 187.099 1.94351 0.7
      vertex 186.899 1.75363 -4.28196e-16
    endloop
  endfacet
  facet normal 0.687705 -0.72599 0
    outer loop
      vertex 187.099 1.94351 0.7
      vertex 186.899 1.75363 0.7
      vertex 186.899 1.75363 -4.28196e-16
    endloop
  endfacet
  facet normal 0.762179 -0.647367 0
    outer loop
      vertex 186.899 1.75363 -4.28196e-16
      vertex 186.899 1.75363 0.7
      vertex 186.72 1.54319 -4.6954e-16
    endloop
  endfacet
  facet normal 0.762179 -0.647367 0
    outer loop
      vertex 186.899 1.75363 0.7
      vertex 186.72 1.54319 0.7
      vertex 186.72 1.54319 -4.6954e-16
    endloop
  endfacet
  facet normal 0.827674 -0.561208 0
    outer loop
      vertex 186.72 1.54319 -4.6954e-16
      vertex 186.72 1.54319 0.7
      vertex 186.565 1.31466 -5.05379e-16
    endloop
  endfacet
  facet normal 0.827674 -0.561208 0
    outer loop
      vertex 186.72 1.54319 0.7
      vertex 186.565 1.31466 0.7
      vertex 186.565 1.31466 -5.05379e-16
    endloop
  endfacet
  facet normal 0.883518 -0.468396 0
    outer loop
      vertex 186.565 1.31466 -5.05379e-16
      vertex 186.565 1.31466 0.7
      vertex 186.436 1.07072 -5.35293e-16
    endloop
  endfacet
  facet normal 0.883518 -0.468396 0
    outer loop
      vertex 186.565 1.31466 0.7
      vertex 186.436 1.07072 0.7
      vertex 186.436 1.07072 -5.35293e-16
    endloop
  endfacet
  facet normal 0.928966 -0.370166 0
    outer loop
      vertex 186.436 1.07072 -5.35293e-16
      vertex 186.436 1.07072 0.7
      vertex 186.333 0.814219 -5.58932e-16
    endloop
  endfacet
  facet normal 0.928966 -0.370166 0
    outer loop
      vertex 186.436 1.07072 0.7
      vertex 186.333 0.814219 0.7
      vertex 186.333 0.814219 -5.58932e-16
    endloop
  endfacet
  facet normal 0.963552 -0.267522 0
    outer loop
      vertex 186.333 0.814219 -5.58932e-16
      vertex 186.333 0.814219 0.7
      vertex 186.26 0.548175 -5.76017e-16
    endloop
  endfacet
  facet normal 0.963552 -0.267522 0
    outer loop
      vertex 186.333 0.814219 0.7
      vertex 186.26 0.548175 0.7
      vertex 186.26 0.548175 -5.76017e-16
    endloop
  endfacet
  facet normal 0.986833 -0.161745 0
    outer loop
      vertex 186.26 0.548175 -5.76017e-16
      vertex 186.26 0.548175 0.7
      vertex 186.215 0.275703 -5.86349e-16
    endloop
  endfacet
  facet normal 0.986833 -0.161745 0
    outer loop
      vertex 186.26 0.548175 0.7
      vertex 186.215 0.275703 0.7
      vertex 186.215 0.275703 -5.86349e-16
    endloop
  endfacet
  facet normal 0.998531 -0.0541843 0
    outer loop
      vertex 186.215 0.275703 -5.86349e-16
      vertex 186.215 0.275703 0.7
      vertex 186.2 -2.90514e-16 -5.89806e-16
    endloop
  endfacet
  facet normal 0.998531 -0.0541843 0
    outer loop
      vertex 186.215 0.275703 0.7
      vertex 186.2 -2.90514e-16 0.7
      vertex 186.2 -2.90514e-16 -5.89806e-16
    endloop
  endfacet
  facet normal 0.998531 0.0541843 0
    outer loop
      vertex 186.2 -2.90514e-16 -5.89806e-16
      vertex 186.2 -2.90514e-16 0.7
      vertex 186.215 -0.275703 -5.86349e-16
    endloop
  endfacet
  facet normal 0.998531 0.0541843 0
    outer loop
      vertex 186.2 -2.90514e-16 0.7
      vertex 186.215 -0.275703 0.7
      vertex 186.215 -0.275703 -5.86349e-16
    endloop
  endfacet
  facet normal 0.986833 0.161745 0
    outer loop
      vertex 186.215 -0.275703 -5.86349e-16
      vertex 186.215 -0.275703 0.7
      vertex 186.26 -0.548175 -5.76017e-16
    endloop
  endfacet
  facet normal 0.986833 0.161745 0
    outer loop
      vertex 186.215 -0.275703 0.7
      vertex 186.26 -0.548175 0.7
      vertex 186.26 -0.548175 -5.76017e-16
    endloop
  endfacet
  facet normal 0.963552 0.267522 0
    outer loop
      vertex 186.26 -0.548175 -5.76017e-16
      vertex 186.26 -0.548175 0.7
      vertex 186.333 -0.814219 -5.58932e-16
    endloop
  endfacet
  facet normal 0.963552 0.267522 0
    outer loop
      vertex 186.26 -0.548175 0.7
      vertex 186.333 -0.814219 0.7
      vertex 186.333 -0.814219 -5.58932e-16
    endloop
  endfacet
  facet normal 0.928966 0.370166 0
    outer loop
      vertex 186.333 -0.814219 -5.58932e-16
      vertex 186.333 -0.814219 0.7
      vertex 186.436 -1.07072 -5.35293e-16
    endloop
  endfacet
  facet normal 0.928966 0.370166 0
    outer loop
      vertex 186.333 -0.814219 0.7
      vertex 186.436 -1.07072 0.7
      vertex 186.436 -1.07072 -5.35293e-16
    endloop
  endfacet
  facet normal 0.883518 0.468396 0
    outer loop
      vertex 186.436 -1.07072 -5.35293e-16
      vertex 186.436 -1.07072 0.7
      vertex 186.565 -1.31466 -5.05379e-16
    endloop
  endfacet
  facet normal 0.883518 0.468396 0
    outer loop
      vertex 186.436 -1.07072 0.7
      vertex 186.565 -1.31466 0.7
      vertex 186.565 -1.31466 -5.05379e-16
    endloop
  endfacet
  facet normal 0.827674 0.561208 0
    outer loop
      vertex 186.565 -1.31466 -5.05379e-16
      vertex 186.565 -1.31466 0.7
      vertex 186.72 -1.54319 -4.6954e-16
    endloop
  endfacet
  facet normal 0.827674 0.561208 0
    outer loop
      vertex 186.565 -1.31466 0.7
      vertex 186.72 -1.54319 0.7
      vertex 186.72 -1.54319 -4.6954e-16
    endloop
  endfacet
  facet normal 0.762179 0.647367 0
    outer loop
      vertex 186.72 -1.54319 -4.6954e-16
      vertex 186.72 -1.54319 0.7
      vertex 186.899 -1.75363 -4.28196e-16
    endloop
  endfacet
  facet normal 0.762179 0.647367 0
    outer loop
      vertex 186.72 -1.54319 0.7
      vertex 186.899 -1.75363 0.7
      vertex 186.899 -1.75363 -4.28196e-16
    endloop
  endfacet
  facet normal 0.687705 0.72599 0
    outer loop
      vertex 186.899 -1.75363 -4.28196e-16
      vertex 186.899 -1.75363 0.7
      vertex 187.099 -1.94351 -3.81832e-16
    endloop
  endfacet
  facet normal 0.687705 0.72599 0
    outer loop
      vertex 186.899 -1.75363 0.7
      vertex 187.099 -1.94351 0.7
      vertex 187.099 -1.94351 -3.81832e-16
    endloop
  endfacet
  facet normal 0.605176 0.796092 0
    outer loop
      vertex 187.099 -1.94351 -3.81832e-16
      vertex 187.099 -1.94351 0.7
      vertex 187.319 -2.11061 -3.30991e-16
    endloop
  endfacet
  facet normal 0.605176 0.796092 0
    outer loop
      vertex 187.099 -1.94351 0.7
      vertex 187.319 -2.11061 0.7
      vertex 187.319 -2.11061 -3.30991e-16
    endloop
  endfacet
  facet normal 0.515553 0.856858 0
    outer loop
      vertex 187.319 -2.11061 -3.30991e-16
      vertex 187.319 -2.11061 0.7
      vertex 187.556 -2.25296 -2.7627e-16
    endloop
  endfacet
  facet normal 0.515553 0.856858 0
    outer loop
      vertex 187.319 -2.11061 0.7
      vertex 187.556 -2.25296 0.7
      vertex 187.556 -2.25296 -2.7627e-16
    endloop
  endfacet
  facet normal 0.419884 0.907578 0
    outer loop
      vertex 187.556 -2.25296 -2.7627e-16
      vertex 187.556 -2.25296 0.7
      vertex 187.806 -2.36889 -2.1831e-16
    endloop
  endfacet
  facet normal 0.419884 0.907578 0
    outer loop
      vertex 187.556 -2.25296 0.7
      vertex 187.806 -2.36889 0.7
      vertex 187.806 -2.36889 -2.1831e-16
    endloop
  endfacet
  facet normal 0.319291 0.947657 0
    outer loop
      vertex 187.806 -2.36889 -2.1831e-16
      vertex 187.806 -2.36889 0.7
      vertex 188.068 -2.45705 -1.5779e-16
    endloop
  endfacet
  facet normal 0.319291 0.947657 0
    outer loop
      vertex 187.806 -2.36889 0.7
      vertex 188.068 -2.45705 0.7
      vertex 188.068 -2.45705 -1.5779e-16
    endloop
  endfacet
  facet normal 0.214971 0.97662 0
    outer loop
      vertex 188.068 -2.45705 -1.5779e-16
      vertex 188.068 -2.45705 0.7
      vertex 188.337 -2.51641 -9.542e-17
    endloop
  endfacet
  facet normal 0.214971 0.97662 0
    outer loop
      vertex 188.068 -2.45705 0.7
      vertex 188.337 -2.51641 0.7
      vertex 188.337 -2.51641 -9.542e-17
    endloop
  endfacet
  facet normal 0.108123 0.994137 0
    outer loop
      vertex 188.337 -2.51641 -9.542e-17
      vertex 188.337 -2.51641 0.7
      vertex 188.612 -2.54626 -3.19315e-17
    endloop
  endfacet
  facet normal 0.108123 0.994137 0
    outer loop
      vertex 188.337 -2.51641 0.7
      vertex 188.612 -2.54626 0.7
      vertex 188.612 -2.54626 -3.19315e-17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 188.612 -2.54626 -3.19315e-17
      vertex 188.612 -2.54626 0.7
      vertex 188.888 -2.54626 3.19315e-17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 188.612 -2.54626 0.7
      vertex 188.888 -2.54626 0.7
      vertex 188.888 -2.54626 3.19315e-17
    endloop
  endfacet
  facet normal -0.108123 0.994137 0
    outer loop
      vertex 188.888 -2.54626 3.19315e-17
      vertex 188.888 -2.54626 0.7
      vertex 189.163 -2.51641 9.542e-17
    endloop
  endfacet
  facet normal -0.108123 0.994137 0
    outer loop
      vertex 188.888 -2.54626 0.7
      vertex 189.163 -2.51641 0.7
      vertex 189.163 -2.51641 9.542e-17
    endloop
  endfacet
  facet normal -0.21496 0.976623 0
    outer loop
      vertex 189.163 -2.51641 9.542e-17
      vertex 189.163 -2.51641 0.7
      vertex 189.432 -2.45705 1.5779e-16
    endloop
  endfacet
  facet normal -0.21496 0.976623 0
    outer loop
      vertex 189.163 -2.51641 0.7
      vertex 189.432 -2.45705 0.7
      vertex 189.432 -2.45705 1.5779e-16
    endloop
  endfacet
  facet normal -0.319307 0.947651 0
    outer loop
      vertex 189.432 -2.45705 1.5779e-16
      vertex 189.432 -2.45705 0.7
      vertex 189.694 -2.36889 2.1831e-16
    endloop
  endfacet
  facet normal -0.319307 0.947651 0
    outer loop
      vertex 189.432 -2.45705 0.7
      vertex 189.694 -2.36889 0.7
      vertex 189.694 -2.36889 2.1831e-16
    endloop
  endfacet
  facet normal -0.419884 0.907578 0
    outer loop
      vertex 189.694 -2.36889 2.1831e-16
      vertex 189.694 -2.36889 0.7
      vertex 189.944 -2.25296 2.7627e-16
    endloop
  endfacet
  facet normal -0.419884 0.907578 0
    outer loop
      vertex 189.694 -2.36889 0.7
      vertex 189.944 -2.25296 0.7
      vertex 189.944 -2.25296 2.7627e-16
    endloop
  endfacet
  facet normal -0.515553 0.856858 0
    outer loop
      vertex 189.944 -2.25296 2.7627e-16
      vertex 189.944 -2.25296 0.7
      vertex 190.181 -2.11061 3.30991e-16
    endloop
  endfacet
  facet normal -0.515553 0.856858 0
    outer loop
      vertex 189.944 -2.25296 0.7
      vertex 190.181 -2.11061 0.7
      vertex 190.181 -2.11061 3.30991e-16
    endloop
  endfacet
  facet normal -0.605176 0.796092 0
    outer loop
      vertex 190.181 -2.11061 3.30991e-16
      vertex 190.181 -2.11061 0.7
      vertex 190.401 -1.94351 3.81832e-16
    endloop
  endfacet
  facet normal -0.605176 0.796092 0
    outer loop
      vertex 190.181 -2.11061 0.7
      vertex 190.401 -1.94351 0.7
      vertex 190.401 -1.94351 3.81832e-16
    endloop
  endfacet
  facet normal -0.687705 0.72599 0
    outer loop
      vertex 190.401 -1.94351 3.81832e-16
      vertex 190.401 -1.94351 0.7
      vertex 190.601 -1.75363 4.28196e-16
    endloop
  endfacet
  facet normal -0.687705 0.72599 0
    outer loop
      vertex 190.401 -1.94351 0.7
      vertex 190.601 -1.75363 0.7
      vertex 190.601 -1.75363 4.28196e-16
    endloop
  endfacet
  facet normal -0.762152 0.647398 0
    outer loop
      vertex 190.601 -1.75363 4.28196e-16
      vertex 190.601 -1.75363 0.7
      vertex 190.78 -1.54319 4.6954e-16
    endloop
  endfacet
  facet normal -0.762152 0.647398 0
    outer loop
      vertex 190.601 -1.75363 0.7
      vertex 190.78 -1.54319 0.7
      vertex 190.78 -1.54319 4.6954e-16
    endloop
  endfacet
  facet normal -0.8277 0.561172 0
    outer loop
      vertex 190.78 -1.54319 4.6954e-16
      vertex 190.78 -1.54319 0.7
      vertex 190.935 -1.31466 5.05379e-16
    endloop
  endfacet
  facet normal -0.8277 0.561172 0
    outer loop
      vertex 190.78 -1.54319 0.7
      vertex 190.935 -1.31466 0.7
      vertex 190.935 -1.31466 5.05379e-16
    endloop
  endfacet
  facet normal -0.883518 0.468396 0
    outer loop
      vertex 190.935 -1.31466 5.05379e-16
      vertex 190.935 -1.31466 0.7
      vertex 191.064 -1.07072 5.35293e-16
    endloop
  endfacet
  facet normal -0.883518 0.468396 0
    outer loop
      vertex 190.935 -1.31466 0.7
      vertex 191.064 -1.07072 0.7
      vertex 191.064 -1.07072 5.35293e-16
    endloop
  endfacet
  facet normal -0.928966 0.370166 0
    outer loop
      vertex 191.064 -1.07072 5.35293e-16
      vertex 191.064 -1.07072 0.7
      vertex 191.167 -0.814219 5.58932e-16
    endloop
  endfacet
  facet normal -0.928966 0.370166 0
    outer loop
      vertex 191.064 -1.07072 0.7
      vertex 191.167 -0.814219 0.7
      vertex 191.167 -0.814219 5.58932e-16
    endloop
  endfacet
  facet normal -0.963552 0.267522 0
    outer loop
      vertex 191.167 -0.814219 5.58932e-16
      vertex 191.167 -0.814219 0.7
      vertex 191.24 -0.548175 5.76017e-16
    endloop
  endfacet
  facet normal -0.963552 0.267522 0
    outer loop
      vertex 191.167 -0.814219 0.7
      vertex 191.24 -0.548175 0.7
      vertex 191.24 -0.548175 5.76017e-16
    endloop
  endfacet
  facet normal -0.986824 0.161797 0
    outer loop
      vertex 191.24 -0.548175 5.76017e-16
      vertex 191.24 -0.548175 0.7
      vertex 191.285 -0.275703 5.86349e-16
    endloop
  endfacet
  facet normal -0.986824 0.161797 0
    outer loop
      vertex 191.24 -0.548175 0.7
      vertex 191.285 -0.275703 0.7
      vertex 191.285 -0.275703 5.86349e-16
    endloop
  endfacet
  facet normal -0.998534 0.0541304 0
    outer loop
      vertex 191.285 -0.275703 5.86349e-16
      vertex 191.285 -0.275703 0.7
      vertex 191.3 -6.02799e-16 5.89806e-16
    endloop
  endfacet
  facet normal -0.998534 0.0541304 5.13575e-17
    outer loop
      vertex 191.285 -0.275703 0.7
      vertex 191.3 -1.22737e-15 0.7
      vertex 191.3 -6.02799e-16 5.89806e-16
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.305 2.51933 1.3
      vertex 183.609 3.09332 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 7 1.3
      vertex 15 2.22452 1.3
      vertex 15.65 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.609 3.09332 1.3
      vertex 183.973 3.63105 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.973 3.63105 1.3
      vertex 184.394 4.1262 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 7 1.3
      vertex 184.394 4.1262 1.3
      vertex 184.866 4.57297 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.971 5.57386 1.3
      vertex 191.56 5.30107 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.61 1.28982 1.3
      vertex 195 6.89317 1.3
      vertex 194.436 1.91581 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 6.89317 1.3
      vertex 194.195 2.51933 1.3
      vertex 194.436 1.91581 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.56 5.30107 1.3
      vertex 192.117 4.96613 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.117 4.96613 1.3
      vertex 192.634 4.57297 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 6.89317 1.3
      vertex 192.634 4.57297 1.3
      vertex 193.106 4.1262 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.106 4.1262 1.3
      vertex 193.527 3.63105 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.527 3.63105 1.3
      vertex 193.891 3.09332 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 6.89317 1.3
      vertex 193.891 3.09332 1.3
      vertex 194.195 2.51933 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15.65 2.22452 1.3
      vertex 34.8 2.22452 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 34.8 2.22452 1.3
      vertex 54.8 2.22452 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 7 1.3
      vertex 54.8 2.22452 1.3
      vertex 70.8 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.61 1.28982 1.3
      vertex 194.715 0.648714 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.715 0.648714 1.3
      vertex 194.75 -1.86112e-15 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 6.89317 1.3
      vertex 194.75 -1.86112e-15 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.75 -1.86112e-15 1.3
      vertex 194.715 -0.648714 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 -6.89317 1.3
      vertex 194.715 -0.648714 1.3
      vertex 194.61 -1.28982 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.891 -3.09332 1.3
      vertex 193.527 -3.63105 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.527 -3.63105 1.3
      vertex 193.106 -4.1262 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.305 -2.51933 1.3
      vertex 183.178 -2.22452 1.3
      vertex 92.031 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.61 -1.28982 1.3
      vertex 194.436 -1.91581 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.436 -1.91581 1.3
      vertex 194.195 -2.51933 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 -6.89317 1.3
      vertex 194.195 -2.51933 1.3
      vertex 193.891 -3.09332 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.106 -4.1262 1.3
      vertex 192.634 -4.57297 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.634 -4.57297 1.3
      vertex 192.117 -4.96613 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 -6.89317 1.3
      vertex 192.117 -4.96613 1.3
      vertex 191.56 -5.30107 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.94 -5.30107 1.3
      vertex 185.383 -4.96613 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.383 -4.96613 1.3
      vertex 184.866 -4.57297 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.866 4.57297 1.3
      vertex 185.383 4.96613 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.383 4.96613 1.3
      vertex 185.94 5.30107 1.3
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 7 1.3
      vertex 185.94 5.30107 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.94 5.30107 1.3
      vertex 186.529 5.57386 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.178 2.22452 1.3
      vertex 183.305 2.51933 1.3
      vertex 92.031 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.305 2.51933 1.3
      vertex 15 7 1.3
      vertex 92.031 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 92.031 2.22452 1.3
      vertex 15 7 1.3
      vertex 82.95 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 7 1.3
      vertex 70.8 2.22452 1.3
      vertex 82.95 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.529 5.57386 1.3
      vertex 187.145 5.7813 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.145 5.7813 1.3
      vertex 187.779 5.92096 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.81 7 1.3
      vertex 187.779 5.92096 1.3
      vertex 188.425 5.9912 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.425 5.9912 1.3
      vertex 189.075 5.9912 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.075 5.9912 1.3
      vertex 189.721 5.92096 1.3
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.81 7 1.3
      vertex 189.721 5.92096 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.721 5.92096 1.3
      vertex 190.355 5.7813 1.3
      vertex 195 6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 6.89317 1.3
      vertex 190.355 5.7813 1.3
      vertex 190.971 5.57386 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.81 -7 1.3
      vertex 189.075 -5.9912 1.3
      vertex 188.425 -5.9912 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.866 -4.57297 1.3
      vertex 184.394 -4.1262 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.394 -4.1262 1.3
      vertex 183.973 -3.63105 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 -7 1.3
      vertex 183.973 -3.63105 1.3
      vertex 92.031 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.973 -3.63105 1.3
      vertex 183.609 -3.09332 1.3
      vertex 92.031 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 92.031 -2.22452 1.3
      vertex 183.609 -3.09332 1.3
      vertex 183.305 -2.51933 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 92.031 -2.22452 1.3
      vertex 82.95 -2.22452 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 82.95 -2.22452 1.3
      vertex 70.8 -2.22452 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 -7 1.3
      vertex 70.8 -2.22452 1.3
      vertex 54.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.425 -5.9912 1.3
      vertex 187.779 -5.92096 1.3
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.779 -5.92096 1.3
      vertex 187.145 -5.7813 1.3
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.81 -7 1.3
      vertex 187.145 -5.7813 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.145 -5.7813 1.3
      vertex 186.529 -5.57386 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 -7 1.3
      vertex 186.529 -5.57386 1.3
      vertex 185.94 -5.30107 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.56 -5.30107 1.3
      vertex 190.971 -5.57386 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.971 -5.57386 1.3
      vertex 190.355 -5.7813 1.3
      vertex 195 -6.89317 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 195 -6.89317 1.3
      vertex 190.355 -5.7813 1.3
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.355 -5.7813 1.3
      vertex 189.721 -5.92096 1.3
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.81 -7 1.3
      vertex 189.721 -5.92096 1.3
      vertex 189.075 -5.9912 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 54.8 -2.22452 1.3
      vertex 34.8 -2.22452 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 34.8 -2.22452 1.3
      vertex 15.65 -2.22452 1.3
      vertex 15 -7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 -7 1.3
      vertex 15.65 -2.22452 1.3
      vertex 15 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 91.381 -2.22452 2.6
      vertex 91.381 2.22452 2.6
      vertex 83.6 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 91.381 2.22452 2.6
      vertex 83.6 2.22452 2.6
      vertex 83.6 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 9 -10 12
      vertex 6 -10 12
      vertex 9 10 12
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 6 -10 12
      vertex 6 10 12
      vertex 9 10 12
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -10 0
      vertex 15 -8.3 0
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -8.3 0
      vertex 15 -7 1.3
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -7 1.3
      vertex 15 -2.22452 1.3
      vertex 15 -2.22452 1.95
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -7 1.3
      vertex 15 -2.22452 1.95
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -2.22452 1.95
      vertex 15 -2.22452 6.80323
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -10 15
      vertex 15 -2.22452 6.80323
      vertex 15 -2.22452 7.87045
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -2.22452 7.87045
      vertex 15 -2.22452 9.21554
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -2.22452 9.21554
      vertex 15 -2.22452 12.0871
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 -10 15
      vertex 15 -2.22452 12.0871
      vertex 15 -2.22452 15
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 82.3 -2.22452 2.6
      vertex 82.3 2.22452 2.6
      vertex 72.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 82.3 2.22452 2.6
      vertex 72.3 2.22452 2.6
      vertex 72.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 2.22452 15
      vertex 15 10 15
      vertex -2.60209e-15 10 15
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 2.22452 15
      vertex -2.60209e-15 10 15
      vertex 15 -2.22452 15
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -2.60209e-15 10 15
      vertex -2.60209e-15 -10 15
      vertex 15 -2.22452 15
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 15 -2.22452 15
      vertex -2.60209e-15 -10 15
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 86.0085 2.22452 9.21554
      vertex 82.95 2.22452 9.21554
      vertex 82.95 2.22452 9.46469
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 175.198 2.22452 1.95
      vertex 183.178 2.22452 1.3
      vertex 92.031 2.22452 1.3
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 77.3 2.22452 8.62495
      vertex 82.95 2.22452 6.80323
      vertex 82.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 6.80323
      vertex 82.95 2.22452 1.95
      vertex 82.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 24.8 2.22452 12.9017
      vertex 23.9854 2.22452 12.0871
      vertex 15.65 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 23.9854 2.22452 12.0871
      vertex 21.1139 2.22452 9.21554
      vertex 15.65 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 12.0871
      vertex 21.1139 2.22452 9.21554
      vertex 15.65 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 21.1139 2.22452 9.21554
      vertex 19.7688 2.22452 7.87045
      vertex 15.65 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 9.21554
      vertex 19.7688 2.22452 7.87045
      vertex 15.65 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 19.7688 2.22452 7.87045
      vertex 18.7016 2.22452 6.80323
      vertex 15.65 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 7.87045
      vertex 18.7016 2.22452 6.80323
      vertex 15.65 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 18.7016 2.22452 6.80323
      vertex 16.3 2.22452 4.40168
      vertex 15.65 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 6.80323
      vertex 16.3 2.22452 4.40168
      vertex 15.65 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 16.3 2.22452 4.40168
      vertex 16.3 2.22452 2.6
      vertex 15.65 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 1.95
      vertex 16.3 2.22452 2.6
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 16.3 2.22452 2.6
      vertex 33.3 2.22452 2.6
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 1.95
      vertex 33.3 2.22452 2.6
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 33.3 2.22452 2.6
      vertex 33.3 2.22452 4.40168
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 33.3 2.22452 4.40168
      vertex 30.8984 2.22452 6.80323
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 30.8984 2.22452 6.80323
      vertex 29.8312 2.22452 7.87045
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 6.80323
      vertex 29.8312 2.22452 7.87045
      vertex 34.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 29.8312 2.22452 7.87045
      vertex 28.4861 2.22452 9.21554
      vertex 34.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 7.87045
      vertex 28.4861 2.22452 9.21554
      vertex 34.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 28.4861 2.22452 9.21554
      vertex 25.6146 2.22452 12.0871
      vertex 34.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 44.8 2.22452 11.2724
      vertex 42.7431 2.22452 9.21554
      vertex 34.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 42.7431 2.22452 9.21554
      vertex 41.398 2.22452 7.87045
      vertex 34.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 9.21554
      vertex 41.398 2.22452 7.87045
      vertex 34.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 41.398 2.22452 7.87045
      vertex 40.3308 2.22452 6.80323
      vertex 34.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 7.87045
      vertex 40.3308 2.22452 6.80323
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 40.3308 2.22452 6.80323
      vertex 36.3 2.22452 2.77245
      vertex 34.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 6.80323
      vertex 36.3 2.22452 2.77245
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 36.3 2.22452 2.77245
      vertex 36.3 2.22452 2.6
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 1.95
      vertex 36.3 2.22452 2.6
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 36.3 2.22452 2.6
      vertex 53.3 2.22452 2.6
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 1.95
      vertex 53.3 2.22452 2.6
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 53.3 2.22452 2.6
      vertex 53.3 2.22452 2.77245
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 13.3871
      vertex 50.7585 2.22452 12.0871
      vertex 34.8 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 50.7585 2.22452 12.0871
      vertex 44.8 2.22452 11.2724
      vertex 34.8 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 53.3 2.22452 2.77245
      vertex 49.2692 2.22452 6.80323
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 49.2692 2.22452 6.80323
      vertex 48.202 2.22452 7.87045
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 6.80323
      vertex 48.202 2.22452 7.87045
      vertex 54.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 48.202 2.22452 7.87045
      vertex 46.8569 2.22452 9.21554
      vertex 54.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 7.87045
      vertex 46.8569 2.22452 9.21554
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 46.8569 2.22452 9.21554
      vertex 44.8 2.22452 11.2724
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 62.8 2.22452 9.80614
      vertex 62.2094 2.22452 9.21554
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 62.2094 2.22452 9.21554
      vertex 60.8643 2.22452 7.87045
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 9.21554
      vertex 60.8643 2.22452 7.87045
      vertex 54.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 60.8643 2.22452 7.87045
      vertex 59.7971 2.22452 6.80323
      vertex 54.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 7.87045
      vertex 59.7971 2.22452 6.80323
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 59.7971 2.22452 6.80323
      vertex 56.3 2.22452 3.30614
      vertex 54.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 6.80323
      vertex 56.3 2.22452 3.30614
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 56.3 2.22452 3.30614
      vertex 56.3 2.22452 2.6
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 1.95
      vertex 56.3 2.22452 2.6
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 56.3 2.22452 2.6
      vertex 69.3 2.22452 2.6
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 1.95
      vertex 69.3 2.22452 2.6
      vertex 70.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 7.87045
      vertex 64.7357 2.22452 7.87045
      vertex 63.3906 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 69.3 2.22452 2.6
      vertex 69.3 2.22452 3.30614
      vertex 70.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 69.3 2.22452 3.30614
      vertex 65.8029 2.22452 6.80323
      vertex 70.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 6.80323
      vertex 65.8029 2.22452 6.80323
      vertex 64.7357 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 64.7357 2.22452 7.87045
      vertex 70.8 2.22452 7.87045
      vertex 70.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 7.87045
      vertex 72.3 2.22452 3.62495
      vertex 70.8 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 6.80323
      vertex 72.3 2.22452 3.62495
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 72.3 2.22452 3.62495
      vertex 72.3 2.22452 2.6
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 1.95
      vertex 72.3 2.22452 2.6
      vertex 82.95 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 72.3 2.22452 2.6
      vertex 82.3 2.22452 2.6
      vertex 82.95 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 1.95
      vertex 82.3 2.22452 2.6
      vertex 82.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 44.8 2.22452 11.2724
      vertex 50.7585 2.22452 12.0871
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 50.7585 2.22452 12.0871
      vertex 54.8 2.22452 11.7578
      vertex 54.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 9.21554
      vertex 54.8 2.22452 11.7578
      vertex 62.8 2.22452 9.80614
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 11.7578
      vertex 70.8 2.22452 10.4544
      vertex 62.8 2.22452 9.80614
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 62.8 2.22452 9.80614
      vertex 70.8 2.22452 10.4544
      vertex 63.3906 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 10.4544
      vertex 70.8 2.22452 9.21554
      vertex 63.3906 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 63.3906 2.22452 9.21554
      vertex 70.8 2.22452 9.21554
      vertex 70.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 9.21554
      vertex 77.3 2.22452 8.62495
      vertex 70.8 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 7.87045
      vertex 77.3 2.22452 8.62495
      vertex 72.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 6.80323
      vertex 92.681 2.22452 2.6
      vertex 92.031 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.681 2.22452 2.6
      vertex 98.9669 2.22452 2.6
      vertex 92.031 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 9.21554
      vertex 86.0085 2.22452 9.21554
      vertex 82.95 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 86.0085 2.22452 9.21554
      vertex 92.031 2.22452 7.87045
      vertex 82.95 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 7.87045
      vertex 92.031 2.22452 7.87045
      vertex 92.031 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 7.87045
      vertex 95.824 2.22452 7.11596
      vertex 92.031 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 6.80323
      vertex 95.824 2.22452 7.11596
      vertex 92.681 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 2.22452 12.0871
      vertex 15 2.22452 15
      vertex 15.65 2.22452 14.9471
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 10.4544
      vertex 82.95 2.22452 9.46469
      vertex 70.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 9.46469
      vertex 82.95 2.22452 9.21554
      vertex 70.8 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 9.21554
      vertex 82.95 2.22452 9.21554
      vertex 77.3 2.22452 8.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 9.21554
      vertex 82.95 2.22452 7.87045
      vertex 77.3 2.22452 8.62495
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 77.3 2.22452 8.62495
      vertex 82.95 2.22452 7.87045
      vertex 82.95 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 7.87045
      vertex 92.031 2.22452 6.80323
      vertex 82.95 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 1.95
      vertex 82.95 2.22452 1.95
      vertex 83.6 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 1.95
      vertex 82.95 2.22452 6.80323
      vertex 83.6 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 83.6 2.22452 2.6
      vertex 82.95 2.22452 6.80323
      vertex 87.4905 2.22452 6.49051
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 6.80323
      vertex 92.031 2.22452 6.80323
      vertex 87.4905 2.22452 6.49051
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 87.4905 2.22452 6.49051
      vertex 92.031 2.22452 6.80323
      vertex 91.381 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 6.80323
      vertex 92.031 2.22452 1.95
      vertex 91.381 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 91.381 2.22452 2.6
      vertex 92.031 2.22452 1.95
      vertex 83.6 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 44.8 2.22452 11.2724
      vertex 34.8 2.22452 9.21554
      vertex 34.8 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 9.21554
      vertex 25.6146 2.22452 12.0871
      vertex 34.8 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 12.0871
      vertex 25.6146 2.22452 12.0871
      vertex 34.8 2.22452 13.3871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 25.6146 2.22452 12.0871
      vertex 24.8 2.22452 12.9017
      vertex 34.8 2.22452 13.3871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 13.3871
      vertex 24.8 2.22452 12.9017
      vertex 15.65 2.22452 14.9471
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 24.8 2.22452 12.9017
      vertex 15.65 2.22452 12.0871
      vertex 15.65 2.22452 14.9471
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 14.9471
      vertex 15.65 2.22452 12.0871
      vertex 15 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 12.0871
      vertex 15.65 2.22452 9.21554
      vertex 15 2.22452 12.0871
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 2.22452 12.0871
      vertex 15.65 2.22452 9.21554
      vertex 15 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 9.21554
      vertex 15.65 2.22452 7.87045
      vertex 15 2.22452 9.21554
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 2.22452 9.21554
      vertex 15.65 2.22452 7.87045
      vertex 15 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 7.87045
      vertex 15.65 2.22452 6.80323
      vertex 15 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 2.22452 7.87045
      vertex 15.65 2.22452 6.80323
      vertex 15 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 6.80323
      vertex 15.65 2.22452 1.95
      vertex 15 2.22452 6.80323
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 2.22452 6.80323
      vertex 15.65 2.22452 1.95
      vertex 15 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 86.0085 2.22452 9.21554
      vertex 92.031 2.22452 8.72494
      vertex 92.031 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 8.72494
      vertex 102.52 2.22452 7.87045
      vertex 92.031 2.22452 7.87045
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 7.87045
      vertex 102.52 2.22452 7.87045
      vertex 95.824 2.22452 7.11596
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 102.52 2.22452 7.87045
      vertex 115.621 2.22452 6.80323
      vertex 95.824 2.22452 7.11596
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 95.824 2.22452 7.11596
      vertex 115.621 2.22452 6.80323
      vertex 98.9669 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 115.621 2.22452 6.80323
      vertex 175.198 2.22452 1.95
      vertex 98.9669 2.22452 2.6
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 98.9669 2.22452 2.6
      vertex 175.198 2.22452 1.95
      vertex 92.031 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 175.198 2.22452 1.95
      vertex 92.031 2.22452 1.3
      vertex 92.031 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 1.95
      vertex 92.031 2.22452 1.3
      vertex 82.95 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 92.031 2.22452 1.3
      vertex 82.95 2.22452 1.3
      vertex 82.95 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 1.95
      vertex 82.95 2.22452 1.3
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 82.95 2.22452 1.3
      vertex 70.8 2.22452 1.3
      vertex 70.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 1.95
      vertex 70.8 2.22452 1.3
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 70.8 2.22452 1.3
      vertex 54.8 2.22452 1.3
      vertex 54.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 1.95
      vertex 54.8 2.22452 1.3
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 54.8 2.22452 1.3
      vertex 34.8 2.22452 1.3
      vertex 34.8 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 1.95
      vertex 34.8 2.22452 1.3
      vertex 15.65 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 34.8 2.22452 1.3
      vertex 15.65 2.22452 1.3
      vertex 15.65 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 1.95
      vertex 15.65 2.22452 1.3
      vertex 15 2.22452 1.95
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.65 2.22452 1.3
      vertex 15 2.22452 1.3
      vertex 15 2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -10 15
      vertex -2.60209e-15 -10 15
      vertex 6 -10 12
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 6 -10 12
      vertex 9 -10 12
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 9 -10 12
      vertex 12 -10 9
      vertex 15 -10 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -10 15
      vertex 12 -10 9
      vertex 15 -10 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 12 -10 9
      vertex 12 -10 3
      vertex 15 -10 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -10 0
      vertex 12 -10 3
      vertex 0 -10 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 12 -10 3
      vertex 3 -10 3
      vertex 0 -10 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 0 -10 0
      vertex 3 -10 3
      vertex -2.60209e-15 -10 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 3 -10 3
      vertex 3 -10 9
      vertex -2.60209e-15 -10 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -2.60209e-15 -10 15
      vertex 3 -10 9
      vertex 6 -10 12
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 77.3 -2.22452 8.62495
      vertex 77.3 2.22452 8.62495
      vertex 82.3 -2.22452 3.62495
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 77.3 2.22452 8.62495
      vertex 82.3 2.22452 3.62495
      vertex 82.3 -2.22452 3.62495
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 77.3 -2.22452 8.62495
      vertex 82.95 -2.22452 7.87045
      vertex 82.95 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 24.8 -2.22452 12.9017
      vertex 25.6146 -2.22452 12.0871
      vertex 34.8 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 6.80323
      vertex 15.65 -2.22452 1.95
      vertex 16.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 1.95
      vertex 16.3 -2.22452 2.6
      vertex 16.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 16.3 -2.22452 2.6
      vertex 15.65 -2.22452 1.95
      vertex 33.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 1.95
      vertex 34.8 -2.22452 1.95
      vertex 33.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 33.3 -2.22452 2.6
      vertex 34.8 -2.22452 1.95
      vertex 33.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 1.95
      vertex 34.8 -2.22452 6.80323
      vertex 33.3 -2.22452 4.40168
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 33.3 -2.22452 4.40168
      vertex 34.8 -2.22452 6.80323
      vertex 30.8984 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 6.80323
      vertex 34.8 -2.22452 7.87045
      vertex 30.8984 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 30.8984 -2.22452 6.80323
      vertex 34.8 -2.22452 7.87045
      vertex 29.8312 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 7.87045
      vertex 34.8 -2.22452 9.21554
      vertex 29.8312 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 29.8312 -2.22452 7.87045
      vertex 34.8 -2.22452 9.21554
      vertex 28.4861 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 23.9854 -2.22452 12.0871
      vertex 24.8 -2.22452 12.9017
      vertex 15.65 -2.22452 14.9471
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 14.9471
      vertex 24.8 -2.22452 12.9017
      vertex 34.8 -2.22452 13.3871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 24.8 -2.22452 12.9017
      vertex 34.8 -2.22452 12.0871
      vertex 34.8 -2.22452 13.3871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 13.3871
      vertex 34.8 -2.22452 12.0871
      vertex 50.7585 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 16.3 -2.22452 4.40168
      vertex 18.7016 -2.22452 6.80323
      vertex 15.65 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 18.7016 -2.22452 6.80323
      vertex 19.7688 -2.22452 7.87045
      vertex 15.65 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 6.80323
      vertex 19.7688 -2.22452 7.87045
      vertex 15.65 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 19.7688 -2.22452 7.87045
      vertex 21.1139 -2.22452 9.21554
      vertex 15.65 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 7.87045
      vertex 21.1139 -2.22452 9.21554
      vertex 15.65 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 21.1139 -2.22452 9.21554
      vertex 23.9854 -2.22452 12.0871
      vertex 15.65 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 9.21554
      vertex 23.9854 -2.22452 12.0871
      vertex 15.65 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 23.9854 -2.22452 12.0871
      vertex 15.65 -2.22452 14.9471
      vertex 15.65 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 6.80323
      vertex 69.3 -2.22452 3.30614
      vertex 70.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 69.3 -2.22452 3.30614
      vertex 69.3 -2.22452 2.6
      vertex 70.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 1.95
      vertex 69.3 -2.22452 2.6
      vertex 54.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 69.3 -2.22452 2.6
      vertex 56.3 -2.22452 2.6
      vertex 54.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 1.95
      vertex 56.3 -2.22452 2.6
      vertex 54.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 56.3 -2.22452 2.6
      vertex 56.3 -2.22452 3.30614
      vertex 54.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 65.8029 -2.22452 6.80323
      vertex 70.8 -2.22452 7.87045
      vertex 64.7357 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 7.87045
      vertex 70.8 -2.22452 9.21554
      vertex 64.7357 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 64.7357 -2.22452 7.87045
      vertex 70.8 -2.22452 9.21554
      vertex 63.3906 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 62.2094 -2.22452 9.21554
      vertex 62.8 -2.22452 9.80614
      vertex 54.8 -2.22452 11.7578
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 63.3906 -2.22452 9.21554
      vertex 70.8 -2.22452 9.21554
      vertex 62.8 -2.22452 9.80614
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 9.21554
      vertex 70.8 -2.22452 10.4544
      vertex 62.8 -2.22452 9.80614
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 62.8 -2.22452 9.80614
      vertex 70.8 -2.22452 10.4544
      vertex 54.8 -2.22452 11.7578
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 56.3 -2.22452 3.30614
      vertex 59.7971 -2.22452 6.80323
      vertex 54.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 59.7971 -2.22452 6.80323
      vertex 60.8643 -2.22452 7.87045
      vertex 54.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 6.80323
      vertex 60.8643 -2.22452 7.87045
      vertex 54.8 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 60.8643 -2.22452 7.87045
      vertex 62.2094 -2.22452 9.21554
      vertex 54.8 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 7.87045
      vertex 62.2094 -2.22452 9.21554
      vertex 54.8 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 62.2094 -2.22452 9.21554
      vertex 54.8 -2.22452 11.7578
      vertex 54.8 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 9.21554
      vertex 54.8 -2.22452 11.7578
      vertex 50.7585 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 95.824 -2.22452 7.11596
      vertex 92.031 -2.22452 6.80323
      vertex 92.681 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 6.80323
      vertex 92.031 -2.22452 1.95
      vertex 92.681 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.681 -2.22452 2.6
      vertex 92.031 -2.22452 1.95
      vertex 98.9669 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 1.3
      vertex 183.178 -2.22452 1.3
      vertex 175.198 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 9.46469
      vertex 70.8 -2.22452 10.4544
      vertex 82.95 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 10.4544
      vertex 70.8 -2.22452 9.21554
      vertex 82.95 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 9.21554
      vertex 70.8 -2.22452 9.21554
      vertex 77.3 -2.22452 8.62495
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 9.21554
      vertex 70.8 -2.22452 7.87045
      vertex 77.3 -2.22452 8.62495
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 77.3 -2.22452 8.62495
      vertex 70.8 -2.22452 7.87045
      vertex 70.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 7.87045
      vertex 65.8029 -2.22452 6.80323
      vertex 70.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 6.80323
      vertex 65.8029 -2.22452 6.80323
      vertex 69.3 -2.22452 3.30614
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 6.80323
      vertex 82.3 -2.22452 3.62495
      vertex 82.95 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.3 -2.22452 3.62495
      vertex 82.3 -2.22452 2.6
      vertex 82.95 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 1.95
      vertex 82.3 -2.22452 2.6
      vertex 70.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.3 -2.22452 2.6
      vertex 72.3 -2.22452 2.6
      vertex 70.8 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 1.95
      vertex 72.3 -2.22452 2.6
      vertex 70.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 72.3 -2.22452 2.6
      vertex 72.3 -2.22452 3.62495
      vertex 70.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 6.80323
      vertex 72.3 -2.22452 3.62495
      vertex 77.3 -2.22452 8.62495
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 36.3 -2.22452 2.77245
      vertex 34.8 -2.22452 6.80323
      vertex 36.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 6.80323
      vertex 34.8 -2.22452 1.95
      vertex 36.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 36.3 -2.22452 2.6
      vertex 34.8 -2.22452 1.95
      vertex 53.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 1.95
      vertex 54.8 -2.22452 1.95
      vertex 53.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 53.3 -2.22452 2.6
      vertex 54.8 -2.22452 1.95
      vertex 53.3 -2.22452 2.77245
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 1.95
      vertex 54.8 -2.22452 6.80323
      vertex 53.3 -2.22452 2.77245
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 53.3 -2.22452 2.77245
      vertex 54.8 -2.22452 6.80323
      vertex 49.2692 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 6.80323
      vertex 54.8 -2.22452 7.87045
      vertex 49.2692 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 49.2692 -2.22452 6.80323
      vertex 54.8 -2.22452 7.87045
      vertex 48.202 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 7.87045
      vertex 54.8 -2.22452 9.21554
      vertex 48.202 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 48.202 -2.22452 7.87045
      vertex 54.8 -2.22452 9.21554
      vertex 46.8569 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 9.21554
      vertex 50.7585 -2.22452 12.0871
      vertex 46.8569 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 46.8569 -2.22452 9.21554
      vertex 50.7585 -2.22452 12.0871
      vertex 44.8 -2.22452 11.2724
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 50.7585 -2.22452 12.0871
      vertex 34.8 -2.22452 12.0871
      vertex 44.8 -2.22452 11.2724
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 44.8 -2.22452 11.2724
      vertex 34.8 -2.22452 12.0871
      vertex 42.7431 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 36.3 -2.22452 2.77245
      vertex 40.3308 -2.22452 6.80323
      vertex 34.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 40.3308 -2.22452 6.80323
      vertex 41.398 -2.22452 7.87045
      vertex 34.8 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 6.80323
      vertex 41.398 -2.22452 7.87045
      vertex 34.8 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 41.398 -2.22452 7.87045
      vertex 42.7431 -2.22452 9.21554
      vertex 34.8 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 7.87045
      vertex 42.7431 -2.22452 9.21554
      vertex 34.8 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 42.7431 -2.22452 9.21554
      vertex 34.8 -2.22452 12.0871
      vertex 34.8 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 9.21554
      vertex 34.8 -2.22452 12.0871
      vertex 28.4861 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 12.0871
      vertex 25.6146 -2.22452 12.0871
      vertex 28.4861 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -2.22452 1.95
      vertex 15.65 -2.22452 1.95
      vertex 15 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 1.95
      vertex 15.65 -2.22452 6.80323
      vertex 15 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -2.22452 6.80323
      vertex 15.65 -2.22452 6.80323
      vertex 15 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 6.80323
      vertex 15.65 -2.22452 7.87045
      vertex 15 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -2.22452 7.87045
      vertex 15.65 -2.22452 7.87045
      vertex 15 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 7.87045
      vertex 15.65 -2.22452 9.21554
      vertex 15 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -2.22452 9.21554
      vertex 15.65 -2.22452 9.21554
      vertex 15 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 9.21554
      vertex 15.65 -2.22452 12.0871
      vertex 15 -2.22452 12.0871
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15 -2.22452 12.0871
      vertex 15.65 -2.22452 12.0871
      vertex 15 -2.22452 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 12.0871
      vertex 15.65 -2.22452 14.9471
      vertex 15 -2.22452 15
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 95.824 -2.22452 7.11596
      vertex 92.031 -2.22452 7.87045
      vertex 92.031 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 7.87045
      vertex 82.95 -2.22452 7.87045
      vertex 92.031 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 6.80323
      vertex 82.95 -2.22452 7.87045
      vertex 82.95 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 7.87045
      vertex 77.3 -2.22452 8.62495
      vertex 82.95 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 6.80323
      vertex 77.3 -2.22452 8.62495
      vertex 82.3 -2.22452 3.62495
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 1.95
      vertex 92.031 -2.22452 1.95
      vertex 91.381 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 1.95
      vertex 92.031 -2.22452 6.80323
      vertex 91.381 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 91.381 -2.22452 2.6
      vertex 92.031 -2.22452 6.80323
      vertex 87.4905 -2.22452 6.49051
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 6.80323
      vertex 82.95 -2.22452 6.80323
      vertex 87.4905 -2.22452 6.49051
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 87.4905 -2.22452 6.49051
      vertex 82.95 -2.22452 6.80323
      vertex 83.6 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 6.80323
      vertex 82.95 -2.22452 1.95
      vertex 83.6 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 83.6 -2.22452 2.6
      vertex 82.95 -2.22452 1.95
      vertex 91.381 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 9.46469
      vertex 82.95 -2.22452 9.21554
      vertex 86.0085 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 9.21554
      vertex 82.95 -2.22452 7.87045
      vertex 86.0085 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 86.0085 -2.22452 9.21554
      vertex 82.95 -2.22452 7.87045
      vertex 92.031 -2.22452 8.72494
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 7.87045
      vertex 92.031 -2.22452 7.87045
      vertex 92.031 -2.22452 8.72494
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 8.72494
      vertex 92.031 -2.22452 7.87045
      vertex 102.52 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 7.87045
      vertex 95.824 -2.22452 7.11596
      vertex 102.52 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 102.52 -2.22452 7.87045
      vertex 95.824 -2.22452 7.11596
      vertex 115.621 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 95.824 -2.22452 7.11596
      vertex 98.9669 -2.22452 2.6
      vertex 115.621 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 115.621 -2.22452 6.80323
      vertex 98.9669 -2.22452 2.6
      vertex 175.198 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 98.9669 -2.22452 2.6
      vertex 92.031 -2.22452 1.95
      vertex 175.198 -2.22452 1.95
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 175.198 -2.22452 1.95
      vertex 92.031 -2.22452 1.95
      vertex 92.031 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 1.95
      vertex 82.95 -2.22452 1.95
      vertex 92.031 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 92.031 -2.22452 1.3
      vertex 82.95 -2.22452 1.95
      vertex 82.95 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 1.95
      vertex 70.8 -2.22452 1.95
      vertex 82.95 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 82.95 -2.22452 1.3
      vertex 70.8 -2.22452 1.95
      vertex 70.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 1.95
      vertex 54.8 -2.22452 1.95
      vertex 70.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 70.8 -2.22452 1.3
      vertex 54.8 -2.22452 1.95
      vertex 54.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 1.95
      vertex 34.8 -2.22452 1.95
      vertex 54.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 54.8 -2.22452 1.3
      vertex 34.8 -2.22452 1.95
      vertex 34.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 1.95
      vertex 15.65 -2.22452 1.95
      vertex 34.8 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 34.8 -2.22452 1.3
      vertex 15.65 -2.22452 1.95
      vertex 15.65 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 1.95
      vertex 15 -2.22452 1.95
      vertex 15.65 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.65 -2.22452 1.3
      vertex 15 -2.22452 1.95
      vertex 15 -2.22452 1.3
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -2.60209e-15 10 15
      vertex 15 10 15
      vertex 9 10 12
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 9 10 12
      vertex 6 10 12
      vertex -2.60209e-15 10 15
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 6 10 12
      vertex 3 10 9
      vertex -2.60209e-15 10 15
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -2.60209e-15 10 15
      vertex 3 10 9
      vertex 0 10 0
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 3 10 9
      vertex 3 10 3
      vertex 0 10 0
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 0 10 0
      vertex 3 10 3
      vertex 15 10 0
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 3 10 3
      vertex 12 10 3
      vertex 15 10 0
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 10 0
      vertex 12 10 3
      vertex 15 10 15
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 12 10 3
      vertex 12 10 9
      vertex 15 10 15
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15 10 15
      vertex 12 10 9
      vertex 9 10 12
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 77.3 -2.22452 8.62495
      vertex 72.3 -2.22452 3.62495
      vertex 77.3 2.22452 8.62495
    endloop
  endfacet
  facet normal 0.707107 0 -0.707106
    outer loop
      vertex 72.3 -2.22452 3.62495
      vertex 72.3 2.22452 3.62495
      vertex 77.3 2.22452 8.62495
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 9 10 12
      vertex 12 10 9
      vertex 9 -10 12
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 12 10 9
      vertex 12 -10 9
      vertex 9 -10 12
    endloop
  endfacet
  facet normal 0.0172577 0.999851 0
    outer loop
      vertex 195 6.89317 1.3
      vertex 195 6.89317 2.08167e-14
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0.0172576 0.999851 -3.70017e-7
    outer loop
      vertex 195 6.89317 2.08167e-14
      vertex 113.493 8.3 0
      vertex 188.81 7 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.432 2.45705 0.7
      vertex 190.355 5.7813 0.7
      vertex 189.163 2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.355 5.7813 0.7
      vertex 189.721 5.92096 0.7
      vertex 189.163 2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.163 2.51641 0.7
      vertex 189.721 5.92096 0.7
      vertex 188.888 2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.721 5.92096 0.7
      vertex 189.075 5.9912 0.7
      vertex 188.888 2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.888 2.54626 0.7
      vertex 189.075 5.9912 0.7
      vertex 188.612 2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.075 5.9912 0.7
      vertex 188.425 5.9912 0.7
      vertex 188.612 2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.612 2.54626 0.7
      vertex 188.425 5.9912 0.7
      vertex 188.337 2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.425 5.9912 0.7
      vertex 187.779 5.92096 0.7
      vertex 188.337 2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.337 2.51641 0.7
      vertex 187.779 5.92096 0.7
      vertex 188.068 2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.779 5.92096 0.7
      vertex 187.145 5.7813 0.7
      vertex 188.068 2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.068 2.45705 0.7
      vertex 187.145 5.7813 0.7
      vertex 187.806 2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.145 5.7813 0.7
      vertex 186.529 5.57386 0.7
      vertex 187.806 2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.806 2.36889 0.7
      vertex 186.529 5.57386 0.7
      vertex 187.556 2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.529 5.57386 0.7
      vertex 185.94 5.30107 0.7
      vertex 187.556 2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.556 2.25296 0.7
      vertex 185.94 5.30107 0.7
      vertex 187.319 2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.94 5.30107 0.7
      vertex 185.383 4.96613 0.7
      vertex 187.319 2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.319 2.11061 0.7
      vertex 185.383 4.96613 0.7
      vertex 187.099 1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.383 4.96613 0.7
      vertex 184.866 4.57297 0.7
      vertex 187.099 1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.099 1.94351 0.7
      vertex 184.866 4.57297 0.7
      vertex 186.899 1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.866 4.57297 0.7
      vertex 184.394 4.1262 0.7
      vertex 186.899 1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.899 1.75363 0.7
      vertex 184.394 4.1262 0.7
      vertex 186.72 1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.394 4.1262 0.7
      vertex 183.973 3.63105 0.7
      vertex 186.72 1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.72 1.54319 0.7
      vertex 183.973 3.63105 0.7
      vertex 186.565 1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.973 3.63105 0.7
      vertex 183.609 3.09332 0.7
      vertex 186.565 1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.565 1.31466 0.7
      vertex 183.609 3.09332 0.7
      vertex 186.436 1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.609 3.09332 0.7
      vertex 183.305 2.51933 0.7
      vertex 186.436 1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.436 1.07072 0.7
      vertex 183.305 2.51933 0.7
      vertex 186.333 0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.305 2.51933 0.7
      vertex 183.064 1.91581 0.7
      vertex 186.333 0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.333 0.814219 0.7
      vertex 183.064 1.91581 0.7
      vertex 186.26 0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.064 1.91581 0.7
      vertex 182.89 1.28982 0.7
      vertex 186.26 0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.26 0.548175 0.7
      vertex 182.89 1.28982 0.7
      vertex 186.215 0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 182.89 1.28982 0.7
      vertex 182.785 0.648714 0.7
      vertex 186.215 0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.215 0.275703 0.7
      vertex 182.785 0.648714 0.7
      vertex 186.2 -2.90514e-16 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 182.785 0.648714 0.7
      vertex 182.75 3.43241e-16 0.7
      vertex 186.2 -2.90514e-16 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.2 -2.90514e-16 0.7
      vertex 182.75 3.43241e-16 0.7
      vertex 186.215 -0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 182.75 3.43241e-16 0.7
      vertex 182.785 -0.648714 0.7
      vertex 186.215 -0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.215 -0.275703 0.7
      vertex 182.785 -0.648714 0.7
      vertex 186.26 -0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 182.785 -0.648714 0.7
      vertex 182.89 -1.28982 0.7
      vertex 186.26 -0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.26 -0.548175 0.7
      vertex 182.89 -1.28982 0.7
      vertex 186.333 -0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 182.89 -1.28982 0.7
      vertex 183.064 -1.91581 0.7
      vertex 186.333 -0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.333 -0.814219 0.7
      vertex 183.064 -1.91581 0.7
      vertex 186.436 -1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.064 -1.91581 0.7
      vertex 183.305 -2.51933 0.7
      vertex 186.436 -1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.436 -1.07072 0.7
      vertex 183.305 -2.51933 0.7
      vertex 186.565 -1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.305 -2.51933 0.7
      vertex 183.609 -3.09332 0.7
      vertex 186.565 -1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.565 -1.31466 0.7
      vertex 183.609 -3.09332 0.7
      vertex 186.72 -1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.609 -3.09332 0.7
      vertex 183.973 -3.63105 0.7
      vertex 186.72 -1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.72 -1.54319 0.7
      vertex 183.973 -3.63105 0.7
      vertex 186.899 -1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 183.973 -3.63105 0.7
      vertex 184.394 -4.1262 0.7
      vertex 186.899 -1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.899 -1.75363 0.7
      vertex 184.394 -4.1262 0.7
      vertex 187.099 -1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.394 -4.1262 0.7
      vertex 184.866 -4.57297 0.7
      vertex 187.099 -1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.099 -1.94351 0.7
      vertex 184.866 -4.57297 0.7
      vertex 187.319 -2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 184.866 -4.57297 0.7
      vertex 185.383 -4.96613 0.7
      vertex 187.319 -2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.319 -2.11061 0.7
      vertex 185.383 -4.96613 0.7
      vertex 187.556 -2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.383 -4.96613 0.7
      vertex 185.94 -5.30107 0.7
      vertex 187.556 -2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.556 -2.25296 0.7
      vertex 185.94 -5.30107 0.7
      vertex 187.806 -2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 185.94 -5.30107 0.7
      vertex 186.529 -5.57386 0.7
      vertex 187.806 -2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.806 -2.36889 0.7
      vertex 186.529 -5.57386 0.7
      vertex 188.068 -2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 186.529 -5.57386 0.7
      vertex 187.145 -5.7813 0.7
      vertex 188.068 -2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.068 -2.45705 0.7
      vertex 187.145 -5.7813 0.7
      vertex 188.337 -2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.145 -5.7813 0.7
      vertex 187.779 -5.92096 0.7
      vertex 188.337 -2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.337 -2.51641 0.7
      vertex 187.779 -5.92096 0.7
      vertex 188.612 -2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 187.779 -5.92096 0.7
      vertex 188.425 -5.9912 0.7
      vertex 188.612 -2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.612 -2.54626 0.7
      vertex 188.425 -5.9912 0.7
      vertex 188.888 -2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.425 -5.9912 0.7
      vertex 189.075 -5.9912 0.7
      vertex 188.888 -2.54626 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 188.888 -2.54626 0.7
      vertex 189.075 -5.9912 0.7
      vertex 189.163 -2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.075 -5.9912 0.7
      vertex 189.721 -5.92096 0.7
      vertex 189.163 -2.51641 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.163 -2.51641 0.7
      vertex 189.721 -5.92096 0.7
      vertex 189.432 -2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.721 -5.92096 0.7
      vertex 190.355 -5.7813 0.7
      vertex 189.432 -2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.432 -2.45705 0.7
      vertex 190.355 -5.7813 0.7
      vertex 189.694 -2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.355 -5.7813 0.7
      vertex 190.971 -5.57386 0.7
      vertex 189.694 -2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.694 -2.36889 0.7
      vertex 190.971 -5.57386 0.7
      vertex 189.944 -2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.971 -5.57386 0.7
      vertex 191.56 -5.30107 0.7
      vertex 189.944 -2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.944 -2.25296 0.7
      vertex 191.56 -5.30107 0.7
      vertex 190.181 -2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.56 -5.30107 0.7
      vertex 192.117 -4.96613 0.7
      vertex 190.181 -2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.181 -2.11061 0.7
      vertex 192.117 -4.96613 0.7
      vertex 190.401 -1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.117 -4.96613 0.7
      vertex 192.634 -4.57297 0.7
      vertex 190.401 -1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.401 -1.94351 0.7
      vertex 192.634 -4.57297 0.7
      vertex 190.601 -1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.634 -4.57297 0.7
      vertex 193.106 -4.1262 0.7
      vertex 190.601 -1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.601 -1.75363 0.7
      vertex 193.106 -4.1262 0.7
      vertex 190.78 -1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.106 -4.1262 0.7
      vertex 193.527 -3.63105 0.7
      vertex 190.78 -1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.78 -1.54319 0.7
      vertex 193.527 -3.63105 0.7
      vertex 190.935 -1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.527 -3.63105 0.7
      vertex 193.891 -3.09332 0.7
      vertex 190.935 -1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.935 -1.31466 0.7
      vertex 193.891 -3.09332 0.7
      vertex 191.064 -1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.891 -3.09332 0.7
      vertex 194.195 -2.51933 0.7
      vertex 191.064 -1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.064 -1.07072 0.7
      vertex 194.195 -2.51933 0.7
      vertex 191.167 -0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.195 -2.51933 0.7
      vertex 194.436 -1.91581 0.7
      vertex 191.167 -0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.167 -0.814219 0.7
      vertex 194.436 -1.91581 0.7
      vertex 191.24 -0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.436 -1.91581 0.7
      vertex 194.61 -1.28982 0.7
      vertex 191.24 -0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.24 -0.548175 0.7
      vertex 194.61 -1.28982 0.7
      vertex 191.285 -0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.61 -1.28982 0.7
      vertex 194.715 -0.648714 0.7
      vertex 191.285 -0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.285 -0.275703 0.7
      vertex 194.715 -0.648714 0.7
      vertex 191.3 -1.22737e-15 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.715 -0.648714 0.7
      vertex 194.75 -3.91547e-16 0.7
      vertex 191.3 -1.22737e-15 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.3 -1.22737e-15 0.7
      vertex 194.75 -3.91547e-16 0.7
      vertex 191.285 0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.75 -3.91547e-16 0.7
      vertex 194.715 0.648714 0.7
      vertex 191.285 0.275703 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.285 0.275703 0.7
      vertex 194.715 0.648714 0.7
      vertex 191.24 0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.715 0.648714 0.7
      vertex 194.61 1.28982 0.7
      vertex 191.24 0.548175 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.24 0.548175 0.7
      vertex 194.61 1.28982 0.7
      vertex 191.167 0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.61 1.28982 0.7
      vertex 194.436 1.91581 0.7
      vertex 191.167 0.814219 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.167 0.814219 0.7
      vertex 194.436 1.91581 0.7
      vertex 191.064 1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.436 1.91581 0.7
      vertex 194.195 2.51933 0.7
      vertex 191.064 1.07072 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.064 1.07072 0.7
      vertex 194.195 2.51933 0.7
      vertex 190.935 1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 194.195 2.51933 0.7
      vertex 193.891 3.09332 0.7
      vertex 190.935 1.31466 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.935 1.31466 0.7
      vertex 193.891 3.09332 0.7
      vertex 190.78 1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.891 3.09332 0.7
      vertex 193.527 3.63105 0.7
      vertex 190.78 1.54319 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.78 1.54319 0.7
      vertex 193.527 3.63105 0.7
      vertex 190.601 1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.527 3.63105 0.7
      vertex 193.106 4.1262 0.7
      vertex 190.601 1.75363 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.601 1.75363 0.7
      vertex 193.106 4.1262 0.7
      vertex 190.401 1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 193.106 4.1262 0.7
      vertex 192.634 4.57297 0.7
      vertex 190.401 1.94351 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.401 1.94351 0.7
      vertex 192.634 4.57297 0.7
      vertex 190.181 2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.634 4.57297 0.7
      vertex 192.117 4.96613 0.7
      vertex 190.181 2.11061 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.181 2.11061 0.7
      vertex 192.117 4.96613 0.7
      vertex 189.944 2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 192.117 4.96613 0.7
      vertex 191.56 5.30107 0.7
      vertex 189.944 2.25296 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.944 2.25296 0.7
      vertex 191.56 5.30107 0.7
      vertex 189.694 2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 191.56 5.30107 0.7
      vertex 190.971 5.57386 0.7
      vertex 189.694 2.36889 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 189.694 2.36889 0.7
      vertex 190.971 5.57386 0.7
      vertex 189.432 2.45705 0.7
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 190.971 5.57386 0.7
      vertex 190.355 5.7813 0.7
      vertex 189.432 2.45705 0.7
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 3 10 9
      vertex 6 10 12
      vertex 3 -10 9
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 6 10 12
      vertex 6 -10 12
      vertex 3 -10 9
    endloop
  endfacet
  facet normal 0.0172576 -0.999851 -3.70017e-7
    outer loop
      vertex 113.493 -8.3 0
      vertex 195 -6.89317 0
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 0.0172577 -0.999851 0
    outer loop
      vertex 195 -6.89317 0
      vertex 195 -6.89317 1.3
      vertex 188.81 -7 1.3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 8.3 0
      vertex 15 10 0
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 10 0
      vertex 15 10 15
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 2.22452 15
      vertex 15 2.22452 12.0871
      vertex 15 10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 2.22452 12.0871
      vertex 15 2.22452 9.21554
      vertex 15 10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 2.22452 9.21554
      vertex 15 2.22452 7.87045
      vertex 15 10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 2.22452 7.87045
      vertex 15 2.22452 6.80323
      vertex 15 10 15
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 10 15
      vertex 15 2.22452 6.80323
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 2.22452 6.80323
      vertex 15 2.22452 1.95
      vertex 15 7 1.3
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15 7 1.3
      vertex 15 2.22452 1.95
      vertex 15 2.22452 1.3
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 98.9669 -2.22452 2.6
      vertex 98.9669 2.22452 2.6
      vertex 92.681 -2.22452 2.6
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 98.9669 2.22452 2.6
      vertex 92.681 2.22452 2.6
      vertex 92.681 -2.22452 2.6
    endloop
  endfacet
  facet normal 0.938558 -0.345122 0
    outer loop
      vertex 183.178 2.22452 1.3
      vertex 183.064 1.91581 1.30925
      vertex 183.064 1.91581 0.7
    endloop
  endfacet
  facet normal 0.963549 -0.267532 0
    outer loop
      vertex 183.064 1.91581 1.30925
      vertex 182.89 1.28982 1.32341
      vertex 183.064 1.91581 0.7
    endloop
  endfacet
  facet normal 0.963549 -0.267532 0
    outer loop
      vertex 183.064 1.91581 0.7
      vertex 182.89 1.28982 1.32341
      vertex 182.89 1.28982 0.7
    endloop
  endfacet
  facet normal 0.986824 -0.161795 0
    outer loop
      vertex 182.89 1.28982 1.32341
      vertex 182.785 0.648714 1.33197
      vertex 182.89 1.28982 0.7
    endloop
  endfacet
  facet normal 0.986824 -0.161795 0
    outer loop
      vertex 182.89 1.28982 0.7
      vertex 182.785 0.648714 1.33197
      vertex 182.785 0.648714 0.7
    endloop
  endfacet
  facet normal 0.998534 -0.0541304 0
    outer loop
      vertex 182.785 0.648714 1.33197
      vertex 182.75 3.43241e-16 1.33483
      vertex 182.785 0.648714 0.7
    endloop
  endfacet
  facet normal 0.998534 -0.0541304 0
    outer loop
      vertex 182.785 0.648714 0.7
      vertex 182.75 3.43241e-16 1.33483
      vertex 182.75 3.43241e-16 0.7
    endloop
  endfacet
  facet normal 0.998534 0.0541304 0
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 182.785 -0.648714 1.33197
      vertex 182.75 3.43241e-16 0.7
    endloop
  endfacet
  facet normal 0.998534 0.0541304 0
    outer loop
      vertex 182.75 3.43241e-16 0.7
      vertex 182.785 -0.648714 1.33197
      vertex 182.785 -0.648714 0.7
    endloop
  endfacet
  facet normal 0.986824 0.161795 0
    outer loop
      vertex 182.785 -0.648714 1.33197
      vertex 182.89 -1.28982 1.32341
      vertex 182.785 -0.648714 0.7
    endloop
  endfacet
  facet normal 0.986824 0.161795 0
    outer loop
      vertex 182.785 -0.648714 0.7
      vertex 182.89 -1.28982 1.32341
      vertex 182.89 -1.28982 0.7
    endloop
  endfacet
  facet normal 0.963549 0.267532 0
    outer loop
      vertex 182.89 -1.28982 1.32341
      vertex 183.064 -1.91581 1.30925
      vertex 182.89 -1.28982 0.7
    endloop
  endfacet
  facet normal 0.963549 0.267532 0
    outer loop
      vertex 182.89 -1.28982 0.7
      vertex 183.064 -1.91581 1.30925
      vertex 183.064 -1.91581 0.7
    endloop
  endfacet
  facet normal 0.938558 0.345122 0
    outer loop
      vertex 183.064 -1.91581 1.30925
      vertex 183.178 -2.22452 1.3
      vertex 183.064 -1.91581 0.7
    endloop
  endfacet
  facet normal 0.92888 0.37009 0.0146774
    outer loop
      vertex 183.064 -1.91581 0.7
      vertex 183.178 -2.22452 1.3
      vertex 183.305 -2.51933 0.7
    endloop
  endfacet
  facet normal 0.918474 0.39548 0
    outer loop
      vertex 183.178 -2.22452 1.3
      vertex 183.305 -2.51933 1.3
      vertex 183.305 -2.51933 0.7
    endloop
  endfacet
  facet normal 0.883511 0.468411 0
    outer loop
      vertex 183.305 -2.51933 0.7
      vertex 183.305 -2.51933 1.3
      vertex 183.609 -3.09332 0.7
    endloop
  endfacet
  facet normal 0.883511 0.468411 0
    outer loop
      vertex 183.305 -2.51933 1.3
      vertex 183.609 -3.09332 1.3
      vertex 183.609 -3.09332 0.7
    endloop
  endfacet
  facet normal 0.827688 0.561189 0
    outer loop
      vertex 183.609 -3.09332 0.7
      vertex 183.609 -3.09332 1.3
      vertex 183.973 -3.63105 0.7
    endloop
  endfacet
  facet normal 0.827688 0.561189 0
    outer loop
      vertex 183.609 -3.09332 1.3
      vertex 183.973 -3.63105 1.3
      vertex 183.973 -3.63105 0.7
    endloop
  endfacet
  facet normal 0.762162 0.647386 0
    outer loop
      vertex 183.973 -3.63105 0.7
      vertex 183.973 -3.63105 1.3
      vertex 184.394 -4.1262 0.7
    endloop
  endfacet
  facet normal 0.762162 0.647386 0
    outer loop
      vertex 183.973 -3.63105 1.3
      vertex 184.394 -4.1262 1.3
      vertex 184.394 -4.1262 0.7
    endloop
  endfacet
  facet normal 0.687702 0.725993 0
    outer loop
      vertex 184.394 -4.1262 0.7
      vertex 184.394 -4.1262 1.3
      vertex 184.866 -4.57297 0.7
    endloop
  endfacet
  facet normal 0.687702 0.725993 0
    outer loop
      vertex 184.394 -4.1262 1.3
      vertex 184.866 -4.57297 1.3
      vertex 184.866 -4.57297 0.7
    endloop
  endfacet
  facet normal 0.605179 0.79609 0
    outer loop
      vertex 184.866 -4.57297 0.7
      vertex 184.866 -4.57297 1.3
      vertex 185.383 -4.96613 0.7
    endloop
  endfacet
  facet normal 0.605179 0.79609 0
    outer loop
      vertex 184.866 -4.57297 1.3
      vertex 185.383 -4.96613 1.3
      vertex 185.383 -4.96613 0.7
    endloop
  endfacet
  facet normal 0.51555 0.85686 0
    outer loop
      vertex 185.383 -4.96613 0.7
      vertex 185.383 -4.96613 1.3
      vertex 185.94 -5.30107 0.7
    endloop
  endfacet
  facet normal 0.51555 0.85686 0
    outer loop
      vertex 185.383 -4.96613 1.3
      vertex 185.94 -5.30107 1.3
      vertex 185.94 -5.30107 0.7
    endloop
  endfacet
  facet normal 0.419888 0.907576 0
    outer loop
      vertex 185.94 -5.30107 0.7
      vertex 185.94 -5.30107 1.3
      vertex 186.529 -5.57386 0.7
    endloop
  endfacet
  facet normal 0.419888 0.907576 0
    outer loop
      vertex 185.94 -5.30107 1.3
      vertex 186.529 -5.57386 1.3
      vertex 186.529 -5.57386 0.7
    endloop
  endfacet
  facet normal 0.319303 0.947653 0
    outer loop
      vertex 186.529 -5.57386 0.7
      vertex 186.529 -5.57386 1.3
      vertex 187.145 -5.7813 0.7
    endloop
  endfacet
  facet normal 0.319303 0.947653 0
    outer loop
      vertex 186.529 -5.57386 1.3
      vertex 187.145 -5.7813 1.3
      vertex 187.145 -5.7813 0.7
    endloop
  endfacet
  facet normal 0.214971 0.97662 0
    outer loop
      vertex 187.145 -5.7813 0.7
      vertex 187.145 -5.7813 1.3
      vertex 187.779 -5.92096 0.7
    endloop
  endfacet
  facet normal 0.214971 0.97662 0
    outer loop
      vertex 187.145 -5.7813 1.3
      vertex 187.779 -5.92096 1.3
      vertex 187.779 -5.92096 0.7
    endloop
  endfacet
  facet normal 0.108119 0.994138 0
    outer loop
      vertex 187.779 -5.92096 0.7
      vertex 187.779 -5.92096 1.3
      vertex 188.425 -5.9912 0.7
    endloop
  endfacet
  facet normal 0.108119 0.994138 0
    outer loop
      vertex 187.779 -5.92096 1.3
      vertex 188.425 -5.9912 1.3
      vertex 188.425 -5.9912 0.7
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 188.425 -5.9912 0.7
      vertex 188.425 -5.9912 1.3
      vertex 189.075 -5.9912 0.7
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 188.425 -5.9912 1.3
      vertex 189.075 -5.9912 1.3
      vertex 189.075 -5.9912 0.7
    endloop
  endfacet
  facet normal -0.108119 0.994138 0
    outer loop
      vertex 189.075 -5.9912 0.7
      vertex 189.075 -5.9912 1.3
      vertex 189.721 -5.92096 0.7
    endloop
  endfacet
  facet normal -0.108119 0.994138 0
    outer loop
      vertex 189.075 -5.9912 1.3
      vertex 189.721 -5.92096 1.3
      vertex 189.721 -5.92096 0.7
    endloop
  endfacet
  facet normal -0.214971 0.97662 0
    outer loop
      vertex 189.721 -5.92096 0.7
      vertex 189.721 -5.92096 1.3
      vertex 190.355 -5.7813 0.7
    endloop
  endfacet
  facet normal -0.214971 0.97662 0
    outer loop
      vertex 189.721 -5.92096 1.3
      vertex 190.355 -5.7813 1.3
      vertex 190.355 -5.7813 0.7
    endloop
  endfacet
  facet normal -0.319303 0.947653 0
    outer loop
      vertex 190.355 -5.7813 0.7
      vertex 190.355 -5.7813 1.3
      vertex 190.971 -5.57386 0.7
    endloop
  endfacet
  facet normal -0.319303 0.947653 0
    outer loop
      vertex 190.355 -5.7813 1.3
      vertex 190.971 -5.57386 1.3
      vertex 190.971 -5.57386 0.7
    endloop
  endfacet
  facet normal -0.419888 0.907576 0
    outer loop
      vertex 190.971 -5.57386 0.7
      vertex 190.971 -5.57386 1.3
      vertex 191.56 -5.30107 0.7
    endloop
  endfacet
  facet normal -0.419888 0.907576 0
    outer loop
      vertex 190.971 -5.57386 1.3
      vertex 191.56 -5.30107 1.3
      vertex 191.56 -5.30107 0.7
    endloop
  endfacet
  facet normal -0.51555 0.85686 0
    outer loop
      vertex 191.56 -5.30107 0.7
      vertex 191.56 -5.30107 1.3
      vertex 192.117 -4.96613 0.7
    endloop
  endfacet
  facet normal -0.51555 0.85686 0
    outer loop
      vertex 191.56 -5.30107 1.3
      vertex 192.117 -4.96613 1.3
      vertex 192.117 -4.96613 0.7
    endloop
  endfacet
  facet normal -0.605179 0.79609 0
    outer loop
      vertex 192.117 -4.96613 0.7
      vertex 192.117 -4.96613 1.3
      vertex 192.634 -4.57297 0.7
    endloop
  endfacet
  facet normal -0.605179 0.79609 0
    outer loop
      vertex 192.117 -4.96613 1.3
      vertex 192.634 -4.57297 1.3
      vertex 192.634 -4.57297 0.7
    endloop
  endfacet
  facet normal -0.687702 0.725993 0
    outer loop
      vertex 192.634 -4.57297 0.7
      vertex 192.634 -4.57297 1.3
      vertex 193.106 -4.1262 0.7
    endloop
  endfacet
  facet normal -0.687702 0.725993 0
    outer loop
      vertex 192.634 -4.57297 1.3
      vertex 193.106 -4.1262 1.3
      vertex 193.106 -4.1262 0.7
    endloop
  endfacet
  facet normal -0.762162 0.647386 0
    outer loop
      vertex 193.106 -4.1262 0.7
      vertex 193.106 -4.1262 1.3
      vertex 193.527 -3.63105 0.7
    endloop
  endfacet
  facet normal -0.762162 0.647386 0
    outer loop
      vertex 193.106 -4.1262 1.3
      vertex 193.527 -3.63105 1.3
      vertex 193.527 -3.63105 0.7
    endloop
  endfacet
  facet normal -0.827688 0.561189 0
    outer loop
      vertex 193.527 -3.63105 0.7
      vertex 193.527 -3.63105 1.3
      vertex 193.891 -3.09332 0.7
    endloop
  endfacet
  facet normal -0.827688 0.561189 0
    outer loop
      vertex 193.527 -3.63105 1.3
      vertex 193.891 -3.09332 1.3
      vertex 193.891 -3.09332 0.7
    endloop
  endfacet
  facet normal -0.883511 0.468411 0
    outer loop
      vertex 193.891 -3.09332 0.7
      vertex 193.891 -3.09332 1.3
      vertex 194.195 -2.51933 0.7
    endloop
  endfacet
  facet normal -0.883511 0.468411 0
    outer loop
      vertex 193.891 -3.09332 1.3
      vertex 194.195 -2.51933 1.3
      vertex 194.195 -2.51933 0.7
    endloop
  endfacet
  facet normal -0.928972 0.370149 0
    outer loop
      vertex 194.195 -2.51933 0.7
      vertex 194.195 -2.51933 1.3
      vertex 194.436 -1.91581 0.7
    endloop
  endfacet
  facet normal -0.928972 0.370149 0
    outer loop
      vertex 194.195 -2.51933 1.3
      vertex 194.436 -1.91581 1.3
      vertex 194.436 -1.91581 0.7
    endloop
  endfacet
  facet normal -0.963555 0.267511 0
    outer loop
      vertex 194.436 -1.91581 0.7
      vertex 194.436 -1.91581 1.3
      vertex 194.61 -1.28982 0.7
    endloop
  endfacet
  facet normal -0.963555 0.267511 0
    outer loop
      vertex 194.436 -1.91581 1.3
      vertex 194.61 -1.28982 1.3
      vertex 194.61 -1.28982 0.7
    endloop
  endfacet
  facet normal -0.986824 0.161795 0
    outer loop
      vertex 194.61 -1.28982 0.7
      vertex 194.61 -1.28982 1.3
      vertex 194.715 -0.648714 0.7
    endloop
  endfacet
  facet normal -0.986824 0.161795 0
    outer loop
      vertex 194.61 -1.28982 1.3
      vertex 194.715 -0.648714 1.3
      vertex 194.715 -0.648714 0.7
    endloop
  endfacet
  facet normal -0.998534 0.0541304 0
    outer loop
      vertex 194.715 -0.648714 0.7
      vertex 194.715 -0.648714 1.3
      vertex 194.75 -3.91547e-16 0.7
    endloop
  endfacet
  facet normal -0.998534 0.0541304 1.27324e-16
    outer loop
      vertex 194.715 -0.648714 1.3
      vertex 194.75 -1.86112e-15 1.3
      vertex 194.75 -3.91547e-16 0.7
    endloop
  endfacet
  facet normal -0.998534 -0.0541304 -1.32581e-16
    outer loop
      vertex 194.75 -3.91547e-16 0.7
      vertex 194.75 -1.86112e-15 1.3
      vertex 194.715 0.648714 0.7
    endloop
  endfacet
  facet normal -0.998534 -0.0541304 0
    outer loop
      vertex 194.75 -1.86112e-15 1.3
      vertex 194.715 0.648714 1.3
      vertex 194.715 0.648714 0.7
    endloop
  endfacet
  facet normal -0.986824 -0.161795 0
    outer loop
      vertex 194.715 0.648714 0.7
      vertex 194.715 0.648714 1.3
      vertex 194.61 1.28982 0.7
    endloop
  endfacet
  facet normal -0.986824 -0.161795 0
    outer loop
      vertex 194.715 0.648714 1.3
      vertex 194.61 1.28982 1.3
      vertex 194.61 1.28982 0.7
    endloop
  endfacet
  facet normal -0.963555 -0.267511 0
    outer loop
      vertex 194.61 1.28982 0.7
      vertex 194.61 1.28982 1.3
      vertex 194.436 1.91581 0.7
    endloop
  endfacet
  facet normal -0.963555 -0.267511 0
    outer loop
      vertex 194.61 1.28982 1.3
      vertex 194.436 1.91581 1.3
      vertex 194.436 1.91581 0.7
    endloop
  endfacet
  facet normal -0.928972 -0.370149 0
    outer loop
      vertex 194.436 1.91581 0.7
      vertex 194.436 1.91581 1.3
      vertex 194.195 2.51933 0.7
    endloop
  endfacet
  facet normal -0.928972 -0.370149 0
    outer loop
      vertex 194.436 1.91581 1.3
      vertex 194.195 2.51933 1.3
      vertex 194.195 2.51933 0.7
    endloop
  endfacet
  facet normal -0.883511 -0.468411 0
    outer loop
      vertex 194.195 2.51933 0.7
      vertex 194.195 2.51933 1.3
      vertex 193.891 3.09332 0.7
    endloop
  endfacet
  facet normal -0.883511 -0.468411 0
    outer loop
      vertex 194.195 2.51933 1.3
      vertex 193.891 3.09332 1.3
      vertex 193.891 3.09332 0.7
    endloop
  endfacet
  facet normal -0.827688 -0.561189 0
    outer loop
      vertex 193.891 3.09332 0.7
      vertex 193.891 3.09332 1.3
      vertex 193.527 3.63105 0.7
    endloop
  endfacet
  facet normal -0.827688 -0.561189 0
    outer loop
      vertex 193.891 3.09332 1.3
      vertex 193.527 3.63105 1.3
      vertex 193.527 3.63105 0.7
    endloop
  endfacet
  facet normal -0.762162 -0.647386 0
    outer loop
      vertex 193.527 3.63105 0.7
      vertex 193.527 3.63105 1.3
      vertex 193.106 4.1262 0.7
    endloop
  endfacet
  facet normal -0.762162 -0.647386 0
    outer loop
      vertex 193.527 3.63105 1.3
      vertex 193.106 4.1262 1.3
      vertex 193.106 4.1262 0.7
    endloop
  endfacet
  facet normal -0.687702 -0.725993 0
    outer loop
      vertex 193.106 4.1262 0.7
      vertex 193.106 4.1262 1.3
      vertex 192.634 4.57297 0.7
    endloop
  endfacet
  facet normal -0.687702 -0.725993 0
    outer loop
      vertex 193.106 4.1262 1.3
      vertex 192.634 4.57297 1.3
      vertex 192.634 4.57297 0.7
    endloop
  endfacet
  facet normal -0.605179 -0.79609 0
    outer loop
      vertex 192.634 4.57297 0.7
      vertex 192.634 4.57297 1.3
      vertex 192.117 4.96613 0.7
    endloop
  endfacet
  facet normal -0.605179 -0.79609 0
    outer loop
      vertex 192.634 4.57297 1.3
      vertex 192.117 4.96613 1.3
      vertex 192.117 4.96613 0.7
    endloop
  endfacet
  facet normal -0.51555 -0.85686 0
    outer loop
      vertex 192.117 4.96613 0.7
      vertex 192.117 4.96613 1.3
      vertex 191.56 5.30107 0.7
    endloop
  endfacet
  facet normal -0.51555 -0.85686 0
    outer loop
      vertex 192.117 4.96613 1.3
      vertex 191.56 5.30107 1.3
      vertex 191.56 5.30107 0.7
    endloop
  endfacet
  facet normal -0.419888 -0.907576 0
    outer loop
      vertex 191.56 5.30107 0.7
      vertex 191.56 5.30107 1.3
      vertex 190.971 5.57386 0.7
    endloop
  endfacet
  facet normal -0.419888 -0.907576 0
    outer loop
      vertex 191.56 5.30107 1.3
      vertex 190.971 5.57386 1.3
      vertex 190.971 5.57386 0.7
    endloop
  endfacet
  facet normal -0.319303 -0.947653 0
    outer loop
      vertex 190.971 5.57386 0.7
      vertex 190.971 5.57386 1.3
      vertex 190.355 5.7813 0.7
    endloop
  endfacet
  facet normal -0.319303 -0.947653 0
    outer loop
      vertex 190.971 5.57386 1.3
      vertex 190.355 5.7813 1.3
      vertex 190.355 5.7813 0.7
    endloop
  endfacet
  facet normal -0.214971 -0.97662 0
    outer loop
      vertex 190.355 5.7813 0.7
      vertex 190.355 5.7813 1.3
      vertex 189.721 5.92096 0.7
    endloop
  endfacet
  facet normal -0.214971 -0.97662 0
    outer loop
      vertex 190.355 5.7813 1.3
      vertex 189.721 5.92096 1.3
      vertex 189.721 5.92096 0.7
    endloop
  endfacet
  facet normal -0.108119 -0.994138 0
    outer loop
      vertex 189.721 5.92096 0.7
      vertex 189.721 5.92096 1.3
      vertex 189.075 5.9912 0.7
    endloop
  endfacet
  facet normal -0.108119 -0.994138 0
    outer loop
      vertex 189.721 5.92096 1.3
      vertex 189.075 5.9912 1.3
      vertex 189.075 5.9912 0.7
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 189.075 5.9912 0.7
      vertex 189.075 5.9912 1.3
      vertex 188.425 5.9912 0.7
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 189.075 5.9912 1.3
      vertex 188.425 5.9912 1.3
      vertex 188.425 5.9912 0.7
    endloop
  endfacet
  facet normal 0.108119 -0.994138 0
    outer loop
      vertex 188.425 5.9912 0.7
      vertex 188.425 5.9912 1.3
      vertex 187.779 5.92096 0.7
    endloop
  endfacet
  facet normal 0.108119 -0.994138 0
    outer loop
      vertex 188.425 5.9912 1.3
      vertex 187.779 5.92096 1.3
      vertex 187.779 5.92096 0.7
    endloop
  endfacet
  facet normal 0.214971 -0.97662 0
    outer loop
      vertex 187.779 5.92096 0.7
      vertex 187.779 5.92096 1.3
      vertex 187.145 5.7813 0.7
    endloop
  endfacet
  facet normal 0.214971 -0.97662 0
    outer loop
      vertex 187.779 5.92096 1.3
      vertex 187.145 5.7813 1.3
      vertex 187.145 5.7813 0.7
    endloop
  endfacet
  facet normal 0.319303 -0.947653 0
    outer loop
      vertex 187.145 5.7813 0.7
      vertex 187.145 5.7813 1.3
      vertex 186.529 5.57386 0.7
    endloop
  endfacet
  facet normal 0.319303 -0.947653 0
    outer loop
      vertex 187.145 5.7813 1.3
      vertex 186.529 5.57386 1.3
      vertex 186.529 5.57386 0.7
    endloop
  endfacet
  facet normal 0.419888 -0.907576 0
    outer loop
      vertex 186.529 5.57386 0.7
      vertex 186.529 5.57386 1.3
      vertex 185.94 5.30107 0.7
    endloop
  endfacet
  facet normal 0.419888 -0.907576 0
    outer loop
      vertex 186.529 5.57386 1.3
      vertex 185.94 5.30107 1.3
      vertex 185.94 5.30107 0.7
    endloop
  endfacet
  facet normal 0.51555 -0.85686 0
    outer loop
      vertex 185.94 5.30107 0.7
      vertex 185.94 5.30107 1.3
      vertex 185.383 4.96613 0.7
    endloop
  endfacet
  facet normal 0.51555 -0.85686 0
    outer loop
      vertex 185.94 5.30107 1.3
      vertex 185.383 4.96613 1.3
      vertex 185.383 4.96613 0.7
    endloop
  endfacet
  facet normal 0.605179 -0.79609 0
    outer loop
      vertex 185.383 4.96613 0.7
      vertex 185.383 4.96613 1.3
      vertex 184.866 4.57297 0.7
    endloop
  endfacet
  facet normal 0.605179 -0.79609 0
    outer loop
      vertex 185.383 4.96613 1.3
      vertex 184.866 4.57297 1.3
      vertex 184.866 4.57297 0.7
    endloop
  endfacet
  facet normal 0.687702 -0.725993 0
    outer loop
      vertex 184.866 4.57297 0.7
      vertex 184.866 4.57297 1.3
      vertex 184.394 4.1262 0.7
    endloop
  endfacet
  facet normal 0.687702 -0.725993 0
    outer loop
      vertex 184.866 4.57297 1.3
      vertex 184.394 4.1262 1.3
      vertex 184.394 4.1262 0.7
    endloop
  endfacet
  facet normal 0.762162 -0.647386 0
    outer loop
      vertex 184.394 4.1262 0.7
      vertex 184.394 4.1262 1.3
      vertex 183.973 3.63105 0.7
    endloop
  endfacet
  facet normal 0.762162 -0.647386 0
    outer loop
      vertex 184.394 4.1262 1.3
      vertex 183.973 3.63105 1.3
      vertex 183.973 3.63105 0.7
    endloop
  endfacet
  facet normal 0.827688 -0.561189 0
    outer loop
      vertex 183.973 3.63105 0.7
      vertex 183.973 3.63105 1.3
      vertex 183.609 3.09332 0.7
    endloop
  endfacet
  facet normal 0.827688 -0.561189 0
    outer loop
      vertex 183.973 3.63105 1.3
      vertex 183.609 3.09332 1.3
      vertex 183.609 3.09332 0.7
    endloop
  endfacet
  facet normal 0.883511 -0.468411 0
    outer loop
      vertex 183.609 3.09332 0.7
      vertex 183.609 3.09332 1.3
      vertex 183.305 2.51933 0.7
    endloop
  endfacet
  facet normal 0.883511 -0.468411 0
    outer loop
      vertex 183.609 3.09332 1.3
      vertex 183.305 2.51933 1.3
      vertex 183.305 2.51933 0.7
    endloop
  endfacet
  facet normal 0.92898 -0.37013 0
    outer loop
      vertex 183.305 2.51933 0.7
      vertex 183.305 2.51933 1.3
      vertex 183.064 1.91581 0.7
    endloop
  endfacet
  facet normal 0.918069 -0.395306 0.0296969
    outer loop
      vertex 183.305 2.51933 1.3
      vertex 183.178 2.22452 1.3
      vertex 183.064 1.91581 0.7
    endloop
  endfacet
  facet normal -0.820783 0 -0.57124
    outer loop
      vertex 95.824 -2.22452 7.11596
      vertex 95.824 2.22452 7.11596
      vertex 98.9669 -2.22452 2.6
    endloop
  endfacet
  facet normal -0.820783 0 -0.57124
    outer loop
      vertex 95.824 2.22452 7.11596
      vertex 98.9669 2.22452 2.6
      vertex 98.9669 -2.22452 2.6
    endloop
  endfacet
  facet normal 0.0811925 3.59652e-6 0.996698
    outer loop
      vertex 183.064 1.91581 1.30925
      vertex 183.178 2.22452 1.3
      vertex 175.198 2.22452 1.95
    endloop
  endfacet
  facet normal 0.0811916 0 0.996699
    outer loop
      vertex 15 2.22452 15
      vertex 15 -2.22452 15
      vertex 15.65 -2.22452 14.9471
    endloop
  endfacet
  facet normal 0.0811925 -3.59652e-6 0.996698
    outer loop
      vertex 175.198 -2.22452 1.95
      vertex 183.178 -2.22452 1.3
      vertex 183.064 -1.91581 1.30925
    endloop
  endfacet
  facet normal 0.0811926 5.55652e-7 0.996698
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 182.785 0.648714 1.33197
      vertex 115.621 2.22452 6.80323
    endloop
  endfacet
  facet normal 0.0811926 1.4676e-7 0.996698
    outer loop
      vertex 115.621 2.22452 6.80323
      vertex 182.785 0.648714 1.33197
      vertex 175.198 2.22452 1.95
    endloop
  endfacet
  facet normal 0.0811923 -9.69645e-7 0.996698
    outer loop
      vertex 182.785 0.648714 1.33197
      vertex 182.89 1.28982 1.32341
      vertex 175.198 2.22452 1.95
    endloop
  endfacet
  facet normal 0.0811924 -3.94457e-7 0.996698
    outer loop
      vertex 175.198 2.22452 1.95
      vertex 182.89 1.28982 1.32341
      vertex 183.064 1.91581 1.30925
    endloop
  endfacet
  facet normal 0.0811925 1.39094e-7 0.996698
    outer loop
      vertex 15.65 -2.22452 14.9471
      vertex 34.8 -2.22452 13.3871
      vertex 15 2.22452 15
    endloop
  endfacet
  facet normal 0.0811926 3.33456e-7 0.996698
    outer loop
      vertex 34.8 -2.22452 13.3871
      vertex 50.7585 -2.22452 12.0871
      vertex 15 2.22452 15
    endloop
  endfacet
  facet normal 0.0811925 -7.20058e-8 0.996698
    outer loop
      vertex 15 2.22452 15
      vertex 50.7585 -2.22452 12.0871
      vertex 54.8 -2.22452 11.7578
    endloop
  endfacet
  facet normal 0.0811926 1.44613e-6 0.996698
    outer loop
      vertex 115.621 2.22452 6.80323
      vertex 102.52 2.22452 7.87045
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811925 -1.0326e-6 0.996698
    outer loop
      vertex 102.52 2.22452 7.87045
      vertex 92.031 2.22452 8.72494
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811926 1.34576e-6 0.996698
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 92.031 2.22452 8.72494
      vertex 86.0085 2.22452 9.21554
    endloop
  endfacet
  facet normal 0.0811926 1.14379e-6 0.996698
    outer loop
      vertex 86.0085 2.22452 9.21554
      vertex 82.95 2.22452 9.46469
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811925 -4.4196e-7 0.996698
    outer loop
      vertex 82.95 2.22452 9.46469
      vertex 70.8 2.22452 10.4544
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811925 -2.3576e-6 0.996698
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 70.8 2.22452 10.4544
      vertex 54.8 2.22452 11.7578
    endloop
  endfacet
  facet normal 0.0811925 -2.18627e-7 0.996698
    outer loop
      vertex 54.8 2.22452 11.7578
      vertex 50.7585 2.22452 12.0871
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811926 2.77465e-6 0.996698
    outer loop
      vertex 50.7585 2.22452 12.0871
      vertex 34.8 2.22452 13.3871
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811925 -1.2998e-7 0.996698
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 34.8 2.22452 13.3871
      vertex 15.65 2.22452 14.9471
    endloop
  endfacet
  facet normal 0.0811925 -4.04679e-7 0.996698
    outer loop
      vertex 54.8 -2.22452 11.7578
      vertex 70.8 -2.22452 10.4544
      vertex 15 2.22452 15
    endloop
  endfacet
  facet normal 0.0811925 7.27336e-8 0.996698
    outer loop
      vertex 70.8 -2.22452 10.4544
      vertex 82.95 -2.22452 9.46469
      vertex 15 2.22452 15
    endloop
  endfacet
  facet normal 0.0811926 6.12573e-7 0.996698
    outer loop
      vertex 15 2.22452 15
      vertex 82.95 -2.22452 9.46469
      vertex 86.0085 -2.22452 9.21554
    endloop
  endfacet
  facet normal 0.0811924 3.94457e-7 0.996698
    outer loop
      vertex 183.064 -1.91581 1.30925
      vertex 182.89 -1.28982 1.32341
      vertex 175.198 -2.22452 1.95
    endloop
  endfacet
  facet normal 0.0811923 9.69645e-7 0.996698
    outer loop
      vertex 182.89 -1.28982 1.32341
      vertex 182.785 -0.648714 1.33197
      vertex 175.198 -2.22452 1.95
    endloop
  endfacet
  facet normal 0.0811926 -1.4676e-7 0.996698
    outer loop
      vertex 175.198 -2.22452 1.95
      vertex 182.785 -0.648714 1.33197
      vertex 115.621 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.0811926 -1.81338e-6 0.996698
    outer loop
      vertex 182.785 -0.648714 1.33197
      vertex 102.52 -2.22452 7.87045
      vertex 115.621 -2.22452 6.80323
    endloop
  endfacet
  facet normal 0.0811916 -7.16457e-5 0.996699
    outer loop
      vertex 15.65 2.22452 14.9471
      vertex 15 2.22452 15
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811925 1.41039e-7 0.996698
    outer loop
      vertex 15 2.22452 15
      vertex 86.0085 -2.22452 9.21554
      vertex 182.75 3.43241e-16 1.33483
    endloop
  endfacet
  facet normal 0.0811926 -5.55602e-7 0.996698
    outer loop
      vertex 182.75 3.43241e-16 1.33483
      vertex 86.0085 -2.22452 9.21554
      vertex 182.785 -0.648714 1.33197
    endloop
  endfacet
  facet normal 0.0811926 -1.67145e-6 0.996698
    outer loop
      vertex 86.0085 -2.22452 9.21554
      vertex 92.031 -2.22452 8.72494
      vertex 182.785 -0.648714 1.33197
    endloop
  endfacet
  facet normal 0.0811925 1.68732e-6 0.996698
    outer loop
      vertex 182.785 -0.648714 1.33197
      vertex 92.031 -2.22452 8.72494
      vertex 102.52 -2.22452 7.87045
    endloop
  endfacet
  facet normal 0.820784 0 -0.571239
    outer loop
      vertex 92.681 -2.22452 2.6
      vertex 92.681 2.22452 2.6
      vertex 95.824 -2.22452 7.11596
    endloop
  endfacet
  facet normal 0.820784 0 -0.571239
    outer loop
      vertex 92.681 2.22452 2.6
      vertex 95.824 2.22452 7.11596
      vertex 95.824 -2.22452 7.11596
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 195 6.89317 1.3
      vertex 195 -6.89317 1.3
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 195 -6.89317 1.3
      vertex 195 -6.89317 0
      vertex 195 6.89317 2.08167e-14
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 87.4905 -2.22452 6.49051
      vertex 87.4905 2.22452 6.49051
      vertex 91.381 -2.22452 2.6
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex 87.4905 2.22452 6.49051
      vertex 91.381 2.22452 2.6
      vertex 91.381 -2.22452 2.6
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 87.4905 -2.22452 6.49051
      vertex 83.6 -2.22452 2.6
      vertex 87.4905 2.22452 6.49051
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex 83.6 -2.22452 2.6
      vertex 83.6 2.22452 2.6
      vertex 87.4905 2.22452 6.49051
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 82.3 -2.22452 3.62495
      vertex 82.3 2.22452 3.62495
      vertex 82.3 -2.22452 2.6
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 82.3 2.22452 3.62495
      vertex 82.3 2.22452 2.6
      vertex 82.3 -2.22452 2.6
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 72.3 -2.22452 3.62495
      vertex 72.3 -2.22452 2.6
      vertex 72.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 72.3 -2.22452 2.6
      vertex 72.3 2.22452 2.6
      vertex 72.3 2.22452 3.62495
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15.2 -51 -5.2
      vertex 0.394011 -51 -5.2
      vertex 15.2 12 -5.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 0.394011 -51 -5.2
      vertex -22.7 -11 -5.2
      vertex 15.2 12 -5.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15.2 12 -5.2
      vertex -22.7 -11 -5.2
      vertex -22.7 12 -5.2
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex -7.675 12 17
      vertex -7.675 -11 17
      vertex -11.35 12 13.325
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex -7.675 -11 17
      vertex -11.35 -11 13.325
      vertex -11.35 12 13.325
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -11.35 12 13.325
      vertex -11.35 -11 13.325
      vertex -11.35 12 -0.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -11.35 -11 13.325
      vertex -11.35 -11 -0.2
      vertex -11.35 12 -0.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -13.35 -11 -0.2
      vertex -13.35 -11 13.325
      vertex -13.35 12 -0.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -13.35 -11 13.325
      vertex -13.35 12 13.325
      vertex -13.35 12 -0.2
    endloop
  endfacet
  facet normal 0.707107 0 0.707107
    outer loop
      vertex 15.2 10 -1.2
      vertex 14.2 10 -0.2
      vertex 15.2 -51 -1.2
    endloop
  endfacet
  facet normal 0.707107 0 0.707107
    outer loop
      vertex 14.2 10 -0.2
      vertex 14.2 -51 -0.2
      vertex 15.2 -51 -1.2
    endloop
  endfacet
  facet normal -0.866025 -0.5 0
    outer loop
      vertex 0.394011 -51 -5.2
      vertex 0.394011 -51 -0.2
      vertex -22.7 -11 -5.2
    endloop
  endfacet
  facet normal -0.866025 -0.5 0
    outer loop
      vertex 0.394011 -51 -0.2
      vertex -22.7 -11 -0.2
      vertex -22.7 -11 -5.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -22.7 -11 19
      vertex -22.7 12 19
      vertex -22.7 -11 -0.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -22.7 12 19
      vertex -22.7 12 -5.2
      vertex -22.7 -11 -0.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -22.7 -11 -0.2
      vertex -22.7 12 -5.2
      vertex -22.7 -11 -5.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 14.2 -51 -0.2
      vertex 0.394011 -51 -0.2
      vertex 15.2 -51 -1.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 0.394011 -51 -0.2
      vertex 0.394011 -51 -5.2
      vertex 15.2 -51 -1.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 -51 -1.2
      vertex 0.394011 -51 -5.2
      vertex 15.2 -51 -5.2
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex -4 12 13.325
      vertex -4 -11 13.325
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex -4 -11 13.325
      vertex -7.675 -11 17
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -0.2 10 -0.2
      vertex -0.2 10 15.2
      vertex -0.2 -11 -0.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -0.2 10 15.2
      vertex -0.2 -11 15.2
      vertex -0.2 -11 -0.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -0.2 10 15.2
      vertex 15.2 10 15.2
      vertex -0.2 -11 15.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15.2 10 15.2
      vertex 15.2 -11 15.2
      vertex -0.2 -11 15.2
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex -13.35 12 13.325
      vertex -13.35 -11 13.325
      vertex -17.025 12 17
    endloop
  endfacet
  facet normal -0.707107 0 -0.707107
    outer loop
      vertex -13.35 -11 13.325
      vertex -17.025 -11 17
      vertex -17.025 12 17
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 15.2 -11 15.2
      vertex 15.2 10 15.2
      vertex 15.2 -11 13.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 15.2 10 15.2
      vertex 15.2 10 13.2
      vertex 15.2 -11 13.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.2 -10 3.2
      vertex 3.2 10 3.2
      vertex 11.8 -10 3.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 3.2 10 3.2
      vertex 11.8 10 3.2
      vertex 11.8 -10 3.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 3.2 -10 8.91716
      vertex 3.2 -10 3.2
      vertex 6.08284 -10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 3.2 -10 3.2
      vertex 11.8 -10 3.2
      vertex 6.08284 -10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 6.08284 -10 11.8
      vertex 11.8 -10 3.2
      vertex 8.91716 -10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 11.8 -10 3.2
      vertex 11.8 -10 8.91716
      vertex 8.91716 -10 11.8
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -13.35 -11 -0.2
      vertex -13.35 12 -0.2
      vertex -20.7 12 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -20.7 -11 -0.2
      vertex -22.7 -11 -0.2
      vertex 0.394011 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 14.2 10 -0.2
      vertex -0.2 10 -0.2
      vertex 14.2 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -0.2 10 -0.2
      vertex -0.2 -11 -0.2
      vertex 14.2 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -4 12 -0.2
      vertex -11.35 12 -0.2
      vertex -4 -11 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -11.35 12 -0.2
      vertex -11.35 -11 -0.2
      vertex -4 -11 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -0.2 -11 -0.2
      vertex -4 -11 -0.2
      vertex 14.2 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -4 -11 -0.2
      vertex -11.35 -11 -0.2
      vertex 14.2 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 14.2 -51 -0.2
      vertex -11.35 -11 -0.2
      vertex 0.394011 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -11.35 -11 -0.2
      vertex -13.35 -11 -0.2
      vertex 0.394011 -51 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 0.394011 -51 -0.2
      vertex -13.35 -11 -0.2
      vertex -20.7 -11 -0.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -13.35 -11 -0.2
      vertex -20.7 12 -0.2
      vertex -20.7 -11 -0.2
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex -17.025 -11 17
      vertex -20.7 -11 13.325
      vertex -17.025 12 17
    endloop
  endfacet
  facet normal 0.707107 0 -0.707107
    outer loop
      vertex -20.7 -11 13.325
      vertex -20.7 12 13.325
      vertex -17.025 12 17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -0.2 10 15.2
      vertex -0.2 10 -0.2
      vertex 3.2 10 3.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 3.2 10 3.2
      vertex -0.2 10 -0.2
      vertex 11.8 10 3.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -0.2 10 -0.2
      vertex 14.2 10 -0.2
      vertex 11.8 10 3.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 14.2 10 -0.2
      vertex 15.2 10 -1.2
      vertex 11.8 10 3.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 11.8 10 3.2
      vertex 15.2 10 -1.2
      vertex 11.8 10 8.91716
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 10 -1.2
      vertex 15.2 10 13.2
      vertex 11.8 10 8.91716
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 11.8 10 8.91716
      vertex 15.2 10 13.2
      vertex 8.91716 10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 10 13.2
      vertex 15.2 10 15.2
      vertex 8.91716 10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 8.91716 10 11.8
      vertex 15.2 10 15.2
      vertex 6.08284 10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 10 15.2
      vertex -0.2 10 15.2
      vertex 6.08284 10 11.8
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 6.08284 10 11.8
      vertex -0.2 10 15.2
      vertex 3.2 10 8.91716
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -0.2 10 15.2
      vertex 3.2 10 3.2
      vertex 3.2 10 8.91716
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -22.7 -11 19
      vertex -22.7 -11 -0.2
      vertex -20.7 -11 -0.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 19 -11 19
      vertex -22.7 -11 19
      vertex -7.675 -11 17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -13.35 -11 13.325
      vertex -13.35 -11 -0.2
      vertex -11.35 -11 -0.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -4 -11 -0.2
      vertex -0.2 -11 -0.2
      vertex -4 -11 13.325
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -0.2 -11 -0.2
      vertex -0.2 -11 15.2
      vertex -4 -11 13.325
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 -11 13.2
      vertex 19 -11 13.2
      vertex 15.2 -11 15.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 19 -11 13.2
      vertex 19 -11 19
      vertex 15.2 -11 15.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 15.2 -11 15.2
      vertex 19 -11 19
      vertex -0.2 -11 15.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 19 -11 19
      vertex -7.675 -11 17
      vertex -0.2 -11 15.2
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -0.2 -11 15.2
      vertex -7.675 -11 17
      vertex -4 -11 13.325
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -20.7 -11 -0.2
      vertex -20.7 -11 13.325
      vertex -22.7 -11 19
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -20.7 -11 13.325
      vertex -17.025 -11 17
      vertex -22.7 -11 19
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -22.7 -11 19
      vertex -17.025 -11 17
      vertex -7.675 -11 17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -17.025 -11 17
      vertex -13.35 -11 13.325
      vertex -7.675 -11 17
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -7.675 -11 17
      vertex -13.35 -11 13.325
      vertex -11.35 -11 13.325
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex -13.35 -11 13.325
      vertex -11.35 -11 -0.2
      vertex -11.35 -11 13.325
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 19 12 19
      vertex 19 12 13.2
      vertex 15.2 12 13.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -22.7 12 19
      vertex 19 12 19
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 19 12 19
      vertex 15.2 12 13.2
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -7.675 12 17
      vertex 15.2 12 13.2
      vertex -4 12 13.325
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.2 12 13.2
      vertex -4 12 -0.2
      vertex -4 12 13.325
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.2 12 13.2
      vertex 15.2 12 -5.2
      vertex -4 12 -0.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 15.2 12 -5.2
      vertex -22.7 12 -5.2
      vertex -4 12 -0.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -4 12 -0.2
      vertex -22.7 12 -5.2
      vertex -11.35 12 -0.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -22.7 12 -5.2
      vertex -13.35 12 -0.2
      vertex -11.35 12 -0.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -11.35 12 -0.2
      vertex -13.35 12 -0.2
      vertex -11.35 12 13.325
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -13.35 12 -0.2
      vertex -13.35 12 13.325
      vertex -11.35 12 13.325
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -11.35 12 13.325
      vertex -13.35 12 13.325
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -13.35 12 13.325
      vertex -17.025 12 17
      vertex -7.675 12 17
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -7.675 12 17
      vertex -17.025 12 17
      vertex -22.7 12 19
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -17.025 12 17
      vertex -20.7 12 13.325
      vertex -22.7 12 19
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -22.7 12 19
      vertex -20.7 12 13.325
      vertex -22.7 12 -5.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -20.7 12 13.325
      vertex -20.7 12 -0.2
      vertex -22.7 12 -5.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex -22.7 12 -5.2
      vertex -20.7 12 -0.2
      vertex -13.35 12 -0.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 3.2 -10 8.91716
      vertex 3.2 10 8.91716
      vertex 3.2 -10 3.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 3.2 10 8.91716
      vertex 3.2 10 3.2
      vertex 3.2 -10 3.2
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -4 12 -0.2
      vertex -4 -11 -0.2
      vertex -4 12 13.325
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex -4 -11 -0.2
      vertex -4 -11 13.325
      vertex -4 12 13.325
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 11.8 -10 3.2
      vertex 11.8 10 3.2
      vertex 11.8 -10 8.91716
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 11.8 10 3.2
      vertex 11.8 10 8.91716
      vertex 11.8 -10 8.91716
    endloop
  endfacet
  facet normal 0.707107 0 0.707107
    outer loop
      vertex 11.8 -10 8.91716
      vertex 11.8 10 8.91716
      vertex 8.91716 -10 11.8
    endloop
  endfacet
  facet normal 0.707107 0 0.707107
    outer loop
      vertex 11.8 10 8.91716
      vertex 8.91716 10 11.8
      vertex 8.91716 -10 11.8
    endloop
  endfacet
  facet normal -0.707107 0 0.707107
    outer loop
      vertex 6.08284 -10 11.8
      vertex 6.08284 10 11.8
      vertex 3.2 -10 8.91716
    endloop
  endfacet
  facet normal -0.707107 0 0.707107
    outer loop
      vertex 6.08284 10 11.8
      vertex 3.2 10 8.91716
      vertex 3.2 -10 8.91716
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 8.91716 -10 11.8
      vertex 8.91716 10 11.8
      vertex 6.08284 -10 11.8
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 8.91716 10 11.8
      vertex 6.08284 10 11.8
      vertex 6.08284 -10 11.8
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15.2 -51 -1.2
      vertex 15.2 -51 -5.2
      vertex 15.2 10 -1.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15.2 -51 -5.2
      vertex 15.2 12 -5.2
      vertex 15.2 10 -1.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15.2 10 -1.2
      vertex 15.2 12 -5.2
      vertex 15.2 10 13.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 15.2 12 -5.2
      vertex 15.2 12 13.2
      vertex 15.2 10 13.2
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -22.7 -11 19
      vertex 19 -11 19
      vertex -22.7 12 19
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex 19 -11 19
      vertex 19 12 19
      vertex -22.7 12 19
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -20.7 12 13.325
      vertex -20.7 -11 13.325
      vertex -20.7 12 -0.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex -20.7 -11 13.325
      vertex -20.7 -11 -0.2
      vertex -20.7 12 -0.2
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 19 -11 13.2
      vertex 19 12 13.2
      vertex 19 -11 19
    endloop
  endfacet
  facet normal 1 0 0
    outer loop
      vertex 19 12 13.2
      vertex 19 12 19
      vertex 19 -11 19
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15.2 12 13.2
      vertex 19 12 13.2
      vertex 15.2 10 13.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 19 12 13.2
      vertex 19 -11 13.2
      vertex 15.2 10 13.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex 15.2 10 13.2
      vertex 19 -11 13.2
      vertex 15.2 -11 13.2
    endloop
  endfacet
endsolid Mesh

```  

### Reflection
This assignment was a good intro into onshape again and i liked the competitive aspect. This assignment was obviously design heavy and the major design choice were made were formed of of the if it aint broke dont fix it concept taking inspiration from previous designs that worked and adapting what we thought would work well. Another thing we did is tackle the problem individually and then take what we thought was the best solution this encouraged each one of us to come up with our own creative solutions.