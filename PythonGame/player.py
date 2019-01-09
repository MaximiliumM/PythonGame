# coding: utf-8

from random import randint
from party import pl_party
import items
import quests


class Player(object):
	def __init__(self, name, theclass, lvl, stre, vit, inte, dex):
		
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

		self.name = name
		self.theclass = theclass
		self.hp = self.getInitialHP()
		self.maxHP = self.hp
		self.mana = self.getInitialMana()
		self.maxMana = self.mana
		self.level = lvl
		self.exp = 0
		self.exp_needed = 1000
		self.crit = 2
		self.bonus = 0
		self.initiative = 0
		self.condition = None
		self.inventory = Inventory(items.woodsword, items.barrel, items.lesserPot)

		# -- Spells --
		self.class_spells = []
		self.startWith = 3
		self.index = 0 # spells index
	
		# -- Armor Class --
		self.ac = 10 + self.inventory.currentArmor.resistance + self.dexMod

		# -- Money --
		self.gold = 2000

	def getModifier(self, stat):
		return (stat - 10) / 2

	def updateModifiers(self):
		self.strMod = self.getModifier(self.strBase)
		self.vitMod = self.getModifier(self.vitBase)
		self.intMod = self.getModifier(self.intBase)
		self.dexMod = self.getModifier(self.dexBase)		

	def getInitialHP(self):
		hp = 0
		for i in range(self.vitMod):
			hp += randint(1, 4)
		return hp + self.vitBase

	def getInitialMana(self):
		mana = 0
		for i in range(self.intMod):
			mana += randint(1, 4) * 10
		return mana

	def check_lvlUp(self):
		if self.exp >= self.exp_needed:
			self.levelUp()

	def levelUp(self):
		self.level += 1
		self.exp = 0
		self.exp_needed = 1000 * self.level
		if self.level == 5 or self.level == 10:
			self.increaseStat()
			self.getNewSpell()
			if self.vitMod > 0:
				for i in range(self.vitMod):
					self.maxHP += randint(1, 4)
			if self.intMod > 0:	
				for i in range(self.intMod):
					self.maxMana += randint(1, 4) * 10
		else:
			if self.vitMod > 0:
				for i in range(self.vitMod):
					self.maxHP += randint(1, 4)
			if self.intMod > 0:	
				for i in range(self.intMod):
					self.maxMana += randint(1, 4) * 10
					
		self.hp = self.maxHP
		self.mana = self.maxMana

	def increaseStat(self):
		statsPoints = 1
		print "Você tem %d ponto para gastar." % statsPoints
		print "Atributos:\n"
		print "1. Força: %d | 2. Vitalidade: %d | 3. Inteligência: %d | 4. Destreza: %d" % (self.strBase, self.vitBase, self.intBase, self.dexBase)
		print "Em qual atributo você quer colocar?\n\n"

		choice = raw_input("> ")

		if choice == "1":
			self.strBase += statsPoints
		elif choice == "2":
			self.vitBase += statsPoints
		elif choice == "3":
			self.intBase += statsPoints
		elif choice == "4":
			self.dexBase += statsPoints
		else:
			print "\t*** Escolha um dos números do menu ***"

		self.updateModifiers()

	def getNewSpell(self):
		import spells
		if self.theclass == "Barbarian":
			self.class_spells.append(spells.barbarian_spells[self.index])
		elif self.theclass == "Mage":
			self.class_spells.append(spells.mage_spells[self.index])
		elif self.theclass == "Rogue":
			self.class_spells.append(spells.rogue_spells[self.index])
		self.index += 1

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

	def attkDamage(self):
		roll = randint(1, self.inventory.currentWeapon.dmg)
		return self.strMod + roll + self.bonus
		
	def rollInitiative(self):
		roll = randint(1, 20)
		self.initiative = self.dexMod + roll
		

class Inventory(object):
	def __init__(self, weapon, armor, potion):
		self.currentWeapon = weapon
		self.currentArmor = armor

		self.allWeapons = [self.currentWeapon]
		self.allArmors = [self.currentArmor]
		self.allPotions = [potion]
		self.questItems = []
		
	def equip(self, item):
		if type(item) == items.Weapon:
			self.currentWeapon = item
		elif type(item) == items.Armor:
			self.currentArmor = item
		
	def addItem(self, item):
		if type(item) == items.Weapon:
			self.addWeapon(item)
		elif type(item) == items.Armor:
			self.addArmor(item)
		elif type(item) == items.Potion:
			self.addPotion(item)
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


