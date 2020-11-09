# coding: utf-8

# --- Battle System ---
#
# The main function battle() requires a party of monsters as argument.
#
# TO DO:
# - Need to make AI capable of healing friends.
# - Line 133: For now, there are no NPCs in the player party, so the potions menu work properly.
# 	Need to change that in the future.
# - Line 239: Need to make monsters capable of using potions.
# ----------------------

from time import sleep
from party import pl_party
import random
import player
import monsters
import menu
import operator

turn = 1
monsters_alive = True
player_alive = True
buffs = []
spell_buff = False

def battle(monstersParty):
	
	global turn
	global monsters_alive
	global player_alive
	
	# --- Initiative Check ---
	print "\n\t*** Checando Iniciativas ***\n"
	order = checkInitiative(monstersParty.members + pl_party.members)
	sleep(1)
	
	orderStr = " > ".join(map(operator.attrgetter('name'), order))
		
	print "\tOrdem de Turno\n", orderStr
	
	sleep(1)
	
	print "\n\t*** Batalha ***"
	
	while monsters_alive and player_alive:
		
		print "\t*** Turno %d ***\n" % turn
		
		for index, attacker in enumerate(order):
			
			if attacker.hp > 0:
				
				print "\tTurno - %s\n" % attacker.name
				
				if (attacker.condition != None) and (attacker.condition.name == "Freeze" or attacker.condition.name == "Paralysis"):
						print "%s não consegue se mover por estar %s.\n" % (attacker.name, attacker.condition.message)
				else:
					if isinstance(attacker, player.Player):
						playerMenu(attacker, monstersParty.members)
					else:
						monsterTurn(attacker)
				
				checkCondition(attacker)	
				checkIfAlive([monstersParty, pl_party])
				
				if monsters_alive != True or player_alive != True:
					break
			
		turn += 1
	
	# While-loop has been broken		
	endBattle([monstersParty, pl_party])
	return
	

def endBattle(group):
	
	(monsterParty, playerParty) = group
	
	if player_alive == False:
		print "Fim de jogo!"
		exit()
	elif monsters_alive == False:
			
		for monster in monsterParty.members:
			
			print "Você ganhou %d de experiência do %s!" % (monster.exp, monster.name)
			
			for player in playerParty.members:
				player.exp += monster.exp
				player.check_lvlUp()
				
			sleep(1)
			
			if monster.drops != "quest":
				got_item = bool
				for i in range(monster.drops):
					if menu.getRandomItem():
						got_item = True
					else:
						if got_item != True:
							got_item = False
	
				if got_item == False:
					print "\n\t*** O %s não deu nada ***\n" % monster.name
			else:
				pl_party.inventory.addQuestItem(monster.getQuestItem())
				
	sleep(2)
		
# For now, buffs are disabled
def checkCondition(attacker):
	
	global buffs
	global spell_buff
	
	if spell_buff == True:
		for buff in buffs:						
			buff.turn += 1
			if buff.turn > buff.turns:
				buff.debuff()
				buffs.remove(buff)
		
		if len(buffs) == 0:
			spell_buff = False
			
	if attacker.condition != None:
		attacker.condition.getEffect(attacker)
	
def checkInitiative(group):
	
	for member in group:
		member.rollInitiative()
		
	return sorted(group, key=operator.attrgetter('initiative'))
		
	
def playerMenu(player, monsters):
	print "HP: %d/%d" % (player.hp, player.maxHP)
	print "Mana: %d/%d\n" % (player.mana, player.maxMana)
	print "1. Atacar"
	print "2. Usar Magia"
	print "3. Usar Poção\n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		target = getTarget(monsters)
		
		if target == "back":
			playerMenu(player, monsters)
		else:
			attack(player, target)
			
	elif choice == "2":
		spell = chooseSpell(player)
		
		if spell == "back":
			playerMenu(player, monsters)
		else:
			if spell.hostility == True:
				if spell.range == "area":
					target = monsters
				else:
					target = [getTarget(monsters)]
			else:
				if spell.range == "self":
					target = [player]
				elif spell.range == "area":
					target = pl_party.members
				else:
					target = [getTarget(pl_party.members)]
			
			if target == "back":
				playerMenu(player, monsters)
			else:
				cast = spell.use(player, target)
				if cast != False:					
					if spell.turns > 1:
						spell_buff = True
						buffs.append(spell)
				else:
					playerMenu(player, monsters)
					
	elif choice == "3":
		if len(pl_party.inventory.allPotions) != 0:	
			potion = choosePotion()
			if potion == "back":
				playerMenu(player, monsters)
			else:
				potion.use(player)
		else:
			print "\t*** Você não tem mais poções! ***\n"
			playerMenu(player, monsters)
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		playerMenu(player, monsters)
		

def monsterTurn(monster):
	
	(outcome, target) = decideAttack(monster)
	
	if outcome == "Melee":
		attack(monster, target)
	else:
		# outcome is a spell
		cast = outcome.use(monster, [target])
		
		if cast != False:
			if outcome.turns > 1:
				spell_buff = True
				buffs.append(outcome)
				


