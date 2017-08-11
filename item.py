class item(object):
    def __init__(self, name, description, value, count):
        self.name = name
        self.description = description
        self.value = value
        self.count = count

class weapon(item):
    def __init__(self, name, description, value, damage, count):
        super(weapon, self).__init__(name, description, value, count)
        self.damage = damage
        

        
class armour(item):
    def __init__(self, name, description, value, defence, count):
        super(weapon, self).__init__(name, description, value, count)
        self.defence = defence

