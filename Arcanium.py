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
    return health, dmg, armour, exp

def showBattle(player,pMoves,enemy,eMoves):
    '''Show stats of the enemy and player in a battle'''
    pb.slowPrint('''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╦╝███████║   ██║      ██║   ██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██████╦╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝''',4)
    print("\n")
    pb.sleep(250)
    print(txt.bold+"=== Enemy ( {} ) ===".format(enemy["type"]+txt.end))
    for i in enemy:
        print(pb.capital(i)+":", enemy[i],1)
    '''print(txt.bold+"=== Enemy ( {} ) ===".format(enemy["type"]+txt.end), # Print Enemy Stats
          txt.bold+txt.italics+txt.faint+"\nHealth:"+txt.end, round(enemy["health"],1),
          txt.bold+txt.italics+txt.faint+"\nDamage:"+txt.end, round(enemy["dmg"],1),
          txt.bold+txt.italics+txt.faint+"\nArmour:"+txt.end, enemy["armour"],
          txt.bold+txt.italics+txt.faint+"\nExp:"+txt.end, round(enemy["exp"],1),
          "\n\n"+
          txt.bold+"===== You ====="+txt.end, # Print Player Stats
          txt.bold+txt.italics+txt.faint+"\nHealth:"+txt.end, round(player["health"],1),
          txt.bold+txt.italics+txt.faint+"\nDamage:"+txt.end, round(player["dmg"],1),
          txt.bold+txt.italics+txt.faint+"\nArmour:"+txt.end, round(player["armour"],1),"\n"
         )'''
    pMultis = pMoves["dmgMultis"]
    pMoves = pMoves["moves"]
    i = len(pMoves)-1
    total = i
    print(txt.bold+"=== Move List ==="+txt.end)
    while i != -1:
        print(str(len(pMoves)-i)+".", txt.bold+txt.italics, pMoves[total-i], txt.faint+"( Damage Multiplier:"+txt.end, txt.bold+txt.italics, pMultis[total-i], txt.faint+")"+txt.end)
        i -= 1

def intro():
    pb.slowPrint("Welcome to...")
    print()
    pb.slowPrint('''
 █████╗ ██████╗  █████╗  █████╗ ███╗  ██╗██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ██║██║██╔══██╗
███████║██████╔╝██║  ╚═╝███████║██╔██╗██║██║███████║
██╔══██║██╔══██╗██║  ██╗██╔══██║██║╚████║██║██╔══██║
██║  ██║██║  ██║╚█████╔╝██║  ██║██║ ╚███║██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝\n''',4)

pb.clear()
enemyTypes = ("Boar","Dragon","Orc","Minotaur","Wolf")
playerStats = {
    "health": 30,
    "dmg": 8,
    "armour": 2
}
playerMoves = {
    "moves": ["Slash","Stab"],
    "dmgMultis": [1.2,1.1]
}
enemyMoves = {}
enemyStats = genEnemy(5,enemyTypes)
intro()
pb.enter(1,True)
pb.clear()
showBattle(playerStats,playerMoves,enemyStats,enemyMoves)
