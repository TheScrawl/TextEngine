import npcData
import area
import menu

def talk(npc):
    if npc.get('name') != None:
        print(npc.get('name')) 
    print(npc.get('startText'))

    try:
        if 'exit' in npc.get('functions'): #catch exit function and quit talk
            print('exiting dialogue')
            area.move(menu.globalCurrentArea) 
        else:
            pass
    except TypeError:
        pass    
    for option in sorted(npc.keys()):
        if option != 'name' and option != 'startText' and option != 'functions' and option != 'optionText':
            print(option + ': ' + npc.get(option).get('optionText'))
        
    choice = str(input('> ')).lower()
    
    npc = npc.get(choice)
    talk(npc)

