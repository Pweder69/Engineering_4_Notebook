import board # type: ignore
import time
import digitalio # type: ignore


RedLED = digitalio.DigitalInOut(board.GP19)
BlueLED = digitalio.DigitalInOut(board.GP13)
Button = digitalio.DigitalInOut(board.GP20)

Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP



for x in [RedLED, BlueLED]:
    x.direction = digitalio.Direction.OUTPUT
    
    
oldval = True


def delayCheck(waitTime):
    global Button,oldval

    
    # print(Button.value, oldval) #DEBUG
    time1 = time.time()
    
    # operates like a sleep but checks for button press and aborts if pressed
    
    
    while time.time() - time1 < waitTime:
        if Button.value == False and oldval:
            print("Aborted")
            RedLED.value = False
            BlueLED.value = False
            # if pressed recursivly call countdown to start the loop in the loop
            countdown()
            
        oldval = Button.value
    
    
    
def countdown():
    global RedLED, BlueLED, Button,oldval
    
    while True:
        time.sleep(.01)
        if Button.value == False:
            # print(Button.value, oldval) #DEBUG
            oldval = Button.value
            
            
            for x in range(5):

                RedLED.value = True
                delayCheck(.25)
                RedLED.value = False
                delayCheck(.25)
            
            #
            #DOESNT MATTER For recusion
            #    
            
            BlueLED.value = True
            time.sleep(2.5)
            BlueLED.value = False

countdown()


  