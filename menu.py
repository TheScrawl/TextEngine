import area
from areaData import areaDict as areaData

def areaMenu(currentArea):
    choice = str(input('> ')).lower()
    if ' ' in choice:
        (function, value) = choice.split(' ')
          
        if str(function) == 'go':
            if value in sorted(currentArea.get('movement')):
                fuckshit = str(currentArea.get('movement').get(str(value)).get('id'))
                area.move(areaData.get(fuckshit))

    else:
        print('please enter two inputs')
