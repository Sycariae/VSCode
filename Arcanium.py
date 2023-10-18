import random as dom
from ProgramBasics import txt
import ProgramBasics as pb

def genEnemy(lvl,types):
    '''Picks a random enemy type from a list and generates 
    a dictionary of enemy stats based on type and level'''
    eType = types[dom.randint(0,len(types)-1)]
    baseHealth, baseDmg, armour, expMult = genStats(eType)
    health = lvl * 4 + baseHealth
    dmg = lvl * 0.75 + baseDmg
    exp = lvl * expMult
    stats = {
        "type": eType,
        "health": health,
        "dmg": dmg,
        "armour": armour,
        "exp": exp
    }
    return stats

def genStats(enemyType):
    '''Generates basic stat values based on enemy type'''
    global enemyMoves # {moveName}: {dmgMultiplier}
    match enemyType.lower():
        case "boar":
            health = dom.randint(5,10)
            dmg = dom.randint(1,2)
            armour = 1
            exp = 5
            enemyMoves = {
                "Charge": 1.2,
                "Bite": 1
            }
        case "dragon":
            health = dom.randint(40,60)
            dmg = dom.randint(8,12)
            armour = 5
            exp = 5
            enemyMoves = {
                "Claws": 1,
                "Fire Breath": 1.35
            }
        case "orc":
            health = dom.randint(10,15)
            dmg = dom.randint(2,4)
            armour = 2
            exp = 5
            enemyMoves = {
                "Club": 1,
                "Body Slam": 1.2
            }
        case "minotaur":
            health = dom.randint(20,30)
            dmg = dom.randint(3,5)
            armour = 2
            exp = 5
            enemyMoves = {
                "Headbutt": 1.1,
                "Battleaxe": 1.2
            }
        case "wolf":
            health = dom.randint(10,15)
            dmg = dom.randint(4,6)
            armour = 2
            exp = 5
            enemyMoves = {
                "Claws": 1.1,
                "Bite": 1.2
            }
        case "vampire":
            health = dom.randint(15,20)
            dmg = dom.randint(4,6)
            armour = 2
            exp = 5
            enemyMoves = {
                "Bite": 1.2,
                "Bat Attack": 1
            }
    return health, dmg, armour, exp

def showBattle(pStats,pMoves,eStats,eMoves):
    '''Show stats of the enemy and player in a battle'''
    pb.slowPrint(3,'''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╦╝███████║   ██║      ██║   ██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██████╦╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝''')
    pb.sleep(250)
    pb.slowPrint(15,txt.bold+"\n\n=== Enemy ( {} ) ===".format(eStats["type"]+txt.end))
    printEntityInfo(eStats,eMoves)
    pb.slowPrint(15,"\n==================================")
    pb.slowPrint(15,txt.bold+"\n=== You ==="+txt.end)
    printEntityInfo(pStats,pMoves)

def printEntityInfo(stats,moves=None):
    for i in stats:
        pb.slowPrint(15,pb.capital(i)+":", stats[i])
    if moves is not None:
        pb.slowPrint(15,txt.italics+"\n=== Moves ==="+txt.end)
        for count, i in enumerate(moves):
            pb.slowPrint(10,f"{count+1}.", i, end="")
            pb.slowPrint(5,txt.fBotalics+f"( Damage Multiplier: {txt.end+str(moves[i])+txt.fBotalics})", txt.end)

def intro():
    pb.slowPrint(40,"Welcome to...")
    print()
    pb.slowPrint(3,'''
 █████╗ ██████╗  █████╗  █████╗ ███╗  ██╗██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ██║██║██╔══██╗
███████║██████╔╝██║  ╚═╝███████║██╔██╗██║██║███████║
██╔══██║██╔══██╗██║  ██╗██╔══██║██║╚████║██║██╔══██║
██║  ██║██║  ██║╚█████╔╝██║  ██║██║ ╚███║██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝\n''')

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
enemyMoves = {}
enemyStats = genEnemy(5,enemyTypes)
skip = input("Skip the intro? (Y/n): ")
if skip.lower() == "n":
    pb.clear()
    intro()
    pb.enter()
pb.clear()
showBattle(playerStats,playerMoves,enemyStats,enemyMoves)
