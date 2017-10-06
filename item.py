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
        self.count = count

        
class armour(object):
    def __init__(self, name, description, value, defence, count):
        self.name = name
        self.description = description
        self.value = value
        self.defence = defence
        self.count = count