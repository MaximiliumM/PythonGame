# coding: utf-8

from random import randint
import quests

class Monster:
	def __init__(self, name, howManyDices, hit_dice, attk_dice, armor_class, dex, treasure, expGiven, quest):
		self.name = name
		self.hp = self.getHP(howManyDices, hit_dice)
		self.attk = attk_dice
		self.ac = armor_class
		self.drops = treasure
		self.dexMod = dex
		self.exp = expGiven
		self.questItem = quest
	
	def getHP(self, dices, hit_dice):
		hp = 0
		for i in range(dices):
			hp += randint(1, hit_dice)
		return hp

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

	def getQuestItem(self):
		print "\n\t*** Você pegou %s! ***\n" % self.questItem.name
		return self.questItem
	
nightmare = Monster("Pesadelo", 2, 12, 8, 15, 3, 2, 1000, None)
narguilosa = Monster("Narguilosa", 2, 8, 8, 15, 3, 1, 500, None)
empada = Monster("Empada", 2, 5, 5, 15, 3, "quest", 1000, quests.azeitona)







