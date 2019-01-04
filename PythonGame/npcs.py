# coding: utf-8

from random import randint
import quests

class NPC(object):
	def __init__(self, name):
		self.name = name

	def getTalk(self):
		talks = [
		"Oi! Eu não tenho nada a oferecer a você. Adeus!",
		"Maldição! Não consigo entender porque esse jogo não faz sentido!",
		"Quem é você? Eu com certeza nunca vi você por aqui.",
		"Vai embora!",
		"Por que você tá falando comigo?"]

		print "%s: %s" % (self.name, talks[randint(0, len(talks) - 1)])
		

class QuestNPC(NPC):
	def __init__(self, name, questNum):
		super(QuestNPC, self).__init__(name)
		self.questNum = questNum
		
	def getTalk(self):
		print "%s:\n%s" % (self.name, quests.allQuests[self.questNum].startQuest())
		
		if quests.allQuests[self.questNum].accepted == False:
			self.dialogue()
		
	def dialogue(self):
		print "%s:\n%s" % (self.name, quests.allQuests[self.questNum].getDialogue())

# -- NPCs ---
johnsmith = NPC("John Smith")

# -- Quest NPCs --
oliver = QuestNPC("Oliver", 0)
stranger = QuestNPC("Encapuzado", 1)
