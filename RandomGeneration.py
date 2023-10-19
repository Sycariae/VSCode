import random as dom

def enemy(lvl,types):
    '''Randomly generates an enemy from the inputs'''
    eType = types[dom.randint(0,len(types)-1)]
    baseHealth, baseDmg, armour, expMult, moves = genStats(eType)
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
    return stats, moves

def genStats(eType):
    '''Generates basic stat values based on enemy type'''
    match eType.lower():
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
    return health, dmg, armour, exp, enemyMoves
