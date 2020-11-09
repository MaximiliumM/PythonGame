# coding: utf-8

from party import pl_party
from items import itemManager
import random
import rooms
import items
import monsters
import shop
import console
			
def search(hasItem):
	
	if hasItem == True:
		if getRandomItem() != True:
			print "\t*** Você não encontrou nada ***\n"
	else:
		print "\t*** Você não encontrou nada ***\n"
		
def getRandomItem():
		
	item = itemManager.getRandomItem()
	
	if item != None:
		pl_party.inventory.addItem(item)
		print "Você pegou: %s" % item.name
		return True
	else:
		return False

def showStatus():
	count = 1
	members = ""

	for member in pl_party.members:
		members += "%d. %s\n" % (count, member.name)
		count += 1
		
		print "-- %s --" % member.name
		print "** Classe **"
		print "%s Lvl: %d\n" % (member.theclass, member.level)
		print "** Status **"
		print "HP: %d | Mana: %d | EXP: %d / %d\n\n" % (member.hp, member.mana, member.exp, member.exp_needed) 
	
	print "Escolha um personagem para ver mais detalhes."
	print "%s%d. Voltar\n" % (members, count)	
	
	choice = raw_input("> ")
	if choice.isdigit():
		choice = int(choice) - 1
	if choice < len(pl_party.members) and choice >= 0:
		showMemberStatus(pl_party.members[choice])
	elif choice == len(pl_party.members):
			return
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		showStatus()
	
def showMemberStatus(member):
	spells = ""

	for spell in member.class_spells:
		spells += "- %s\n%s\n\n" % (spell.name, spell.description)
		
	print "\n** Equipamento **"
	print "- %s" % member.inventory.currentWeapon.name
	print member.inventory.currentWeapon.info
	print "- %s" % member.inventory.currentArmor.name	
	print member.inventory.currentArmor.info

	print "\n** Atributos **"
	print "Força: %d | %d" % (member.strBase, member.strMod)
	print "Vitalidade: %d | %d" % (member.vitBase, member.vitMod)
	print "Inteligência: %d | %d" % (member.intBase, member.intMod)
	print "Destreza: %d | %d\n" % (member.dexBase, member.dexMod)
	print "** Magias **"
	print spells

def showInventory():
	weapons = ""
	if len(pl_party.inventory.allWeapons) == 0:
		weapons = "* Nenhum *\n"
		
	armors = ""
	if len(pl_party.inventory.allArmors) == 0:
		armors = "* Nenhum *\n"
	
	potions = ""	
	if len(pl_party.inventory.allPotions) == 0:
		potions = "* Nenhum *\n"
		
	questItems = ""
	if len(pl_party.inventory.questItems) == 0:
		questItems = "* Nenhum *\n"
							   
	loop_counter = 0
	
	for weapon in pl_party.inventory.allWeapons:
		count = pl_party.inventory.allWeapons.count(weapon)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		weapons += "- %s x%d\n" % (weapon.name, count)
		if loop_counter == 0:
			loop_counter = count - 1

	for armor in pl_party.inventory.allArmors:
		count = pl_party.inventory.allArmors.count(armor)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		armors += "- %s x%d\n" % (armor.name, count)
		if loop_counter == 0:
			loop_counter = count - 1
			
	for potion in pl_party.inventory.allPotions:
		count = pl_party.inventory.allPotions.count(potion)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		potions += "- %s x%d\n" % (potion.name, count)
		if loop_counter == 0:
			loop_counter = count - 1

	for questItem in pl_party.inventory.questItems:
		questItems += "- %s\n" % (questItem.name)

	print "Weapons:\n", weapons
	print "Armors:\n", armors
	print "Potions:\n", potions
	print "Quest Items:\n", questItems
	menuChoice = raw_input("""O que você quer fazer?
1. Equipar Weapons
2. Equipar Armors
3. Usar Potions
4. Voltar

> """)

	if menuChoice == "4":
		return
	elif menuChoice == "1" or menuChoice == "2" or menuChoice == "3":
		showMemberInventory(menuChoice)
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		showInventory()

def showMemberInventory(menuChoice):
	
	members = ""
	count = 1
	
	for member in pl_party.members:		
		if menuChoice == "1":
			arrayEquips = pl_party.inventory.allWeapons
			equipped = "- %s\n" % member.inventory.currentWeapon.name
		elif menuChoice == "2":
			arrayEquips = pl_party.inventory.allArmors
			equipped = "- %s\n" % member.inventory.currentArmor.name
		
		detail = ""
		if menuChoice != "3":
			print "*** %s ***" % member.name
			print "Equipado:\n", equipped
		else:
			detail = ", HP: %d/%d" % (member.hp, member.maxHP)
		
		members += "%d. %s%s\n" % (count, member.name, detail)
		count += 1
			
	if menuChoice == "3":
		arrayEquips = pl_party.inventory.allPotions
		
	print "Escolha quem vai usar."
	print "%s%d. Voltar\n" % (members, count)
	
	choice = raw_input("> ")
	if choice.isdigit():
		choice = int(choice) - 1
	if choice < len(pl_party.members) and choice >= 0:
		chosenMember = pl_party.members[choice]
		equip(menuChoice, chosenMember, arrayEquips)
	elif choice == len(pl_party.members):
		showInventory()
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		showMemberInventory(menuChoice)

def equip(menu_choice, member, arrayEquips):
	result = ""
	count = 1
	loop_counter = 0
	unique_items = []
	
	if len(arrayEquips) == 0:
		print "\t*** Nenhum item desta categoria ***\n"
		showInventory()
	
	for equipment in arrayEquips:
		item_count = arrayEquips.count(equipment)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		unique_items.append(equipment)
		result += "%d. %s x%d\n%s\n\n" % (count, equipment.name, item_count, equipment.info)
		count += 1
		if loop_counter == 0:
			loop_counter = item_count - 1
	
	print "-- %s's Inventory --\n" % member.name
	
	if menu_choice == "1":
		currentEquip = member.inventory.currentWeapon
		print "Equipado:\n- %s\n" % currentEquip.name
		print "Weapons:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a arma que quer equipar."
	elif menu_choice == "2":
		currentEquip = member.inventory.currentArmor
		print "Equipado:\n- %s\n" % currentEquip.name
		print "Armors:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a armadura que quer equipar."
	elif menu_choice == "3":
		print "HP: %d, Mana: %d\n" % (member.hp, member.mana)
		print "Potions:\n"
		print "%s%d. Voltar\n" % (result, count)
		print "Escolha a poção que quer usar."

	choice = raw_input("> ")
	if choice.isdigit():
		choice = int(choice) - 1
	if choice < len(unique_items) and choice >= 0:
		item = unique_items[choice]
		index = arrayEquips.index(item)
		
		if menu_choice == "3":
			potion = arrayPotions.pop(index)
			potion.use(member)
		else:
			print "\t*** %s equipou %s ***\n" % (member.name, arrayEquips[index].name)
			equipment = arrayEquips.pop(index)
			member.inventory.equip(equipment)
			pl_party.inventory.addItem(currentEquip)
	elif choice == len(unique_items):
			showInventory()
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		equip(menu_choice, member, arrayEquips)


def menu(room):
			menuChoices = """\t*** %s ***
O que você quer fazer?
1. Vasculhar a sala
2. Inventário
3. Informações da Party
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
