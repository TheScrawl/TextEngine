class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Armour(Item):
    def __init__(self, name, description, value, defence):
        self.defence = defence
        super().__init__(name, description, value)

    def __str__(self):
        return "{}=====\n{}\nValue: {}\nDefence: {}".format(self.name, self.description, self.value, self.defence)
