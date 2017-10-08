class misc(object):
	playerMisc = []

	def __init__(self, name, description, value, count):
		self.name = name
		self.description = description
		self.value = value
		self.count = count
		if self.count > 1:
			self.playerMisc.append(self)


class weapon(object):
	playerWeapons = []

	def __init__(self, name, description, value, damage, count):
		self.name = name
		self.description = description
		self.value = value
		self.damage = damage
		self.count = count
		if self.count > 1:
			self.playerWeapons.append(self)


class armour(object):
	armourList = []

	def __init__(self, name, description, value, defence, count):
		self.armourList.append(self)
		self.name = name
		self.description = description
		self.value = value
		self.defence = defence
		self.count = count
