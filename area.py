import areaData
import npcData

def move(area):
    print(area.get('name'))
    print(area.get('startText'))
    print('')

    if area.get('npcList') != None:
        print('Area NPCs:')
        for npc in area.get('npcList'):
            print(npc.get('name') + '\n') 
    for areaNum in sorted(area.get('movement')):
        print(areaNum + ': ' + area.get('movement').get(areaNum).get('id'))
  
move(areaData.testAreaCentral)
        
