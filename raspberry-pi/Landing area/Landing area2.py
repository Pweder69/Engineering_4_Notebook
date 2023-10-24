from adafruit_display_text import label #type: ignore
import adafruit_displayio_ssd1306 #type: ignore
import board # type: ignore
import digitalio # type: ignore
import math
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address= 0x3d ,reset=board.GP10)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    
