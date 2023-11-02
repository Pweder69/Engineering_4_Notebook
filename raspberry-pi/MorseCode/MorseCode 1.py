MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ': "  "} 

while True:
    msg = input("Enter a message to convert to morse code or -q to quit: ").upper() # get the message and make it uppercase because lower case is not in the hash.
    print( ' '.join([MORSE_CODE[letter] for letter in msg])) if msg != "-Q" else exit() # join a list of the letters translated to morse code to an empty string 
                                                                                        # if msg is -q exit the program
    # ik its sucks that its in 1 line but i like it that way