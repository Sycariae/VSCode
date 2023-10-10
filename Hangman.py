# version 0.4-beta

import ProgramBasics as pb
from ProgramBasics import txt

def completeCheck():
    global currentWord
    global complete
    correct = True
    for i in currentWord:
        if i == "_":
            correct = False
    if correct == True:
        complete = True

def listToString(list):
    text = ""
    count = len(list)
    for i in list:
        text = text + list[len(list)-count]
        count -= 1
    return text

def usedCheck(letter):
    used = False
    global usedLetters
    for i in usedLetters:
        if i == letter:
            used = True
    return used

def spaceOut(input):
    output = ""
    for i in input:
        output = output + " " + i
    return output

pb.clear()
complete = False
blank = ""
word = input("Enter a word to be guessed: ").upper()
pb.clear()

for i in word:
    blank = blank + " _"

currentWord = blank.split()
wordLength = len(word)
letterCorrect = False
usedLetters = []

print(spaceOut(listToString(currentWord)))
while complete == False:
    guess = input("\nGuess a letter of the word: ").upper()
    if len(guess) == 1:
        if usedCheck(guess) == False:
            count = wordLength
            for i in word:
                if guess == i:
                    print(txt.green + txt.bold + "\nYou got a letter!\n" + txt.end)
                    a = wordLength - count
                    currentWord[a] = i
                    letterCorrect = True
                count -= 1
            if letterCorrect == False:
                print(txt.red + txt.bold + "\nYou did not guess a letter...\n" + txt.end)
            completeCheck()
            if complete == False:
                print(spaceOut(listToString(currentWord)))
            else:
                print(txt.bold + "Correct Word: " + txt.end, txt.green + txt.bold + spaceOut(listToString(currentWord)) + txt.end)
        else:
            print(txt.red + txt.bold + "\nOI! You already used that letter mate!" + txt.end)
        usedLetters.append(guess)
    elif guess == "EGG":
        pb.egg()
    else:
        print(txt.red + txt.bold + "(!) INVALID INPUT\n(!) Input should only be 1 character in length" + txt.end)
        pass
    letterCorrect = False

print(txt.green + txt.bold + '''
   _____                            _       _     
  / ____|                          | |     | |    
 | |     ___  _ __   __ _ _ __ __ _| |_ ___| |    
 | |    / _ \| '_ \ / _` | '__/ _` | __/ __| |    
 | |___| (_) | | | | (_| | | | (_| | |_\__ \_|    
  \_____\___/|_| |_|\__, |_|  \__,_|\__|___(_)    
      __     __      __/ |_          __         _ 
      \ \   / /     |___/\ \        / /        | |
       \ \_/ /__  _   _   \ \  /\  / /__  _ __ | |
        \   / _ \| | | |   \ \/  \/ / _ \| '_ \| |
         | | (_) | |_| |    \  /\  / (_) | | | |_|
         |_|\___/ \__,_|     \/  \/ \___/|_| |_(_)\n''' + txt.end)

pb.exit()