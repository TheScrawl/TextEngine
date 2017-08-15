from areaData import areaDict as areaData
import npcData
import menu

def move(area):
    print(area)
    print(area.get('name'))
    print(area.get('startText'))
    if area.get('npcList') != None:
        print('Area NPCs:')
        for npc in area.get('npcList'):
            print(npc.get('name')) 
    for areaNum in sorted(area.get('movement')):
        print(areaNum + ': ' + area.get('movement').get(str(areaNum)).get('id')))
    menu.areaMenu(area)
move(areaData.get('testAreaCentral'))
        
