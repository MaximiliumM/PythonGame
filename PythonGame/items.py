# coding: utf-8

import random

class Item(object):
	def __init__(self, name, info, percent, price):
		self.name = name
		self.info = info
		self.dropChance = percent
		self.price = price

class Weapon(Item):
	def __init__(self, name, info, damage, critical, percent, price):
		super(Weapon, self).__init__(name, info, percent, price)
		self.dmg = damage
		self.crit = critical

class Armor(Item):
	def __init__(self, name, info, resist, percent, price):
		super(Armor, self).__init__(name, info, percent, price)
		self.resistance = resist

class Potion(Item):
	def __init__(self, name, info, healAmount, statAffected, percent, price):
		super(Potion, self).__init__(name, info, percent, price)
		self.statAffected = statAffected
		self.amount = healAmount

	def use(self, user):
		if self.e == "hp":
			print "Você recuperou %d pontos de vida!\n" % self.amount
			if user.hp + self.amount > user.maxHP: 
				user.hp = user.maxHP
			else:
				user.hp += self.amount
		elif self.statAffected == "mana":
			print "Você recuperou %d pontos de mana!\n" % self.amount
			user.mana += self.amount
		elif self.statAffected == "int":
			if self.amount > 1:
				print "Você ganhou %d pontos de Inteligência" % self.amount
			else:
				print "Você ganhou %d ponto de Inteligência" % self.amount
			user.intBase += self.amount
			user.updateModifiers()
	
class ItemManager(object):
	def __init__(self, allItems):
		self.items = allItems
	
	def getItemByName(self, name):
		for item in self.items:
			if item.name == name:
				return item
	
	def getRandomItem(self):
		x = random.random() * 100
		candidates = []
		
		for item in self.items:
				if x < item.dropChance:
					candidates.append(item)
			
		if len(candidates) == 0:
			return None		
		elif len(candidates) > 1:
			return random.choice(candidates)
		else:
			return candidates[0] # only one item, thus first index
			
import player

itemManager = ItemManager([
				
# -- Weapons -- name, info, damage, critical, percent, price
		
Weapon("Espada de Madeira", "Uma lasca de madeira que você achou ali atrás.", 1, 20, 15.0, 2),
Weapon("Sword of God", "Espada embuida por mãos divinas", 4, 15, 1.00, 50),
Weapon("Flame Blade", "Espada forjada nas profundezas do Nether", 6, 20, 0.10, 100),
Weapon("Super Saiyajin King Kong Dragon Sword of Monster Trap", "Uma espada. Uma.", 999, 2, 0.01, 9999),
Weapon("Espada de Diamante", "Espada forjada por diamantes das Montanhas de Mordor", 8, 20, 0.05, 150),
Weapon("Mjolnir", "Um martelo que afugenta fraudadores.", 6, 20, 0.04, 300),
Weapon("Garrafa Quebrada", "Uma garrafa quebrada na cabeça de uma cobra.", 2, 20, 20.0, 1),
Weapon("Espada Tinteira", "Uma espada para decorar os inimigos.", 3, 20, 2.00, 25),
Weapon("Water Blade", "Espada forjada nas profundezas de Atlantis", 7, 20, 0.08, 120),
Weapon("Mystic Blade", "Uma espada com um brilho sinistro. Sua origem é misteriosa", 9, 19, 0.04, 140),
Weapon("Masamune", "Espada lendária criada nas terras do sol nascente pelo Mestre Hanzo.", 8, 20, 0.04, 200),

# -- Armors -- name, info, resist, percent, price

Armor("Chainmail", "Malha metálica de baixa proteção", 5, 0.50, 50),
Armor("Barril", "Um barril de chope descartado.", 2, 15.0, 10),
Armor('Armadura de Escama de "Dragão"', "Escama de um lagarto que você encontrou bebâdo na esquina.", 4, 5.00, 25),
Armor("Armadura de Escama de Dragão", "Escama de um dragão encontrado no interior das Montanhas Tártaro.", 10, 0.10, 800),
Armor("Armadura Metálica", "Metal reforçado com acabamento de couro.", 8, 0.50, 300),
Armor("Couraça", "Armadura de couro leve composta de várias camadas de tecido.", 2, 4.0, 100),


# -- Potions -- name, info, healAmount, statAffected, percent, price

Potion("Greater Healing Potion", "Recupera 10 pontos de vida", 10, "hp", 5.00, 30),
Potion("Lesser Healing Potion", "Recupera 2 pontos de vida", 2, "hp", 30.0, 10),
Potion("Poção do Conhecimento", "Aumenta sua inteligência em +1", 1, "int", 0.5, 100)

])

