#extraData is a file used for user editable variables that may be edited but should otherwise remain as their defaults
#please don't edit these unless you know what your doing


class systemItem(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description


emptyItem = systemItem('None', 'There is nothing equipped')

armourSlots = ['Head', 'Shoulders', 'Torso', 'Hands', 'Legs', 'Feet']