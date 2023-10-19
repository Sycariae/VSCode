from ProgramBasics import txt
import ProgramBasics as pb

def battle(pStats,pMoves,eStats,eMoves):
    '''Show stats of the enemy and player in a battle'''
    pb.clear()
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
    pb.clear()
    pb.slowPrint(40,"Welcome to...")
    print()
    pb.slowPrint(3,'''
 █████╗ ██████╗  █████╗  █████╗ ███╗  ██╗██╗ █████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ██║██║██╔══██╗
███████║██████╔╝██║  ╚═╝███████║██╔██╗██║██║███████║
██╔══██║██╔══██╗██║  ██╗██╔══██║██║╚████║██║██╔══██║
██║  ██║██║  ██║╚█████╔╝██║  ██║██║ ╚███║██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝\n''')