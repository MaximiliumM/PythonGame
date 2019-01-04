# coding: utf-8

import random
import player
import rooms
import items
import monsters
import battle
import shop
import console
			
itemSelector = []

def search(hasItem):
	
	if hasItem == True:
		if getRandomItem() != True:
			print "\t*** Você não encontrou nada ***\n"
	else:
		print "\t*** Você não encontrou nada ***\n"
		
def getRandomItem():

	got_item = bool

	x = random.randint(0, 10000)

	allItems = items.allItems

	if x == 1:
		player.pl_inventory.addWeapon(items.cheaterSword)
	elif x > 1 and x <= 6: 
		for item in allItems:
			if item.percentage == 0.05:
				itemSelector.append(item)
			addItem()
			got_item = True
	elif x > 6 and x <= 16:
		for item in allItems:
			if item.percentage == 0.10:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 16 and x <= 36:
		for item in allItems:
			if item.percentage == 0.20:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 36 and x <= 86:
		for item in allItems:
			if item.percentage == 0.50:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 86 and x <= 186:
		for item in allItems:
			if item.percentage == 1.00:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 186 and x <= 686:
		for item in allItems:
			if item.percentage == 5.00:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 686 and x <= 1686:
		for item in allItems:
			if item.percentage == 10.0:
				itemSelector.append(item)
		addItem()
		got_item = True
	elif x > 1686 and x <= 3186:
		for item in allItems:
			if item.percentage == 15.0:
				itemSelector.append(item)
		addItem()
		got_item = True
	else:
		got_item = False

	for i in range(len(itemSelector)):
		itemSelector.pop()

	return got_item

def addItem():

	item_toAdd = random.choice(itemSelector)
	if isinstance(item_toAdd, items.Weapon):
		player.pl_inventory.addWeapon(item_toAdd)
	elif isinstance(item_toAdd, items.Armor):
		player.pl_inventory.addArmor(item_toAdd)
	elif isinstance(item_toAdd, items.Potion):
		player.pl_inventory.addPotion(item_toAdd) 
	print "Você pegou: %s" % item_toAdd.name

def showStatus():
	spells = ""

	for spell in player.pl.class_spells:
		spells += "- %s\n" % spell.name

	print "** Classe **"
	print "%s Lvl: %d\n" % (player.pl.theclass, player.pl.level)
	print "** Status **"
	print "HP: %d | Mana: %d | EXP: %d / %d" % (player.pl.hp, player.pl.mana, player.pl.exp, player.pl.exp_needed) 
	print "\n** Atributos **"
	print "Força: %d | %d" % (player.pl.strBase, player.pl.strMod)
	print "Vitalidade: %d | %d" % (player.pl.vitBase, player.pl.vitMod)
	print "Inteligência: %d | %d" % (player.pl.intBase, player.pl.intMod)
	print "Destreza: %d | %d\n" % (player.pl.dexBase, player.pl.dexMod)
	print "** Magias **"
	print spells

def showInventory():
	weapons = ""
	if len(player.pl_inventory.allWeapons) == 0:
		weapons = "* Nenhum *\n"
		
	armors = ""
	if len(player.pl_inventory.allArmors) == 0:
		armors = "* Nenhum *\n"
	
	potions = ""	
	if len(player.pl_inventory.allPotions) == 0:
		potions = "* Nenhum *\n"
		
	questItems = ""
	if len(player.pl_inventory.questItems) == 0:
		questItems = "* Nenhum *\n"
		
	equipped = "- %s\n- %s\n" % (player.pl_inventory.currentWeapon.name,
							   player.pl_inventory.currentArmor.name)
	loop_counter = 0
	
	for weapon in player.pl_inventory.allWeapons:
		count = player.pl_inventory.allWeapons.count(weapon)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		weapons += "- %s x%d\n" % (weapon.name, count)
		if loop_counter == 0:
			loop_counter = count - 1

	for armor in player.pl_inventory.allArmors:
		count = player.pl_inventory.allArmors.count(armor)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		armors += "- %s x%d\n" % (armor.name, count)
		if loop_counter == 0:
			loop_counter = count - 1
			
	for potion in player.pl_inventory.allPotions:
		count = player.pl_inventory.allPotions.count(potion)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		potions += "- %s x%d\n" % (potion.name, count)
		if loop_counter == 0:
			loop_counter = count - 1

	for questItem in player.pl_inventory.questItems:
		questItems += "- %s\n" % (questItem.name)

	print "Equipados:\n", equipped
	print "Weapons:\n", weapons
	print "Armors:\n", armors
	print "Potions:\n", potions
	print "Quest Items:\n", questItems
	menuChoices = """O que você quer fazer?
1. Equipar Weapons
2. Equipar Armors
3. Usar Potions
4. Voltar

> """

	equip(raw_input(menuChoices))


def equip(menu_choice):

	arrayWeapons = player.pl_inventory.allWeapons
	arrayArmors = player.pl_inventory.allArmors
	arrayPotions = player.pl_inventory.allPotions
	result = ""
	count = 1
	loop_counter = 0
	unique_items = []

	if menu_choice == "1":
		for weapon in arrayWeapons:
			item_count = arrayWeapons.count(weapon)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(weapon)
			result += "%d. %s x%d\n%s\n\n" % (count, weapon.name, item_count, weapon.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Weapons:\n", result
		print "Escolha a arma que quer equipar."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayWeapons.index(item)
			arrayWeapons[index].equip()
			print "\t*** Você equipou %s ***\n" % arrayWeapons[index].name
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			equip(menu_choice)
	elif menu_choice == "2":
		for armor in arrayArmors:
			item_count = arrayArmors.count(armor)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(armor)
			result += "%d. %s x%d\n%s\n\n" % (count, armor.name, item_count, armor.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Armors:\n", result
		print "Escolha a armadura que quer equipar."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayArmors.index(item)
			arrayArmors[index].equip()
			print "\t*** Você equipou %s ***\n" % arrayArmors[index].name
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			equip(menu_choice)
	elif menu_choice == "3":
		for potion in arrayPotions:
			item_count = arrayPotions.count(potion)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(potion)
			result += "%d. %s x%d\n%s\n\n" % (count, potion.name, item_count, potion.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Potions:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a poção que quer usar."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayPotions.index(item)
			potion = arrayPotions.pop(index)
			potion.use()
		elif choice == len(unique_items):
			showInventory()
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			equip(menu_choice)
	elif menu_choice == "4":
		return
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		showInventory()


def menu(room):
			menuChoices = """\t*** %s ***
O que você quer fazer?
1. Vasculhar a sala
2. Mostrar inventário
3. Minhas informações
4. Andar

> """ % room.name

			choice = raw_input(menuChoices)	

			if choice == "1":
				search(room.hasTreasure)
				room.hasTreasure = False
				return menu(room)
			elif choice == "2":
				showInventory()
				return menu(room)
			elif choice == "3":
				showStatus()
				return menu(room)
			elif choice == "4":
				#shop.vendor()
				return room.walk()
			else:
				print "\t*** Escolha um dos números do menu ***\n"
				return menu(room)	
