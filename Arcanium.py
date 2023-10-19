from ProgramBasics import txt
import ProgramBasics as pb
import DisplayScreens as display
import RandomGeneration as generate

def playerTurn():
    choice = None
    first = True # Used to check for the first iteration
    while choice not in range(1,len(playerMoves)+1):
        if first is False: print("Invalid Choice, Pick Again")
        pb.slowPrint(30,"\nType the number of the move to attack with: ", end="")
        choice = int(input())
        first = False
    print(f"Valid Choice: {choice}")

def skip():
    '''Ask whether to skip the intro sequence'''
    skip = input(txt.italics+"Skip the intro? (Y/n): "+txt.end)
    if skip.lower() == "n":
        display.intro()
        pb.enter()

pb.clear()
enemyTypes = ("Boar","Dragon","Orc","Minotaur","Wolf","Vampire")
playerStats = {
    "health": 30,
    "dmg": 8,
    "armour": 2
}
playerMoves = {
    "Slash": 1.2,
    "Stab": 1.1
}
enemyStats, enemyMoves = generate.enemy(5,enemyTypes)
skip()
display.battle(playerStats,playerMoves,enemyStats,enemyMoves)
playerTurn()
