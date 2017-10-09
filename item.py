class misc(object):
	playerList = []

	def __init__(self, name, description, value, count):
		self.name = name
		self.description = description
		self.value = value
		self.count = count
		if self.count > 0:
			self.playerList.append(self)


class weapon(object):
	playerList = []

	def __init__(self, name, description, value, damage, count):
		self.name = name
		self.description = description
		self.value = value
		self.damage = damage
		self.count = count
		if self.count > 0:
			self.playerList.append(self)


class armour(object):
	playerList = []

	def __init__(self, name, description, value, defence, count):
		self.name = name
		self.description = description
		self.value = value
		self.defence = defence
		self.count = count
		if self.count > 0:
			self.playerList.append(self)

