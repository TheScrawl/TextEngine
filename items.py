class item(object):
    def __init__(self, name, description, value, count):
        self.name = name
        self.description = description
        self.value = value
        self.count = count

class weapon(object):
    def __init__(self, name, description, value, damage, count):
        self.name = name
        self.description = description
        self.value = value
        self.damage = damage
        self.count = 0

        
class armour(object):
    def __init__(self, name, description, value, defence, count):
        self.name = name
        self.description = description
        self.value = value
        self.defence = defence
        self.count = 0

#ITEMLISTS (these should be moved to a new file in future, itemData.py or something)
        
#Currencies
gold = item('Gold', 'A small gold coin', 1, 0)

#Quest Items
shibbledibble = item('Shibbledibble', 'Its shibbledibble, used for a quest', 900000, 0)

#Weapons
rustyDagger = weapon('Rusty Dagger', 'its a small rusty dagger', 1, 5, 0)

#Armour
rustyHelmet = armour('Rusty Helmet', 'its a rusty helmet', 1, 5, 0)
