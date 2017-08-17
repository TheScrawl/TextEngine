import area
from areaData import areaDict as areaData

def areaMenu(currentArea):
    choice = str(input('> ')).lower()
    if ' ' in choice:
        (function, option) = choice.split(' ')
          
        if str(function) == 'go':
            if option in currentArea.get('movement'):
               area.move(areaData.get(currentArea.get('movement').get(option).get('id')))

    else:
        print('please enter two inputs')
