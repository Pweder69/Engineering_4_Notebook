from adafruit_display_text import label #type: ignore
import adafruit_displayio_ssd1306 #type: ignore
import displayio #type: ignore
import busio # type: ignore
import board # type: ignore
import time # type: ignore
import math
import terminalio #type: ignore
from adafruit_display_shapes.triangle import Triangle #type: ignore
from adafruit_display_shapes.line import Line   #type: ignore
from adafruit_display_shapes.circle import Circle #type: ignore
displayio.release_displays()


sda_pin = board.GP14
scl_pin = board.GP15

i2c = busio.I2C(scl_pin, sda_pin)   

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address= 0x3d ,reset=board.GP10)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


SWidth  = 128
SHeight = 64
screenGroup = displayio.Group()

def rgb_to_hex(red, green, blue):
    hex_code = (red << 16) + (green << 8) + blue
    return hex(hex_code)


def drawGrid():
    white = rgb_to_hex(255,255,255)
    screenGroup.append(Line(SWidth//2,0,SWidth//2,SHeight, color= 0xFFFFFF ))
    screenGroup.append(Line(0,SHeight//2,SWidth,SHeight//2, color= 0xFFFFFF))

def getArea(p1,p2,p3):
            side1 = (1/2) * \
                    abs(
                        p1[0]*(p2[1]-(p3[1]))  + 
                        p2[0]*(p3[1]-(p1[1]))  + 
                        p3[0]*(p1[1]-(p2[1]))
                        )
                        # In accordance to the area of a triangle formula relative to coordinate geometry
                        # https://www.cuemath.com/geometry/area-of-triangle-in-coordinate-geometry/
            return side1    


def transformCords(cords): # transforms the coordinates relative to the center of the screen and scales them up by "multiplier".
    multiplier = 4
    x = (cords[0] * multiplier) + SWidth//2
    y = SHeight//2 + (cords[1] * multiplier)
    return x,y


while True:
    
    p1 = input("First point: ")
    p2 = input("second point: ") # Must grab inputs outside of the main try loop or else we get stuck
    p3 = input("third point: ") 
    
    #try:
        

    l = [p1,p2,p3]
    AL = []
    nl = [] 
    for i,point in enumerate(l):
        AL.append(tuple(int(x) for x in point.split(","))) # fancy fast way to split the string into a tuple of ints
        nl.append(transformCords(tuple(int(x) for x in point.split(",")))) # same as above but the coordinates to be drawn
        
    Triangle = Triangle(nl[0][0],nl[0][1],nl[1][0],nl[1][1],nl[2][0],nl[2][1], fill=0xFFFFFF) #passes in the transformed coordinates

    while len(screenGroup) > 0:
        screenGroup.pop()
    
    
    drawGrid()  
    screenGroup.append(Triangle)
    
    text = f"Area : {getArea(nl[0],nl[1],nl[2])} km^2" # Gets area of triangle and prints it.
    text_area = label.Label(terminalio.FONT, text = text , color=0xFFFF00, x=5, y=5)
    screenGroup.append(text_area)
    
    display.show(screenGroup)
    
    print(f"Area of the triangle is {getArea(nl[0],nl[1],nl[2])}") 
    #except Exception as e:
    # print(f"An error occurred: {e}")
    continue
        