def decideAttack(monster):
	# If AI has low hp, check if heal is possible
	if (monster.hp * 100 / monster.maxHP) < 30:
		if len(monster.defenseSpells) > 0:
			chosenSpell = monster.defenseSpells[0]

			for spell in monster.defenseSpells:
				if spell.stat != "hp":
					continue
				
				if spell.amount > chosenSpell.amount:
					if (monster.mana - spell.manaCost) >= 0:
						chosenSpell = spell
			
			if (monster.mana - chosenSpell.manaCost) >= 0:
				return (chosenSpell, monster)
		
		# Check if AI has potions to use
		# -- NOT IMPLEMENTED YET --
		
	
	# Decide who will be targeted from the player's party
	# Right now, the AI will pick the party member with lowest HP
	lowestHP_target = None
	
	for member in pl_party.members:
		if member.hp <= 0:
			continue
			
		if lowestHP_target is not None:
			if member.hp <= lowestHP_target.hp:
				lowestHP_target = member
		else:
			lowestHP_target = member
		
	# AI will attack using Melee if target has low HP and it can be one-hit kill
	if (lowestHP_target.hp - monster.attk) <= 0 and monster.dexMod > 2:
		return ("Melee", lowestHP_target)
	
	# Decide if AI will attack using Spell or Melee
	predictedDmg = 0
	
	if len(monster.hostileSpells) > 0:
		chosenSpell = monster.hostileSpells[0]

		for spell in monster.hostileSpells:
			if spell.stat != "hp":
				continue
			
			if spell.amount > chosenSpell.amount:
				if (monster.mana - spell.manaCost) >= 0:
					chosenSpell = spell
		
		if (monster.mana - chosenSpell.manaCost) >= 0:
			if chosenSpell.operator == "*":
				predictedDmg = chosenSpell.amount * monster.level
			
			if predictedDmg > monster.attk:				
				return (chosenSpell, lowestHP_target)
				
	# If no mana or no spells
	return ("Melee", lowestHP_target)
				

def getTargetForMonsters():
	group = []
	
	for member in pl_party.members:
		if member.hp <= 0:
			continue
		
		group.append(member)
		
	return random.choice(group)


def getTarget(possibleTargets):
	targets = ""
	targetsList = []
	count = 1

	for target in possibleTargets:
		if target.hp <= 0:
			continue
			
		targets += "%d. %s, HP: %d\n" % (count, target.name, target.hp)
		count += 1	
		targetsList.append(target)
		
	print "%s%d. Voltar\n" % (targets, count)
	print "Escolha o alvo.\n"

	choice = raw_input("> ")
	
	if choice.isdigit():
		choice = int(choice) - 1

	if choice < len(targetsList) and choice >= 0:
		return targetsList[choice]
	elif choice == len(targetsList):
		return "back"
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		return getTarget(possibleTargets)
	

def attack(attacker, target):
	if attacker.hp > 0:
		hit = checkHit(attacker, target)
		sleep(2)
			
		if hit == "Critical":
			print "Dano Crítico!"
			dmg = attacker.attkDamage() * attacker.crit
			target.hp -= dmg
			print "%s levou %d de dano!\n" % (target.name, dmg)
		elif hit == True:
			dmg = attacker.attkDamage()
			target.hp -= dmg
			print "%s levou %d de dano!\n" % (target.name, dmg)
		else:
			print "%s errou!\n" % attacker.name
			
	sleep(1)	


def checkHit(attacker, defender):
	attk = attacker.hitOrMiss()
	def_ac = defender.ac
	if attk == "Condition":
		return "Condition"
	elif attk == "Fumble":
		return False
	elif attk == "Critical":
		return "Critical"
	elif attk > def_ac:
		return True
	else:
		return False

def chooseSpell(player):
	spells = ""
	count = 1

	for spell in player.class_spells:
		spells += "%d. %s, %dMP\n" % (count, spell.name, spell.manaCost)
		count += 1

	print "%s%d. Voltar\n" % (spells, count)
	print "Escolha qual magia você quer usar.\n"

	choice = raw_input("> ")
	
	if choice.isdigit():
		choice = int(choice) - 1
		
	if choice < len(player.class_spells) and choice >= 0:
		return player.class_spells[choice]
	elif choice == len(player.class_spells):
		return "back"
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		return chooseSpell(player)
		
def choosePotion():
	potions = ""
	count = 1
	loop_counter = 0
	unique_items = []

	for potion in pl_party.inventory.allPotions:
		item_count = pl_party.inventory.allPotions.count(potion)
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
		index = pl_party.inventory.allPotions.index(item)
		return pl_party.inventory.allPotions.pop(index)
	elif choice == len(unique_items):
		return "back"
	else:
		print "\t*** Escolha um dos números do menu ***\n"
		return choosePotion()
		
		
# This function takes an array with
# two parties to check if members are alive.
def checkIfAlive(group):
	
	global monsters_alive
	global player_alive
	
	for party in group:
		for member in party.members:
			if member.hp <= 0 and not member in party.faintedMembers:
				party.faintedMembers.append(member)
				print "%s morreu!\n" % member.name
		
		if len(party.members) == len(party.faintedMembers):
			if party.type == "player":
				player_alive = False
			else:
				monsters_alive = False
			
