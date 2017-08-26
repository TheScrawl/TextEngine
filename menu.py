from areaData import areaDict as areaData

def areaMenu(currentArea):
    import area
    choice = str(input('> ')).lower()
    if ' ' in choice:
        (function, option) = choice.split(' ')
          
        if str(function) == 'go':
            if option in currentArea.get('movement'):
               area.move(areaData.get(currentArea.get('movement').get(option).get('id')))
            
            else:
                print('please enter a vaid option')
                area.move(currentArea)
        else:
            print('Please enter a valid function (e.g go, talk)')
            area.move(currentArea)
    else:
        print('please enter two inputs')
        area.move(currentArea)
