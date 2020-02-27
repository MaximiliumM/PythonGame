# coding: utf-8

# --- Monster Class ---
#
# The class arguments are:
#		name: Monster's name
#		stre, vit, inte, dex: Base stats
#		howManyDices: How many dices the system will roll for HP when the monster is spawned
#		hit_dice: What dice will be rolled for HP
#		attk_dice: What dice will be rolled for Attack
#		armor_class: This is how hard it is to hit the monster
#		treasure: It can be a number (how many drops) or a string "quest" when the drop is part of a quest
#		expGiven: Experience given to player when monster dies
#		quest: The quest item object is passed here.
#		monster_spells: An array with spells the monster can cast in battle
#
# TO DO:
# - Monsters need to learn how to cast spells. (implement spell system here)
# ----------------------

from random import randint
import quests
import spells

class Monster:
	def __init__(self, name, lvl, stre, vit, inte, dex, howManyDices, hit_dice, attk_dice, armor_class, treasure, expGiven, quest, monster_spells):
		
		# -- Base Stats --
		self.strBase = stre
		self.vitBase = vit
		self.intBase = inte
		self.dexBase = dex
		# -- Stats Modifiers --
		self.strMod = self.getModifier(stre)
		self.vitMod = self.getModifier(vit)
		self.intMod = self.getModifier(inte)
		self.dexMod = self.getModifier(dex)
		
		# -- Spells --
		self.spells = monster_spells
		(self.hostileSpells, self.defenseSpells) = self.categorizeSpells(monster_spells)
		
		self.name = name
		self.level = lvl
		self.dices = howManyDices
		self.hit_dice = hit_dice
		self.hp = self.getHP()
		self.maxHP = self.hp
		self.mana = self.getMana()
		self.maxMana = self.mana
		self.attk = attk_dice
		self.ac = armor_class
		self.condition = None
		self.drops = treasure
		self.crit = 2
		self.exp = expGiven
		self.initiative = 0
		self.questItem = quest
		
	def getModifier(self, stat):
		return (stat - 10) / 2

	def updateModifiers(self):
		self.strMod = self.getModifier(self.strBase)
		self.vitMod = self.getModifier(self.vitBase)
		self.intMod = self.getModifier(self.intBase)
		self.dexMod = self.getModifier(self.dexBase)
	
	def spawn(self):
		self.hp = self.getHP()
	
	def getHP(self):
		hp = 0
		for i in range(self.dices):
			hp += randint(1, self.hit_dice)
		return hp
		
	def getMana(self):
		mana = 0
		for i in range(self.intMod):
			mana += randint(1, 4) * 10
		return mana
			
	def categorizeSpells(self, spells):
		hostileSpells = []
		defenseSpells = []
		
		if spells is not None:
			for spell in spells:
				if spell.hostility == True:
					hostileSpells.append(spell)
				else:
					defenseSpells.append(spell)
				
			return (hostileSpells, defenseSpells)
		else:
			return ([],[])
						
	
	def attkDamage(self):
		roll = randint(1, self.attk)
		return roll
		
	def hitOrMiss(self):
		roll = randint(1, 20)
		if roll == 1:
			return "Fumble"
		elif roll == 20:
			return "Critical"
		else:
			return roll + self.dexMod
				
	def rollInitiative(self):
		roll = randint(1, 20)		
		self.initiative = self.dexMod + roll

	def getQuestItem(self):
		print "\n\t*** Você pegou %s! ***\n" % self.questItem.name
		return self.questItem
		
# -- Monsters Database --
# Monster(name, stre, vit, inte, dex, howManyDices, hit_dice, attk_dice, armor_class, treasure, expGiven, quest)
	
nightmare = Monster("Pesadelo", 5, 18, 16, 13, 15, 2, 12, 8, 15, 2, 1000, None, [spells.healing])
narguilosa = Monster("Narguilosa", 3, 16, 13, 1, 15, 2, 8, 8, 15, 3, 500, None, None)
empada = Monster("Empada", 12, 1, 10, 5, 12, 2, 5, 5, 15, "quest", 1000, quests.azeitona, [spells.healing])
goblin = Monster("Goblin", 11, 1,12, 10, 13, 2, 6, 8, 15, 1, 50, None, None)




