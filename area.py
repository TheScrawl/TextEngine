from areaData import areaDict as areaData
from npcData import npcDict as npcData
from menu import areaMenu
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def move(area):
    print('')
    print(color.BOLD + area.get('name') + color.END)
    print(area.get('startText'))
    if area.get('npcList') != None:
        print('')
        print(color.BOLD + 'Area NPCs:' + color.END)
        for key, value in sorted(area.get('npcList').items()):
            print(key + ': ' + npcData.get(value).get('name'))
        print('')
    print(color.BOLD + 'Movement Options' + color.END)
    for key, value in sorted(area.get('movement').items()):
        print(key + ': ' + value.get('optionText'))
    areaMenu(area)

if __name__ == '__main__':
    move(areaData.get('testAreaCentral'))
        
