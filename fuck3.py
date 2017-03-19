#Attempt at python rpg for Text-Engine base Version Alpha 0.0.3
#This code is for a testing phase of what will eventually become TextEngine

#immediate todos list:
#Location dataset and functions
#combat and enemies
#shops
#items and inventory
#quest system

#Later todos list (after other crap is done):
#get the textfile to dataset functionality working
#write tutorials and guides and whatnot
#make sample game

#want to list (some may never happen):
#maps
#more comfy UI
#Ascii art
#graphical text-engine editor


##DATASETS##

#NPCs
testNPC = {
    'npcName': 'Test Npc',
    'startText': 'This is the startText',

    'a': {
        'optionHeader': 'Option A',
        'optionText': 'this is option A',
            
        'a': {
            'optionHeader': 'Option AA',
            'optionText': 'this is option AA',
                    
            'functions': {
                'exitTalk': True,
                    },
            },

        'b': {
            'optionHeader': 'Option AB',
            'optionText': 'this is option AB',
                    
            'functions': {
                'exitTalk': True,
                    },
            },

        },

    'b': {
        'optionHeader': 'Option B',
        'optionText': 'this is option B',
            
        'functions': {
            'exitTalk': True,
                },
        },
}
#Locations
testAreaC = {
        
        'areaName': 'Test Area Central',
        'areaText': 'This is Area Central text',
        
         #NPCs
        'areaNPCs': {
            'a': 'testNPC', 
        },
        
        #Movements
        'areaMoves': { 
            'a': 'testAreaN',
            'b': 'testAreaS',
            'c': 'testAreaE',
            'd': 'testAreaW',
            }
        
        #Items and Chests
        #Enemies
}


#Enemies
#Items
class weapon(object):
    def __init__(self, ID, name, weaponType, attack, block, weight, buyValue, sellValue, count)
        self.ID = ID
        self.name = name
        self.weaponType = weaponType
        self.attack = attack
        self.block = block
        self.weight = weight
        self.buyValue = buyValue
        self.sellValue
        self.count = count

#ID SYSTEM: first letter : item type,   next 2 numbers : set number,    last 2 numbers : item number

                        #ID        Name                 Type            Attack      Block   Weight  buyValue    sellValue   count 
rustyKnife =      weapon('w1001', 'Rusty Knife',        'oneHand',      1,          1,      1,      10,         5,          0)
rustySword =      weapon('w1002', 'Rusty Sword',        'oneHand',      2,          2,      3,      15,         10,         0)
rustyBow =        weapon('w1003', 'Rusty Bow',          'ranged',       2,          1,      2,      15,         10,         0)
rustyHammer =     weapon('w1004', 'Rusty Warhammer',    'twoHand',      5,          1,      6,      20,         10,         0)
rustyBatAxe =     weapon('w1005', 'Rusty Battle Axe',   'twoHand',      3,          1,      4,      15,         10,         0)

class armour(object):
    def __init__(self, ID, name, armourType, armourPiece, defence, weight, buyValue, sellValue, count)
        self.ID = ID
        self.name = name
        self.armourType = armourType
        self.armourPiece = armourPiece
        self.defence = defence
        self.weight = weight
        self.buyValue = buyValue
        self.sellValue = sellValue
        self.count = count

#ID SYSTEM: first letter : item type,   next 2 numbers : set number,    last 2 numbers : item number
                            #ID        Name                     Type        Piece           Defence   Weight  buyValue    sellValue   count
#Light
clothHat =            armour('a1001',  'Cloth Hat',             'light',    'head',         0,        1,       5,         2,          0)
clothShirt =          armour('a1002',
#Medium
leatherHelmet =       armour('a2001',  'Leather Helmet',        'medium',   'head',         3,        2,      10,         5,          0)
leatherShoulders =    armour('a2002',  'Leather Shoulderpads',  'medium',   'shoulder',     2,        2,      10,         5,          0)
leatherChestplate =   armour('a2003',  'Leather Chestplate',    'medium',   'chest',        5,        4,      20,         10,         0)
leatherGreaves =      armour('a2004',  'Leather Greaves',       'medium',   'legs',         2,        2,      10,         5,          0)
leatherGloves =       armour('a2005',  'Leather Gloves',        'medium',   'hands',        1,        1,      5,          2,          0)
leatherBoots =        armour('a2006',  'Leather Boots',         'medium',   'feet',         1,        1,      5,          2,          0)
leatherShield =       armour('a2007',  'Leather Shield',        'medium',   'shield',       5,        4,      20,         10,         0)
#Heavy
steelHelmet =         armour('a3001',  'Steel Helmet',          'heavy',    'head',         5,        4,      15,         10,         0)
steelShoulders =      armour('a3002',  'Steel Shoulderpads',    'heavy',    'shoulder',     4,        4,      15,         10,         0)
steelChestplate =     armour('a3003',  'Steel Chestplate',      'heavy',    'chest',        10,       8,      25,         15,         0)
steelGreaves =        armour('a3004',  'Steel Greaves',         'heavy',    'legs',         3,        4,      15,         10,         0)
steelGloves =         armour('a3005',  'Steel Gloves',          'heavy',    'hands',        2,        2,      10,         5,          0)
steelBoots =          armour('a3006',  'Steel Boots',           'heavy',    'feet',         2,        2,      10,         5,          0)
steelShield =         armour('a3007',  'Steel Shield',          'heavy',    'shield',       10,       8,      25,         15,         0)
#
#Shops
#Quests


def talkNPC(npc):

#talkNPC Todo List
#more functions including giveItem, openShop and more
#could probably use a bit of tyding up and optimising but eh it was a pain to get it this far and it works as it is.

#Print Start info.
    print('~' + npc.get('npcName'))
    print('')
    print(npc.get('startText'))
    print('')

#Print out options into formatted list
    for key in sorted(npc.keys()):
        if len(key) <= 1:
            print(key + ': ' + npc.get(key).get('optionHeader'))


#Define and Start Choice Sequence    
    def talkCont(option):
        print('')
        print(option.get('optionText'))
        print('')

        #print out options
        for key in sorted(option.keys()):
            if len(key) <= 1:
                print(key + ': ' + option.get(key).get('optionHeader'))
        
        #start choice 
        choice = input(str('> ')).lower()
        
        if 'functions' in option.keys():
            if 'exitTalk' in option.get('functions'):
                if option.get('functions').get('exitTalk') == True:
                    return
            
        if choice in option and len(choice) <= 1:
            choice = option.get(choice)
            talkCont(choice)

        else:
            print('Invalid input')
            talkCont(option)

#Back to main part
    choice = input(str('> ')).lower()

    if 'functions' in npc.keys():
        if 'exitTalk' in npc.get('functions'):
            if npc.get('functions').get('exitTalk') == True:
                return

    if choice in npc and len(choice) <= 1:
        choice = npc.get(choice)
        talkCont(choice)
   
    else:
        print('Invalid Input')
        talkNPC(npc)


def moveArea(area):
    print('')
    print(area.get('areaName'))
    print('')
    print(area.get('areaText'))
    print('')
    print('NPCs:')
    for key, value in sorted(area.get('areaNPCs').items()):
        print(key + ': ' + value)
    print('')
    print('Movements:')
    for key, value in sorted(area.get('areaMoves').items()):
        print(key + ': ' + value)

    choice = input(str('> '))
    if ' ' in choice:
        (function, value) = choice.split().lower()
        if function = 'go' or 'move':
            if value in area.get('areaMoves'):
                moveArea(eval(value))
    else:
        print('error: please enter two values')
    


moveArea(testAreaC)
#talkNPC(testNPC)
