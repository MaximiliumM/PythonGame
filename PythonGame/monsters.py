# coding: utf-8

from random import randint
import quests

class Monster:
	def __init__(self, name, howManyDices, hit_dice, attk_dice, armor_class, dex, treasure, expGiven, quest):
		self.name = name
		self.dices = howManyDices
		self.hit_dice = hit_dice
		self.hp = self.getHP()
		self.attk = attk_dice
		self.ac = armor_class
		self.condition = None
		self.drops = treasure
		self.dexMod = dex
		self.exp = expGiven
		self.questItem = quest
		
	def spawn(self):
		self.hp = self.getHP()
	
	def getHP(self):
		hp = 0
		for i in range(self.dices):
			hp += randint(1, self.hit_dice)
		return hp

	def attkDamage(self):
		roll = randint(1, self.attk)
		return roll
		
	def hitOrMiss(self):
		if self.condition != None:
			if self.condition.name == "Freeze" or self.condition.name == "Paralysis":
				return "Condition"
		else:
			roll = randint(1, 20)
			if roll == 1:
				return "Fumble"
			elif roll == 20:
				return "Critical"
			else:
				return roll + self.dexMod

	def getQuestItem(self):
		print "\n\t*** Você pegou %s! ***\n" % self.questItem.name
		return self.questItem
		
# -- Monsters Database --
# Monster(name, howManyDices, hit_dice, attk_dice, armor_class, dex, treasure, expGiven, quest)
	
nightmare = Monster("Pesadelo", 2, 12, 8, 15, 3, 2, 1000, None)
narguilosa = Monster("Narguilosa", 2, 8, 8, 15, 3, 1, 500, None)
empada = Monster("Empada", 2, 5, 5, 15, 3, "quest", 1000, quests.azeitona)
goblin = Monster("Goblin", 2, 6, 8, 15, 2, 1, 50, None)







