

import time # type: ignore
import board # type: ignore
import busio # type: ignore
import digitalio # type: ignore 

RedLED = digitalio.DigitalInOut(board.GP16)


for x in [RedLED]:
    x.direction = digitalio.Direction.OUTPUT
    
    

dotHash = {".": 0.25, "-": 0.75, " ": -.25, "/": -1.75} # type: ignore

MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", # type: ignore
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", # type: ignore
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", # type: ignore
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", # type: ignore
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", # type: ignore
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", # type: ignore
    "9": "----.", "0": "-----", ",": "--..--", ".": ".-.-.-", "?": "..--..", # type: ignore
    "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-", " ": "/"} # type: ignore



while True:
    msg = input("Enter a message to convert to morse code or -q to quit: ").upper() # get the message and make it uppercase because lower case is not in the hash.
    morseMsg =  ' '.join([MORSE_CODE[letter] + " " for letter in msg]) if msg != "-Q" else exit() # join a list of the letters translated to morse code to an empty string 
    
    for MorseValue in morseMsg:
        val = dotHash[MorseValue]
        
        if val> 0:
            RedLED.value = True
            time.sleep(dotHash[MorseValue])
            RedLED.value = False
            time.sleep(0.25)
        else:
            time.sleep(abs(val))
        