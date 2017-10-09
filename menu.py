from areaData import areaDict as areaData
from npcData import npcDict as npcData
import itemData as i


class SetColor:
		PURPLE = '\033[95m'
		CYAN = '\033[96m'
		DARKCYAN = '\033[36m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		END = '\033[0m'


globalCurrentArea = None


def areaMenu(currentArea):
		global globalCurrentArea
		globalCurrentArea = currentArea
		import area
		import npc
		choice = str(input('> ')).lower()
		if ' ' in choice:
				(function, option) = choice.split(' ')

				if str(function) == 'go':
						if option in currentArea.get('movement'):
								area.move(areaData.get(currentArea.get('movement').get(option).get('id')))

						else:
								print('you cannot go that way')

				if str(function) == 'talk':
						if currentArea.get('npcList') is not None and option in currentArea.get('npcList'):
								npc.talk(npcData.get(currentArea.get('npcList').get(option)))
						else:
								print('that person is not here')
								area.move(currentArea)
				else:
						print('Please enter a valid function (e.g go, talk)')
						area.move(currentArea)
		else:
				print('please enter two inputs')
				area.move(currentArea)


def inventory():
		print(SetColor.BOLD + 'Inventory' + SetColor.END)
		print('Options:')
		print('1: View Items')
		print('2: Equip or Unequip Items') #TODO
		print('3: Drop Items') #TODO
		print('4: Exit') #TODO

		print(i.weapon.playerList)
		print(i.misc.playerList)
		choice = str(input('> '))
		if choice == '1':

				print('Items:')
				for misc in i.misc.playerList:
					print(misc.name + ' | ' + misc.description + ' | ' + str(misc.value) + ' | ' + str(misc.count))

				print('\nWeapons:')
				for weapon in i.weapon.playerList:
					print(weapon.name + ' | ' + weapon.description + ' | ' + str(weapon.value) + ' | ' + str(weapon.damage) + ' | ' + str(weapon.count))

				print('\nArmour:')
				for armour in i.armour.playerList:
					print(armour.name + ' | ' + armour.description + ' | ' + str(armour.value) + ' | ' + str(armour.defence) + ' | ' + str(armour.count))
			inventory()
