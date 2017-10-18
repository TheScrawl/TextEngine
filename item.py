import player


class misc(object):
	def __init__(self, name, description, value, count):
		self.name = name
		self.description = description
		self.value = value
		self.count = count
		if self.count > 0:
			player.miscList.append(self)


class weapon(object):
	def __init__(self, name, description, weaponType, value, damage, count):
		self.name = name
		self.description = description
		self.weaponType = weaponType
		self.value = value
		self.damage = damage
		self.count = count
		if self.count > 0:
			player.weaponList.append(self)


class armour(object):
	def __init__(self, name, description, slot, value, defence, count):
		self.name = name
		self.description = description
		self.slot = slot
		self.value = value
		self.defence = defence
		self.count = count
		if self.count > 0:
			player.armourList.append(self)
