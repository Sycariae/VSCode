import os
import time

class txt:
    #def __init__(self,text):
    #    self.text = text
    end = '\033[0m'         # To add text markdown. Example:  print( txt.red + txt.bold + "text" + txt.end )
    bold = '\033[1m'          # This would produce "text" written in red and weighted in bold.
    italics = '\x1B[3m'
    underline = '\033[4m'
    purple = '\033[95m'
    cyan = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    faint = '\033[2m'
    botalics = '\033[1m \x1B[3m' # Bold + Italics
    fBotalics = '\033[1m \x1B[3m \033[2m' # Faint + Bold + Italics

def sleep(milleseconds):
    time.sleep(milleseconds / 1000)

def clear():
    try: os.system('cls' if os.name == 'nt' else "printf '\033c'")
    except: pass

def egg():                                 # For sake of adding easter eggs into programs
    print(txt.yellow+txt.bold+'''
Congratulations! You've found an...

███████╗ █████╗  ██████╗████████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
█████╗  ███████║╚█████╗    ██║   █████╗  ██████╔╝
██╔══╝  ██╔══██║ ╚═══██╗   ██║   ██╔══╝  ██╔══██╗
███████╗██║  ██║██████╔╝   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    ███████╗ ██████╗  ██████╗ 
    ██╔════╝██╔════╝ ██╔════╝ 
    █████╗  ██║  ██╗ ██║  ██╗ 
    ██╔══╝  ██║  ╚██╗██║  ╚██╗
    ███████╗╚██████╔╝╚██████╔╝
    ╚══════╝ ╚═════╝  ╚═════╝ '''+txt.end)

def checkForKey(search,dictionary):
    '''Searches a dictionary to check if it contains a value with a specific key

    checkForKey({search},{dictionary})
    '''
    if search in dictionary:
        keyFound = True
    else:
        keyFound = False
    return keyFound

def capital(text):
    firstChar = True
    output = ""
    for char in text:
        if firstChar is True: output = output + char.upper()
        else: output = output + char
        firstChar = False
    return output
   
def slowPrint(*args, **kwargs):
    '''Prints a list of arguments, character by character with a 
    customisable ms delay between each character

    {delay} is optional and defaults to 40 if the first argument is not numeric.

    {kwarg} is optional and can be used to take the following input: end=""
    which will make the next print statement type from where it left off.

    slowPrint(delay,arg1,arg2,arg3...kwarg)
    '''
    for i, arg in enumerate(args):
        if i == 0:
            if isinstance(arg,int): 
                delay = arg
                continue
            else: delay = 40
        arg = str(arg)
        for char in arg:
            print(char, end='', flush=True)
            sleep(delay)
    if checkForKey("end",kwargs) is False:
        print()

def enter(option=1):
    '''Prints an ' Press ENTER to proceed/exit...' prompt.

    CALL: enter() OR enter(1) = OUTPUT: Press ENTER to proceed...
    CALL: enter(2) = OUTPUT: Press ENTER to exit...
    '''
    enterText = txt.bold+"ENTER"+txt.end
    match option:
        case 1:
            print(f"\nPress {enterText} to proceed...")
        case 2:
            print(f"\nPress {enterText} to exit...")
    input()
