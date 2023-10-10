from ProgramBasics import txt
import ProgramBasics as pb
import random as dom

def genEnemy(lvl):
    global enemyTypes
    type = enemyTypes[dom.randint(0,len(enemyTypes)-1)]
    baseHealth, baseDmg, armour, expMult = genStats(type)
    health = lvl * 4 + baseHealth
    dmg = lvl * 0.75 + baseDmg
    exp = lvl * expMult
    stats = {
        "type": type,
        "health": health,
        "dmg": dmg,
        "armour": armour,
        "exp": exp
    }
    return stats

def genStats(enemyType):
    match enemyType.lower():
        case "boar":
            health = dom.randint(5,10)
            dmg = dom.randint(1,2)
            armour = 1
            exp = 5
        case "dragon":
            health = dom.randint(40,60)
            dmg = dom.randint(8,12)
            armour = 5
            exp = 5
        case "orc":
            health = dom.randint(10,15)
            dmg = dom.randint(2,4)
            armour = 2
            exp = 5
        case "alberto":
            health = dom.randint(30,40)
            dmg = dom.randint(4,6)
            armour = 3
            exp = 5
        case "alfredo":
            health = dom.randint(30,40)
            dmg = dom.randint(4,6)
            armour = 3
            exp = 5
        case "minotaur":
            health = dom.randint(20,30)
            dmg = dom.randint(3,5)
            armour = 2
            exp = 5
    return health, dmg, armour, exp

def showDisplay(player,enemy):
    print(txt.bold+"=== Enemy ( {} ) ===".format(enemy["type"]+txt.end), # Print Enemy Stats
          txt.bold+txt.italics+txt.faint+"\nHealth:"+txt.end, round(enemy["health"]), 
          txt.bold+txt.italics+txt.faint+"\nDamage:"+txt.end, round(enemy["dmg"]), 
          txt.bold+txt.italics+txt.faint+"\nArmour:"+txt.end, enemy["armour"], 
          txt.bold+txt.italics+txt.faint+"\nExp:"+txt.end, round(enemy["exp"]),

          txt.bold+"\n\n===== You ====="+txt.end, # Print Player Stats
          txt.bold+txt.italics+txt.faint+"\nHealth:"+txt.end, player["health"],
          txt.bold+txt.italics+txt.faint+"\nDamage:"+txt.end, player["dmg"],
          txt.bold+txt.italics+txt.faint+"\nArmour:"+txt.end, player["armour"]
          )

def intro():
    print('''Welcome to...\n
 █████╗ ██████╗  █████╗  █████╗ ███╗  ██╗██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ██║██║██╔══██╗
███████║██████╔╝██║  ╚═╝███████║██╔██╗██║██║███████║
██╔══██║██╔══██╗██║  ██╗██╔══██║██║╚████║██║██╔══██║
██║  ██║██║  ██║╚█████╔╝██║  ██║██║ ╚███║██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝
          ''')

pb.clear()

enemyTypes = ["Boar","Dragon","Orc","Alberto","Alfredo","Minotaur"]

intro()
playerStats = {
    "health": 30,
    "dmg": 8,
    "armour": 2
}
enemyStats = genEnemy(5)
showDisplay(playerStats,enemyStats)
