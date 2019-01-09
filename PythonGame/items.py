# coding: utf-8

class Item(object):
	def __init__(self, name, info, percent, price):
		self.name = name
		self.info = info
		self.percentage = percent
		self.price = price

class Weapon(Item):
	def __init__(self, name, info, damage, percent, price):
		super(Weapon, self).__init__(name, info, percent, price)
		self.dmg = damage

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
			
# -- Weapons -- name, info, damage, percent, price
		
woodsword = Weapon("Espada de Madeira", "Uma lasca de madeira que você achou ali atrás.", 1, 15.0, 2)
sog = Weapon("Sword of God", "Espada embuida por mãos divinas", 4, 1.00, 50)
flameblade = Weapon("Flame Blade", "Espada forjada nas profundezas do Nether", 6, 0.10, 100)
cheaterSword = Weapon("Super Saiyajin King Kong Dragon Sword of Monster Trap", "Uma espada. Uma.", 999, 0.01, 9999)
diamondSword = Weapon("Espada de Diamante", "Espada forjada por diamantes das Montanhas de Mordor", 8, 0.05, 150)
mjolnirRisk = Weapon("Mjolnir", "Um martelo que afugenta fraudadores.", 6, 0.04, 300)
brokenBottle = Weapon("Garrafa Quebrada", "Uma garrafa quebrada na cabeça de uma cobra.", 2, 20.0, 1)
tintSword = Weapon("Espada Tinteira", "Uma espada para decorar os inimigos.", 3, 2.00, 25)
waterblade = Weapon("Water Blade", "Espada forjada nas profundezas de Atlantis", 7, 0.08, 120)
mysticblade = Weapon("Mystic Blade", "Uma espada com um brilho sinistro. Sua origem é misteriosa", 9, 0.04, 140)

# -- Armors --

chainmail = Armor("Chainmail", "Malha metálica de baixa proteção", 5, 0.50, 50)
barrel = Armor("Barril", "Um barril de chope descartado.", 2, 15.0, 10)
fakeDragonScaled = Armor('Armadura de Escama de "Dragão"', "Escama de um lagarto que você encontrou bebâdo na esquina.", 4, 5.00, 25)
dragonScaled = Armor("Armadura de Escama de Dragão", "Escama de um dragão encontrado no interior das Montanhas Tártaro.", 10, 0.10, 150)

# -- Potions --

greaterPot = Potion("Greater Healing Potion", "Recupera 10 pontos de vida", 10, "hp", 5.00, 30)
lesserPot = Potion("Lesser Healing Potion", "Recupera 2 pontos de vida", 2, "hp", 10.0, 10)
intPotion = Potion("Poção do Conhecimento", "Aumenta sua inteligência em +1", 1, "int", 0, 100)

import player

allItems = [woodsword, sog, chainmail, greaterPot, flameblade, cheaterSword, lesserPot, diamondSword, barrel, mjolnirRisk, brokenBottle, tintSword, fakeDragonScaled, dragonScaled, waterblade, mysticblade]

