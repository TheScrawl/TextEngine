from areaData import areaDict as areaData
import npcData
import menu

def move(area):
    print(area.get('name'))
    print(area.get('startText'))
    if area.get('npcList') != None:
        print('Area NPCs:')
        for npc in area.get('npcList'):
            print(npc.get('name')) 
    for key, value in sorted(area.get('movement').items()):
        print(key + ': ' + value.get('optionText'))
    menu.areaMenu(area)
move(areaData.get('testAreaCentral'))
        
