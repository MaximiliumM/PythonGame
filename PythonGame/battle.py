# coding: utf-8

import player
import monsters
import menu

turn = 0
turn_check = object
buff = object
spell_buff = False

def attack(monster):

	global spell_buff
	global turn
	global turn_check
	global buff

	while monster.hp > 0 and player.pl.hp > 0:
		print "\t*** Batalha ***\n"
		print "HP: %d/%d" % (player.pl.hp, player.pl.maxHP)
		print "Mana: %d/%d\n" % (player.pl.mana, player.pl.maxMana)
		print "1. Atacar"
		print "2. Usar Magia"
		print "3. Usar Poção\n"

		if spell_buff == True and turn_check != "back":
			turn += 1
			if turn > buff.turns:
				buff.debuff()
				turn = 0
				spell_buff = False

		turn_check = object

		choice = raw_input("> ")
		if choice == "1":
			hit = checkHit(player.pl, monster) 
			if hit == "Critical":
				print "Dano Crítico!"
				dmg = player.pl.attkDamage() * player.pl.crit
				monster.hp -= dmg
				print "Você deu %d de dano!\n" % dmg
			elif hit == True:
				dmg = player.pl.attkDamage()				
				monster.hp -= dmg
				print "Você deu %d de dano!\n" % dmg
			else:
				print "Você errou!\n"
		elif choice == "2":
				spell = chooseSpell()
				if spell != "back":
					if spell.turns > 1:	
						spell_buff = True
						buff = spell
					cast = spell.use(monster)
					if cast == False:
						attack(monster)
				else:
					turn_check = "back"
					attack(monster)
		elif choice == "3":
			if len(player.pl_inventory.allPotions) != 0:	
				potion = choosePotion()
				if potion != "back":
					potion.use()
				else:
					turn_check = "back"
					attack(monster)
			else:
				print "\t*** Você não tem mais poções! ***\n"
				attack(monster)
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			attack(monster)

		# --- Monster Turn ---
		
		if monster.hp > 0:

			print "\t*** Turno do Inimigo ***\n"
			hit = checkHit(monster, player.pl)
			if hit == "Critical":
				print "Dano Crítico!"
				dmg = monster.attkDamage() * 2
				player.pl.hp -= dmg
				print "Você levou %d de dano!\n" % dmg
			elif hit == True:
				dmg = monster.attkDamage()
				player.pl.hp -= dmg
				print "Você levou %d de dano!\n" % dmg
			else:
				print "%s errou!\n" % monster.name

def endBattle(monster):
	if player.pl.hp <= 0:
		print "Você morreu! Fim de jogo."
	elif monster.hp <= 0:
		player.pl.exp += monster.exp
		print "Você ganhou %d de experiência!" % monster.exp 
		player.pl.check_lvlUp()

		if monster.drops != "quest":
			got_item = bool
			for i in range(monster.drops):
				if menu.getRandomItem():
					got_item = True
				else:
					if got_item != True:
						got_item = False

			if got_item == False:
				print "\n\t*** O monstro não deu nada ***\n"
		else:
			player.pl_inventory.addQuestItem(monster.getQuestItem())

def checkHit(attacker, defender):
	attk = attacker.hitOrMiss()
	def_ac = defender.ac
	if attk == "Fumble":
		return False
	elif attk == "Critical":
		return "Critical"
	elif attk > def_ac:
		return True
	else:
		return False

def chooseSpell():
	spells = ""
	count = 1

	for spell in player.pl.class_spells:
		spells += "%d. %s, %dMP\n" % (count, spell.name, spell.manaCost)
		count += 1

	print "%s%d. Voltar\n" % (spells, count)
	print "Escolha qual magia você quer usar.\n"

	choice = raw_input("> ")
	if choice.isdigit():
		choice = int(choice) - 1
	if choice < len(player.pl.class_spells) and choice >= 0:
		return player.pl.class_spells[choice]
	elif choice == len(player.pl.class_spells):
		return "back"
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		return chooseSpell()

def choosePotion():
	potions = ""
	count = 1
	loop_counter = 0
	unique_items = []

	for potion in player.pl_inventory.allPotions:
		item_count = player.pl_inventory.allPotions.count(potion)
		if loop_counter > 0:
			loop_counter -= 1
			continue
		unique_items.append(potion)
		potions += "%d. %s x%d\n" % (count, potion.name, item_count)
		count += 1
		if loop_counter == 0:
			loop_counter = item_count - 1

	print "%s%d. Voltar\n" % (potions, count)
	print "Escolha qual poção você quer usar.\n"

	choice = raw_input("> ")
	if choice.isdigit():
		choice = int(choice) - 1
	if choice < len(unique_items) and choice >= 0:
		item = unique_items[choice]
		index = player.pl_inventory.allPotions.index(item)
		return player.pl_inventory.allPotions.pop(index)
	elif choice == len(unique_items):
		return "back"
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		return choosePotion()
