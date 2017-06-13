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
#poop

import random

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

#PLAYER STATS
class player(object):
    def __init__(self, name, health, attack, defence, carryWeight, currentWeapon, currentHead, currentShoulders, currentChest, currentLegs, currentFeet, currentShield):

        self.name = 'cunt'
        self.health = 100
        self.attack = self.currentWeapon.attack

        self.defence = (
                    self.currentHead.defence +
                    self.currentShoulders.defence + 
                    self.currentChest.defence + 
                    self.currentLegs.defence + 
                    self.currentFeet.defence + 
                    self.currentShield.defence
                    )

        self.carryWeight = (
                    self.currentHead.carryWeight + 
                    self.currentShoulders.carryWeight +
                    self.currentChest.carryWeight + 
                    self.currentLegs.carryWeight + 
                    self.currentFeet.carryWeight + 
                    self.currentShield.carryWeight + 
                    self.currentWeapon.carryWeight
                    )

        self.currentWeapon = currentWeapon
        self.currentHead = currentHead
        self.currentShoulders = currentShoulders
        self.currentChest = currentChest
        self.currentLegs = currentLegs
        self.currentFeet = currentFeet
        self.currentShield = currentShield

#Enemies
class enemy(object):
    def __init__(self, ID, level, name, health, attack, defence, dropList):
        self.ID = ID
        self.level = level
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.dropList = dropList

#DROPLISTS
droplistWolf = {
    'wolfPelt': {    
        'count': 1,
        'chance': 70,
        },
    }

droplistSlime = {
    'slimeBall': {
        'count': random.randint(1, 10),
        'chance': 100,
        },
    }




#ID Layout: letter : type, first 2 numbers:level, second 2 numbers:creature number

#                #ID        level   Name        Health    Attack    Defence     droplists
enemyWolf =  enemy('e1001', 1,      'Wolf',     5,        5,        5,          droplistWolf)
enemySlime = enemy('e1002', 1,      'Slime',    3,        2,        7,          droplistSlime)

#Items
class weapon(object):
    registry = [] 

    def __init__(self, ID, name, weaponType, attack, block, weight, buyValue, sellValue, count):
        self.registry.append(self)
        self.ID = ID
        self.name = name
        self.weaponType = weaponType
        self.attack = attack
        self.block = block
        self.weight = weight
        self.buyValue = buyValue
        self.sellValue = sellValue
        self.count = count

#ID SYSTEM: first letter : item type,   next 2 numbers : set number,    last 2 numbers : item number

                        #ID        Name                 Type            Attack      Block   Weight  buyValue    sellValue   count 
rustyKnife =      weapon('w1001', 'Rusty Knife',        'oneHand',      1,          1,      1,      10,         5,          1)
rustySword =      weapon('w1002', 'Rusty Sword',        'oneHand',      2,          2,      3,      15,         10,         0)
rustyBow =        weapon('w1003', 'Rusty Bow',          'ranged',       2,          1,      2,      15,         10,         0)
rustyHammer =     weapon('w1004', 'Rusty Warhammer',    'twoHand',      5,          1,      6,      20,         10,         0)
rustyBatAxe =     weapon('w1005', 'Rusty Battle Axe',   'twoHand',      3,          1,      4,      15,         10,         0)

class armour(object):
    registry = []

    def __init__(self, ID, name, armourType, armourPiece, defence, weight, buyValue, sellValue, count):
        self.registry.append(self)
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
clothHat =            armour('a1001',  'Cloth Hat',             'light',    'head',         0,        1,       5,         2,          1)
clothShirt =          armour('a1002',  'Cloth Shirt',           'light',    'chest',        1,        2,       7,         3,          1)
clothTrousers =       armour('a1003',  'Cloth Trousers',        'light',    'legs',         1,        2,       5,         2,          1)
leatherSandals =      armour('a1004',  'Leather Sandals',       'light',    'feet',         0,        1,       3,         1,          1)
#Medium
leatherHelmet =       armour('a2001',  'Leather Helmet',        'medium',   'head',         3,        2,      10,         5,          0)
leatherShoulders =    armour('a2002',  'Leather Shoulderpads',  'medium',   'shoulders',     2,        2,      10,         5,          0)
leatherChestplate =   armour('a2003',  'Leather Chestplate',    'medium',   'chest',        5,        4,      20,         10,         0)
leatherGreaves =      armour('a2004',  'Leather Greaves',       'medium',   'legs',         2,        2,      10,         5,          0)
leatherGloves =       armour('a2005',  'Leather Gloves',        'medium',   'hands',        1,        1,      5,          2,          0)
leatherBoots =        armour('a2006',  'Leather Boots',         'medium',   'feet',         5,        1,      5,          2,          0)
leatherShield =       armour('a2007',  'Leather Shield',        'medium',   'shield',       5,        4,      20,         10,         0)
#Heavy
steelHelmet =         armour('a3001',  'Steel Helmet',          'heavy',    'head',         5,        4,      15,         10,         0)
steelShoulders =      armour('a3002',  'Steel Shoulderpads',    'heavy',    'shoulders',     4,        4,      15,         10,         0)
steelChestplate =     armour('a3003',  'Steel Chestplate',      'heavy',    'chest',        10,       8,      25,         15,         0)
steelGreaves =        armour('a3004',  'Steel Greaves',         'heavy',    'legs',         3,        4,      15,         10,         0)
steelGloves =         armour('a3005',  'Steel Gloves',          'heavy',    'hands',        2,        2,      10,         5,          0)
steelBoots =          armour('a3006',  'Steel Boots',           'heavy',    'feet',         2,        2,      10,         5,          0)
steelShield =         armour('a3007',  'Steel Shield',          'heavy',    'shield',       10,       8,      25,         15,         0)
#Shops
#Quests

