from areaData import areaDict as areaData
from npcData import npcDict as npcData
globalCurrentArea = None
def areaMenu(currentArea):
    global globalCurrentArea
    globalCurrentArea = currentArea
    import area
    import npc
    choice = str(input('> ')).lower()
    if ' ' in choice:
        (function, option) = choice.split(' ')
          
        if str(function) == 'go':
            if option in currentArea.get('movement'):
               area.move(areaData.get(currentArea.get('movement').get(option).get('id')))
           
            else:
                print('you cannot go that way')

        if str(function) == 'talk':
            if currentArea.get('npcList') is not None and option in currentArea.get('npcList'):
                npc.talk(npcData.get(currentArea.get('npcList').get(option)))  
            else:
                print('that person is not here')
                area.move(currentArea)
        else:
            print('Please enter a valid function (e.g go, talk)')
            area.move(currentArea)
    else:
        print('please enter two inputs')
        area.move(currentArea)
