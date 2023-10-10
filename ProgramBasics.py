import os
import time

class txt:                  # To add text markdown. Example:  print( txt.red + txt.bold + "text" + txt.end )
    bold = '\033[1m'        # This would produce "text" written in red and weighted in bold.
    italics = '\x1B[3m'
    end = '\033[0m'
    underline = '\033[4m'
    purple = '\033[95m'
    cyan = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    faint = "\033[2m"

def sleep(milleseconds):
    time.sleep(milleseconds / 1000)

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'") 

def egg():                                 # For sake of adding easter eggs into programs
    print(txt.yellow+txt.bold+''' 
Congratulations! You've found an...
  ______          _            ______            
 |  ____|        | |          |  ____|           
 | |__   __ _ ___| |_ ___ _ __| |__   __ _  __ _ 
 |  __| / _` / __| __/ _ \ '__|  __| / _` |/ _` |
 | |___| (_| \__ \ ||  __/ |  | |___| (_| | (_| |
 |______\__,_|___/\__\___|_|  |______\__, |\__, |
                                      __/ | __/ |
                                     |___/ |___/ '''+txt.end)

def next():
    print("\nPress",  "Enter", "to continue...")
    input()

def exit():
    print("\nPress",  "Enter", "to exit...")
    input()