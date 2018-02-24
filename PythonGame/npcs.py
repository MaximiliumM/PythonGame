# coding: utf-8

from random import randint
import quests

class NPC(object):
	def __init__(self, name, num):
		self.name = name
		self.questNum = num

	def getTalk(self):

		if self.questNum == 0:
			self.getRandomTalk()
		else:
			quests.getQuest(self.questNum)

	def getRandomTalk(self):
		talks = [
		"Oi! Eu não tenho nada a oferecer a você. Adeus!",
		"Maldição! Não consigo entender porque esse jogo não faz sentido!",
		"Quem é você? Eu com certeza nunca vi você por aqui.",
		"Vai embora!",
		"Por que você tá falando comigo?"]

		print "%s: %s" % (self.name, talks[randint(0, len(talks) - 1)])

johnsmith = NPC("John Smith", 0)
oliver = NPC("Oliver", 1)
stranger = NPC("Encapuzado", 2)
