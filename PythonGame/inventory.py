# coding: utf-8

# --- Inventory System ---
# There are two types of inventory management: Party and PC.

class Inventory(object):	
	def __init__(self, name):		
		self.name = "%s's Inventory" % name

class PCInventory(Inventory):
	def __init__(self, name, weapon, armor):
		self.currentWeapon = weapon
		self.currentArmor = armor
		
	def equip(self, item):
		if type(item) == items.Weapon:
			self.currentWeapon = item
		elif type(item) == items.Armor:
			self.currentArmor = item
		

class PartyInventory(Inventory):
	def __init__(self, name):
		self.allWeapons = []
		self.allArmors = []
		self.allPotions = []
		self.questItems = []
		
	def addItem(self, item):
		if type(item) == items.Weapon:
			self.addWeapon(item)
		elif type(item) == items.Armor:
			self.addArmor(item)
		elif type(item) == items.Potion:
			self.addPotion(item)
		elif type(item) == quests.QuestItem:
			self.addQuestItem(item)
		else:
			raise ValueError('item type not found.')
			
	def addWeapon(self, weapon):	
		self.allWeapons.append(weapon)
		self.allWeapons = sorted(self.allWeapons)

	def addArmor(self, armor):
		self.allArmors.append(armor)
		self.allArmors = sorted(self.allArmors)
			
	def addPotion(self, potion):
		self.allPotions.append(potion)
		self.allPotions = sorted(self.allPotions)

	def addQuestItem(self, item):
		self.questItems.append(item)
		self.questItems = sorted(self.questItems)

# Import Dependecies after declaring Class 
# to fix circular dependecy problems (I guess)
import items
import quests
