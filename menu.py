import area
import areaData

def areaMenu(currentArea):
    choice = str(input('> ')).lower()
    if ' ' in choice:
        (function, value) = choice.split(' ')
        
        if function == 'go':
            for i in currentArea:
                if value in currentArea.get('movement'):
                    area.move(currentArea.get('movement').get(value).get('id'))

    else:
        print('please enter two inputs')
