# coding: utf-8

import items
import player

shop_items = [items.greaterPot, items.lesserPot, items.sog]

def vendor():

	print """
	Olá!
	Seja bem-vindo à loja dos três lados.
	O que você quer fazer?

	1. Comprar
	2. Vender
	3. Sair
	"""

	choice = raw_input("> ")

	if choice == "1":
		buy()
	elif choice == "2":
		sell()
	elif choice == "3":
		return
	else: 
		print "\t*** Escolha um dos números do menu ***\n"
		vendor()

def buy():

	buy_items = ""
	count = 1
	for item in shop_items:
		buy_items += "%d. %s, Preço: %dG\n" % (count, item.name, item.price)
		count += 1

	print "Seu ouro: %dG" % player.pl.gold
	print "Aqui estão os itens que nós temos:\n\n%s%d. Voltar" % (buy_items, count)
	

	index = raw_input("> ")
	if index.isdigit() == False:
		print "\t*** Escolha um dos números do menu ***\n"
		buy()

		
	index = int(index) - 1
	if index != len(shop_items) and index < len(shop_items):
		item_bought = shop_items[index]
		if player.pl.gold >= item_bought.price:
			player.pl.gold -= item_bought.price
			print "Você comprou %s por %d de ouro!\n" % (item_bought.name, item_bought.price)
			if isinstance(item_bought, items.Weapon):
				player.pl.inventory.addWeapon(item_bought)
				buy()
			elif isinstance(item_bought, items.Armor):
				player.pl.inventory.addArmor(item_bought)
				buy()
			elif isinstance(item_bought, items.Potion):
				player.pl.inventory.addPotion(item_bought) 
				buy()
		else:
			print "\t*** Você não tem ouro suficiente para comprar esse item ***\n"
			buy()
	else:
		vendor()

def sell():
	weapons = ""
	armors = ""
	potions = ""
	loop_counter = 0

	for weapon in player.pl.inventory.allWeapons:
		count = player.pl.inventory.allWeapons.count(weapon)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		weapons += "- %s x%d\n" % (weapon.name, count)
		if loop_counter == 0:
			loop_counter = count - 1
			
	for armor in player.pl.inventory.allArmors:
		count = player.pl.inventory.allArmors.count(armor)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		armors += "- %s x%d\n" % (armor.name, count)
		if loop_counter == 0:
			loop_counter = count - 1
			
	for potion in player.pl.inventory.allPotions:
		count = player.pl.inventory.allPotions.count(potion)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		potions += "- %s x%d\n" % (potion.name, count)
		if loop_counter == 0:
			loop_counter = count - 1

	print "Seu ouro: %dG" % player.pl.gold
	print "1. Weapons:\n", weapons
	print "2. Armors:\n", armors
	print "3. Potions:\n", potions
	print "4. Voltar\n"

	choice = raw_input("> ")

	if choice == "1":
		show_weapons()
	elif choice == "2":
		show_armors()
	elif choice == "3":
		show_potions()
	elif choice == "4":
		vendor()
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		sell()

def show_weapons():

	arrayWeapons = player.pl.inventory.allWeapons
	unique_items = []
	loop_counter = 0
	result = ""
	count = 1
	
	if len(arrayWeapons) != 0:
		for weapon in arrayWeapons:
			item_count = arrayWeapons.count(weapon)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(weapon)
			result += "%d. %s x%d, Preço: %dG\n%s\n\n" % (count, weapon.name, item_count, weapon.price / 2, weapon.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Seu ouro: %dG" % player.pl.gold
		print "Weapons:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a arma que quer vender."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayWeapons.index(item)
			weapon = arrayWeapons.pop(index)
			print "\t*** Você vendeu %s por %d de ouro! ***\n" % (item.name, item.price / 2)
			player.pl.gold += weapon.price / 2
			show_weapons()
		elif choice == len(unique_items):
			sell()
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			show_weapons()
	else:		
		print "\t*** Você não tem mais armas para vender ***\n"		
		sell()

def show_armors():

	arrayArmors = player.pl.inventory.allArmors
	unique_items = []
	loop_counter = 0
	result = ""
	count = 1
	
	if len(arrayArmors) != 0:
		for armor in arrayArmors:
			item_count = arrayArmors.count(armor)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(armor)
			result += "%d. %s x%d, Preço: %dG\n%s\n\n" % (count, armor.name, item_count, armor.price / 2, armor.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Seu ouro: %dG" % player.pl.gold
		print "Armors:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a armadura que quer vender."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayArmors.index(item)
			armor = arrayArmors.pop(index)
			print "\t*** Você vendeu %s por %d de ouro! ***\n" % (item.name, item.price / 2)
			player.pl.gold += armor.price / 2
			show_armors()
		elif choice == len(unique_items):
			sell()
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			show_armors()
	else:		
		print "\t*** Você não tem mais armaduras para vender ***\n"		
		sell()

def show_potions():

	arrayPotions = player.pl.inventory.allPotions
	unique_items = []
	loop_counter = 0
	result = ""
	count = 1
	
	if len(arrayPotions) != 0:
		for potion in arrayPotions:
			item_count = arrayPotions.count(potion)
			if loop_counter > 0:
				loop_counter -= 1
				continue
			unique_items.append(potion)
			result += "%d. %s x%d, Preço: %dG\n%s\n\n" % (count, potion.name, item_count, potion.price / 2, potion.info)
			count += 1
			if loop_counter == 0:
				loop_counter = item_count - 1

		print "Seu ouro: %dG" % player.pl.gold
		print "Poções:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a poção que quer vender."
		choice = raw_input("> ")
		if choice.isdigit():
			choice = int(choice) - 1
		if choice < len(unique_items) and choice >= 0:
			item = unique_items[choice]
			index = arrayPotions.index(item)
			potion = arrayPotions.pop(index)
			print "\t*** Você vendeu %s por %d de ouro! ***\n" % (item.name, item.price / 2)
			player.pl.gold += potion.price / 2
			show_potions()
		elif choice == len(unique_items):
			sell()
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			show_potions()
	else:		
		print "\t*** Você não tem mais poções para vender ***\n"		
		sell()

