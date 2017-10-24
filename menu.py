from areaData import areaDict as areaData
from npcData import npcDict as npcData
import itemData
import player
import TablePrint
import extraData

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
				(choiceFunction, choiceOption) = choice.split(' ')

				if str(choiceFunction) == 'go':
						if choiceOption in currentArea.get('movement'):
								area.move(areaData.get(currentArea.get('movement').get(choiceOption).get('id')))

						else:
								print('you cannot go that way')

				if str(choiceFunction) == 'talk':
						if currentArea.get('npcList') is not None and choiceOption in currentArea.get('npcList'):
								npc.talk(npcData.get(currentArea.get('npcList').get(choiceOption)))
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
	print('2: Equip or Unequip Items')	#TODO
	print('3: Drop Items')	#TODO
	print('4: Exit')	#TODO

	choice = str(input('> '))
	if choice == '1':

		print('\nItems:')
		itemList = []
		for misc in player.miscList:
			itemList.append([misc.name, misc.description, misc.value, misc.count])
		TablePrint.table(['Name', 'Description', 'Value', 'Count'], *itemList)

		print('\nWeapons:')
		weaponList = []
		for weapon in player.weaponList:
			weaponList.append([weapon.name, weapon.description, weapon.weaponType, str(weapon.value), str(weapon.damage), str(weapon.count)])
		TablePrint.table(['Name', 'Description', 'Type', 'Value', 'Damage', 'Count'], *weaponList)

		print('\nArmour:')
		armourList = []
		for armour in player.armourList:
			armourList.append([armour.name, armour.description, armour.slot, str(armour.value), str(armour.defence), str(armour.count)])
		TablePrint.table(['Name', 'Description', 'slot', 'Value', 'Defence', 'Count'], *armourList)

		print('\nCurrently Equipped')
		TablePrint.table(
			['Head', 'Shoulders', 'Torso', 'Hands', 'Legs', 'Feet', 'Weapon'],
			[
				player.equippedArmourHead.name,
				player.equippedArmourShoulders.name,
				player.equippedArmourTorso.name,
				player.equippedArmourHands.name,
				player.equippedArmourLegs.name,
				player.equippedArmourFeet.name,
				*player.equippedWeapons,
			]
			)

		inventory()

	if choice == '2':
		print('What type of item would you like to equip/unequip')
		print('1: Armour')
		print('2: Weapons')
		print('3: Other')

		typeChoice = str(input('> '))
		if typeChoice == '1':
			print('Current Loadout: ')
			counter = 0
			for slot in extraData.armourSlots:
				counter = counter + 1
				print(str(counter) + ': ' + slot)
			print('Which slot would you like to change item?')
			slotChoice = str(input('> '))
			counter = 0
			for item in player.armourList:
				if item.slot.lower() == extraData.armourSlots[int(slotChoice) - 1].lower():
					counter = counter + 1
					print(str(counter) + ': ' + item.name)
			if counter == 0:
				print('You dont have any items for that slot')
				inventory()

			itemChoice = str(input('> '))
			counter = 0
			for item in player.armourList:
				counter = counter + 1
				if str(counter) == itemChoice and item.slot.lower() == extraData.armourSlots[int(slotChoice) - 1].lower():
					if slotChoice == '1':
						player.equippedArmourHead = item
					if slotChoice == '2':
						player.equippedArmourShoulders = item
					if slotChoice == '3':
						player.equippedArmourTorso = item
					if slotChoice == '4':
						player.equippedArmourHands = item
					if slotChoice == '5':
						player.equippedArmourLegs = item
					if slotChoice == '6':
						player.equippedArmourFeet = item

					player.defenceStat = (
						player.equippedArmourHead.defence +
						player.equippedArmourShoulders.defence +
						player.equippedArmourTorso.defence +
						player.equippedArmourHands.defence +
						player.equippedArmourLegs.defence +
						player.equippedArmourFeet.defence)
					print('You equipped ' + player.equippedArmourHead.name)

					slotChoice = None
					itemChoice = None
					counter = None
				inventory()

if __name__ == '__main__':
	inventory()
