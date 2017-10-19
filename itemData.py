from item import armour
from item import weapon
from item import misc

#Testing ItemsS
testItem = misc('test item', 'its a test item', 69, 10)
testItem2 = misc('test item 2', 'its a test item as well', 69, 10)
testWeapon = weapon('test sword', 'its a test weapon', 'sword', 45, 13, 1)
testWeapon2 = weapon('test spear', 'its a test weapon as well', 'spear', 45, 13, 1)
testHelmet = armour('test helmet', 'its test armour', 'head', 420, 11, 2)
testBoots = armour('test boots', 'its test armour as well', 'feet', 420, 11, 2)

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
    'sword',
    4,
    None,
    0)

# Misc
spoon = misc('Spoon', 'its just a spoon', 0, 0)
fork = misc('Fork', 'its just a fork', 0, 0)
teddyBear = misc('TeddyBear', 'Its a teddy bear, his name is george', 1000, 0)