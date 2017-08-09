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

#########################################################################################################################

class Goldcoin(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(
            name = "Gold coin",
            description = "A small round coin with {} engraved on the front.".format(str(self.amt)),
            value = self.amt
        )

class RustyDagger(Weapon):
    def __init__(self):
        super().__init__(
            name = "Rusty Dagger",
            description = "A once well kept dagger, left to rust.",
            value = 2
            damage = 5

            
