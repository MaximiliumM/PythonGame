# coding: utf-8

from random import randint
import player

class Spell(object):
	def __init__(self, name, amount, mana, hostility, statAffected, operator, turns):
		self.name = name
		self.manaCost = mana
		self.amount = amount
		self.hostility = hostility
		self.stat = statAffected
		self.operator = operator
		self.turns = turns
		self.status = "not active"
		self.lastRoll = 0

	def getEffect(self):
		roll = randint(1, self.amount)
		if self.operator == "+":
			return roll + player.pl.level
		elif self.operator == "*":
			return roll * player.pl.level
		else:
			return roll

	def debuff(self):
		self.status = "not active"
		if self.stat == "str":
			player.pl.strBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Força!\n" % (self.name, self.lastRoll)
		elif self.stat == "vit":
			player.pl.vitBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Vitalidade!\n" % (self.name, self.lastRoll)
		elif self.stat == "int":
			player.pl.intBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Inteligência!\n" % (self.name, self.lastRoll)
		elif self.stat == "dex":
			player.pl.dexBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Destreza!\n" % (self.name, self.lastRoll)
		elif self.stat == "all":
			player.pl.strBase -= self.lastRoll
			player.pl.vitBase -= self.lastRoll
			player.pl.intBase -= self.lastRoll
			player.pl.dexBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de todos os atributos!\n" % (self.name, self.lastRoll)

		player.pl.updateModifiers()

	def use(self, monster):

		roll = self.getEffect()

		if self.manaCost <= player.pl.mana and self.status != "active":	
			if self.hostility == True:
				if self.stat == "hp":
					monster.hp -= roll
					print "Você deu %d de dano!\n" % roll
			elif self.hostility == False:
				if self.stat == "hp":
					if player.pl.hp + self.amount > player.pl.maxHP: 
						print "Você recuperou %d de vida!\n" % (player.pl.maxHP - player.pl.hp)
						player.pl.hp = player.pl.maxHP
					else:
						player.pl.hp += roll
						print "Você recuperou %d de vida!\n" % roll
				elif self.stat == "str":
					player.pl.strBase += roll
					print "Você aumentou %d de Força!\n" % roll
				elif self.stat == "vit":
					player.pl.vitBase += roll
					print "Você aumentou %d de Vitalidade!\n" % roll
				elif self.stat == "int":
					player.pl.intBase += roll
					print "Você aumentou %d de Inteligência!\n" % roll
				elif self.stat == "dex":
					player.pl.dexBase += roll
					print "Você aumentou %d de Destreza!\n" % roll
				elif self.stat == "all":
					player.pl.strBase += roll
					player.pl.vitBase += roll
					player.pl.intBase += roll
					player.pl.dexBase += roll
					print "Você aumentou %d de todos os atributos!\n" % roll

			player.pl.mana -= self.manaCost

			if self.stat != "hp":
				self.status = "active"
				self.lastRoll = roll
				player.pl.updateModifiers()
			return True

		else:
			if self.status == "active":
				print "\t*** %s já está ativo ***\n" % self.name
			else:
				print "\t*** Você não tem Mana suficiente ***\n"
			
			return False

healing = Spell("Cura", 8, 20, False, "hp", "+", 1)
fireball = Spell("Bola de Fogo", 6, 20, True, "hp", "*", 1)
bless = Spell("Bless", 1, 40, False, "all", "+", 3)
rage = Spell("Fúria", 6, 10, False, "str", "+", 2)
alacrity = Spell("Alacrity", 4, 10, False, "dex", "+", 2)

barbarian_spells = [rage]
mage_spells = [healing, fireball, bless]
rogue_spells = []