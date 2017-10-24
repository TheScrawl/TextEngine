#extraData is a file used for user editable variables that may be edited but should otherwise remain as their defaults
#please don't edit these unless you know what your doing


class systemItem(object):
	def __init__(self, name, description, attack, defence):
		self.name = name
		self.description = description
		self.attack = attack
		self.defence = defence


emptyItem = systemItem('None', 'There is nothing equipped', 0, 0)

armourSlots = ['Head', 'Shoulders', 'Torso', 'Hands', 'Legs', 'Feet']