def talkNPC(npc):

#talkNPC Todo List
#more functions including giveItem, openShop and more
#could probably use a bit of tiding up and optimising but eh it was a pain to get it this far and it works as it is.

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
        if function == 'go' or 'move':
            if value in area.get('areaMoves'):
                moveArea(eval(value))
    else:
        print('error: please enter two values')
    
def manageInventory():
    print('')
    print('~ Inventory ~ ')
    print('')
    print('Armour:')
    for item in armour.registry:
        try:
            if (item.count >= 1 
                and item.ID != 
                player.currentHead 
                or player.currentShoulders 
                or player.currentChest 
                or player.currentLegs 
                or player.currentFeet 
                or player.currentShield):
                print(item.name)
        except AttributeError:
                if item.count >=1:
                    print(item.name)
    print('')
    print('Weapons:')
    for item in weapon.registry:
        try:
            if item.count >= 1 and item.ID != player.currentWeapon:
                print(item.name)
            if item.count >= 1 and item.ID == player.currentWeapon:
                print(item.name + ' (Equipped)')
        except AttributeError:
            if item.count >=1:
                print(item.name)
    print('')
    print('What would you like to do?')
    print('A: Equip weapon')
    print('B: Equip armour')
    print('C: Inspect Items')
    print('D: Drop Items')
    print('E: Exit Menu')
    playerChoice = input(str.lower('> '))
    if playerChoice == 'a':
        num = 1
        print('What weapon would you like to equip?')
        for item in weapon.registry:
            try:
                if item.count >= 1:
                    if item.ID != player.currentWeapon:
                        print(str(num) + ': ' +  item.name)
                    if item.ID == player.currentWeapon:
                        print(str(num) + ': ' + item.name + ' (Equipped)')
                    num = num + 1

            except AttributeError:
                if item.count >= 1:
                    print(str(num) + ': ' + item.name)
                    num = num + 1
        playerChoice = input('> ')
        try: 
            int(playerChoice)
        except ValueError:
            print('please input a number')
            manageInventory()
        num = 0
        for item in weapon.registry:
            num  = num + 1
            try:
                if str(num) == playerChoice and item.ID !=  player.currentWeapon:
                    player.currentWeapon = item.ID
                    print('You have equipped ' + item.name)
                    manageInventory()
                if item.ID == player.currentWeapon:
                    print('You already have ' + item.name + ' equipped')
                    manageInventory()
            except AttributeError:
                if str(num) == playerChoice:
                    player.currentWeapon = item.ID
                    print('You have equipped ' +  item.name)
                    manageInventory()

    if playerChoice == 'b':
        num = 1
        print('What armour would you like to equip?')
        for item in armour.registry:
            try:
                if item.count >= 1:
                    if (item.ID != 
                            player.currentHead
                            or player.currentShoulders
                            or player.currentChest
                            or player.currentLegs
                            or player.currentFeet
                            or player.currentShield):
                        print(str(num) + ': ' +  item.name)
                    if (item.ID ==  
                            player.currentHead
                            or player.currentShoulders
                            or player.currentChest
                            or player.currentLegs
                            or player.currentFeet
                            or player.currentShield):
                        print(str(num) + ': ' + item.name + ' (Equipped to ' + item.armourPiece)
                    num = num + 1

            except AttributeError:
                if item.count >= 1:
                    print(str(num) + ': ' + item.name)
                    num = num + 1
        playerChoice = input('> ')
        try: 
            int(playerChoice)
        except ValueError:
            print('please input a number')
            manageInventory()
        num = 0
       for item in armour.registry:
            num = num + 1
            if num == int(playerChoice):
                if item.armourPiece == 'head':
                    try:
                        if item.ID == player.currentHead:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()   
                    except AttributeError:
                        player.currentHead = item.ID
                        manageInventory()
                if item.armourPiece == 'shoulders':
                    try:
                        if item.ID == player.currentShoulders:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()
                    except AttributeError:
                        player.currentShoulders = item.ID
                        manageInventory()
                if item.armourPiece == 'chest':
                    try:
                        if item.ID == player.currentChest:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()
                    except AttributeError:
                        player.currentChest= item.ID
                        manageInventory()
                if item.armourPiece == 'legs':
                    try:
                        if item.ID == player.currentLegs:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()
                    except AttributeError:
                        player.currentLegs = item.ID
                        manageInventory()
                if item.armourPiece == 'feet':
                    try:
                        if item.ID == player.currentFeet:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()
                    except AttributeError:
                        player.currentFeet = item.ID
                        manageInventory()
                if item.armourPiece == 'sheild':
                    try:
                        if item.ID == player.currentSheild:
                            print('You already have ' + item.name + ' equipped')
                            manageInventory()
                        else:
                            player.currentHead = item.ID
                            manageInventory()
                    except AttributeError:
                        player.currentShield = item.ID
                        manageInventory()

manageInventory()
#moveArea(testAreaC)
#talkNPC(testNPC)

#Attempt at python rpg for Text-Engine base Version Alpha 0.0.3
