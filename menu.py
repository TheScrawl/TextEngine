from areaData import areaDict as areaData
from npcData import npcDict as npcData
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
           
        if str(function) == 'talk':
            if currentArea.get('npcList') != None and option in currentArea.get('npcList'):
                npc.talk(npcData.get(currentArea.get('npcList').get(option)))  
            else:
                print('please enter a vaid option')
                area.move(currentArea)
        else:
            print('Please enter a valid function (e.g go, talk)')
            area.move(currentArea)
    else:
        print('please enter two inputs')
        area.move(currentArea)