pl = object

def debugMode():
	
	global pl
	
	pl = Player("Max", "Mage", 1, 8, 14, 18, 15)
	pl_party.members.append(pl)
	
	# NPC Test
	npc = Player("Luna", "Barbarian", 1, 18, 15, 8, 14)
	pl_party.members.append(npc)
	
	# --- Initial Inventory ----
	pl.inventory = Inventory(items.woodsword, items.barrel, items.lesserPot)
	# --------------------------
	
	# -- Test Items --
	pl.inventory.addPotion(items.lesserPot)
	pl.inventory.addPotion(items.lesserPot)
	pl.inventory.addPotion(items.lesserPot)
	pl.inventory.addWeapon(items.sog)

def class_choice():
	global pl

	menu = """
	Escolha sua classe:
	1. Barbarian
	2. Mage
	3. Rogue

	> """

	choice = raw_input(menu)

	if choice != "":
		if choice == "1":
			strBase, vitBase, intBase, dexBase = stats()
			pl = Player("Barbarian", 1, strBase, vitBase, intBase, dexBase)
		elif choice == "2":
			strBase, vitBase, intBase, dexBase = stats()
			pl = Player("Mage", 1, strBase, vitBase, intBase, dexBase)
		elif choice == "3":
			strBase, vitBase, intBase, dexBase = stats()
			pl = Player("Rogue", 1, strBase, vitBase, intBase, dexBase)
		else:
			print "\n\t*** Escolha um dos números do menu ***"
			class_choice()
	else:
		print "\n\t*** Escolha um dos números do menu ***"
		class_choice()
	
def stats():

	strBase = 0
	vitBase = 0
	intBase = 0
	dexBase = 0
	statsPoints = 55

	while strBase < 8 or strBase > 18:
		print "Você tem: %d pontos restantes." % statsPoints
		print "Escolha o quanto de Força você vai ter:\n"
		print "*** Valor entre 8 e 18 ***\n\n"
		strBase = raw_input("> ")
		if strBase.isdigit():
			strBase = int(strBase)
		if strBase >= 8 and strBase <= 18:
			statsPoints -= strBase
	while vitBase < 8 or vitBase > 18:
		print "Você tem: %d pontos restantes." % statsPoints
		print "Escolha o quanto de Vitalidade você vai ter:\n"
		print "*** Valor entre 8 e 18 ***\n\n"
		vitBase = raw_input("> ")
		if vitBase.isdigit():
			vitBase = int(vitBase)
		if vitBase >= 8 and vitBase <= 18:
			statsPoints -= vitBase
	while intBase < 8 or intBase > 18 or statsPoints < 8:
		print "Você tem: %d pontos restantes." % statsPoints
		print "Escolha o quanto de Inteligência você vai ter:\n"
		print "*** Valor entre 8 e 18 ***\n\n"
		intBase = raw_input("> ")
		if intBase.isdigit():
			intBase = int(intBase)
		if intBase >= 8 and intBase <= 18:
			statsPoints -= intBase
	while statsPoints != 0:
		print "Você tem: %d pontos restantes." % statsPoints
		print "Escolha o quanto de Destreza você vai ter:\n"
		print "*** Valor entre 8 e 18 ***\n\n"
		dexBase = raw_input("> ")
		if dexBase.isdigit():
			dexBase = int(dexBase)
			if statsPoints - dexBase == 0:
				statsPoints -= dexBase

	print "Estes são seus atributos:\n"
	print "Força: %d" % strBase
	print "Vitalidade: %d" % vitBase
	print "Inteligência: %d" % intBase
	print "Destreza: %d\n" % dexBase
	print "Confirma? [S/N]\n"
	
	choice = raw_input("> ").lower()

	while choice != "s" or choice != "n":
		if choice == "s":
			return strBase, vitBase, intBase, dexBase
		elif choice == "n":
			return stats()
		else:
			print "Escolha 'S' para 'Sim' ou 'N' para 'Não'.\n"
			choice = raw_input("> ").lower()
