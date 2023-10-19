from ProgramBasics import txt
import ProgramBasics as pb
import DisplayScreens as display
import RandomGeneration as generate

def playerTurn():
    pb.slowPrint("\nType the number of the move to attack with: ", end="")
    choice = input()
    while isinstance(choice,int) and choice in range(playerMoves):
        pb.slowPrint("\nType the number of the move to attack with: ", end="")
        choice = input()

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