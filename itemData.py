from item import armour
from item import weapon
from item import misc

#System Items
#These items are important for the game to run properly, please do not remove them
#emptyArmour = armour('None', 'There is nothing equipped', 0, 0, 0)
#emptyWeapon = weapon('None', 'There is nothing equipped', 0, 0, 0)

#Testing Items
testItem = misc('test item', 'its a test item', 69, 10)
testItem2 = misc('test item 2', 'its a test item as well', 69, 10)
testWeapon = weapon('test weapon', 'its a test weapon', 45, 13, 1)
testWeapon2 = weapon('test weapon 2', 'its a test weapon as well', 45, 13, 1)
testArmour = armour('test armour', 'its test armour', 420, 11, 2)
testArmour2 = armour('test armour 2 ', 'its test armour as well', 420, 11, 2)

# Currencies
copper = misc('Copper', 'A small copper coin', 1, 0)
silver = misc('Silver', 'A small silver coin', 10, 0)
gold = misc('Gold', 'A small gold coin', 100, 0)
emerald = misc('Emerald', 'A small shiny green gem', 1000, 0)

# Quest Items
shibbledibble = misc('Shibbledibble', 'Its shibbledibble, its used for a quest', 'notforsale', 0)

magicSwordOfDoomAndDestruction = weapon(    # Example of item that is too long
    'Magic Sword of Doom and Destruction',
    'Its the magic sword of doom and destruction, its very important',
    4,
    None,
    0)

# Misc
spoon = misc('Spoon', 'its just a spoon', 0, 0)
fork = misc('Fork', 'its just a fork', 0, 0)
teddyBear = misc('TeddyBear', 'Its a teddy bear, his name is george', 1000, 0)