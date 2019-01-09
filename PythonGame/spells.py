# coding: utf-8

from random import randint
from time import sleep
import player

class Condition(object):
	def __init__(self, name, amount, afflictChance, cureChance, message):
		self.name = name
		self.amount = amount
		self.afflictChance = afflictChance
		self.cureChance = cureChance
		self.message = message
		self.status = "not active"
		
	def getEffect(self, target):	
		if self.status == "not active":
			if self.checkAfflict():
				target.condition = self
				self.status = "active"
				print "%s está %s.\n" % (target.name, self.message)
			else:
				print "%s falhou!\n" % self.name
			
		elif self.status == "active":
			if self.amount != 0:
				roll = randint(1, self.amount)
				target.hp -= roll
				print "%s deu %d de dano!\n" % (self.name, roll)
			
			if self.checkDebuff():
				target.condition = None
				print "%s não está mais em efeito!\n" % self.name
				
			sleep(1)
		
	def checkAfflict(self):
		if randint(0, 100) < self.afflictChance:
			return True
		else:
			return False
	
	def checkDebuff(self):
		if randint(0, 100) < self.cureChance:
			self.status = "not active"
			return True
		else:
			return False
		
		
			

class Spell(object):
	def __init__(self, name, amount, mana, hostility, statAffected, operator, turns, accuracy=100, condition=None):
		self.name = name
		self.manaCost = mana
		#self.lvlNeeded = lvl
		self.amount = amount
		self.hostility = hostility
		self.stat = statAffected
		self.operator = operator
		self.turn = 0
		self.turns = turns
		self.status = "not active"
		self.accuracy = accuracy
		self.condition = condition
		self.lastRoll = 0

	def getEffect(self, user):
		roll = randint(1, self.amount)
		if self.operator == "+":
			return roll + user.level
		elif self.operator == "*":
			return roll * user.level
		else:
			return roll

	def debuff(self, user):
		self.status = "not active"
		self.turn = 0
		
		if self.stat == "str":
			user.strBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Força!\n" % (self.name, self.lastRoll)
		elif self.stat == "vit":
			user.vitBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Vitalidade!\n" % (self.name, self.lastRoll)
		elif self.stat == "int":
			user.intBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Inteligência!\n" % (self.name, self.lastRoll)
		elif self.stat == "dex":
			user.dexBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de Destreza!\n" % (self.name, self.lastRoll)
		elif self.stat == "all":
			user.strBase -= self.lastRoll
			user.vitBase -= self.lastRoll
			user.intBase -= self.lastRoll
			user.dexBase -= self.lastRoll
			print "O efeito de %s terminou! Menos %d de todos os atributos!\n" % (self.name, self.lastRoll)
		elif self.stat == "hp":
			print "O efeito de %s terminou!\n" % self.name 
			
		self.lastRoll = 0
		user.updateModifiers()

	def use(self, user, target):
	
		roll = self.getEffect(user)

		if self.manaCost <= user.mana and self.status != "active":	
			if self.hostility == True:
								
				if self.stat == "hp":
					target.hp -= roll
					print "Você deu %d de dano!\n" % roll
					
					sleep(1)
					
					if self.turns > 1:
						self.status = "active"
						
				if self.condition != None:
					self.condition.getEffect(target)
						
			elif self.hostility == False:
				if self.stat == "hp":
					if user.hp + self.amount > user.maxHP: 
						print "Você recuperou %d de vida!\n" % (user.maxHP - user.hp)
						user.hp = user.maxHP
					else:
						user.hp += roll
						print "Você recuperou %d de vida!\n" % roll
				elif self.stat == "str":
					user.strBase += roll
					print "Você aumentou %d de Força!\n" % roll
				elif self.stat == "vit":
					user.vitBase += roll
					print "Você aumentou %d de Vitalidade!\n" % roll
				elif self.stat == "int":
					user.intBase += roll
					print "Você aumentou %d de Inteligência!\n" % roll
				elif self.stat == "dex":
					user.dexBase += roll
					print "Você aumentou %d de Destreza!\n" % roll
				elif self.stat == "all":
					user.strBase += roll
					user.vitBase += roll
					user.intBase += roll
					user.dexBase += roll
					print "Você aumentou %d de todos os atributos!\n" % roll

			user.mana -= self.manaCost

			if self.stat != "hp":
				self.status = "active"
				user.updateModifiers()
			return True

		else:
			if self.status == "active":
				print "\t*** %s já está ativo ***\n" % self.name
			else:
				print "\t*** Você não tem Mana suficiente ***\n"
			
			return False
			
		sleep(1)
			
# -- Spells Database --
# Spell(name, amount, mana, hostility, statAffected, operator, turns, accuracy, condition)
# Condition(name, amount, afflictChance, cureChance, message)

healing = Spell("Cura", 8, 20, False, "hp", "+", 1)
fireball = Spell("Bola de Fogo", 6, 20, True, "hp", "*", 1, 90, Condition("Burn", 3, 25, 25, "queimado"))
acidarrow = Spell("Acid Arrow", 8, 30, True, "hp", "*", 1, 90)
poison = Spell("Poison Spray", 3, 12, True, "hp", "*", 1, 100, Condition("Poison", 3, 75, 25, "envenenado"))
bless = Spell("Bless", 1, 40, False, "all", "+", 3)
rage = Spell("Fúria", 6, 10, False, "str", "+", 2)
alacrity = Spell("Alacrity", 4, 10, False, "dex", "+", 2)
freeze = Spell("Freeze", 6, 20, True, "hp", "*", 1, 100, Condition("Freeze", 0, 30, 30, "congelado")) 

barbarian_spells = [rage]
mage_spells = [fireball, freeze, poison]
rogue_spells = []
