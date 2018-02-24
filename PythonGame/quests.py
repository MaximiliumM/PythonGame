# coding: utf-8

import menu
import items

class Quest(object):
	def __init__(self, name, item, reward, text, afterFirstEncounter, endTxt, doneTxt):
		self.name = name
		self.quest_item = item
		self.reward = reward
		self.text = text
		self.text2 = afterFirstEncounter
		self.endTxt = endTxt
		self.doneTxt = doneTxt
		self.hasDone = False
		self.firstEncounter = True

	def getReward(self):
		print self.endTxt
		return self.reward

	def getText(self, firstEncounter):
		if firstEncounter != True:
			return self.text
		else:
			return self.text2

	def getDoneTxt(self):
		return self.doneTxt

	def getEndText(self):
		return self.endTxt

	def checkEndQuest(self, inventory):
		if self.quest_item in inventory:
			self.hasDone = True
			return True
		else:
			return False

def getQuest(num):

	if self.hasDone != True:
		if quests[num - 1].checkEndQuest() != True:
			print quests[num - 1].getText(quests[num - 1].firstEncounter)
			quests[num - 1].firstEncounter = False
		else:
			print quests[num - 1].getDoneTxt()
	else:
		print quests[num - 1].getEndText()

class QuestItem(object):
	def __init__(self, name, info):
		self.name = name
		self.info = info

azeitona = QuestItem("Azeitona", "Uma azeitona encontrada em empadas.")
chapeuFalante = QuestItem("Chapéu Falante", "Um chapéu tagarela safado que quer testar seu conhecimento de Geografia.")

q1 = Quest("A Azeitona da Empada", azeitona, items.lesserPot,
"""Você! Tenho certeza que é você! Só pode ser você!
Entre na minha loja agora! Você não vai acreditar! É SURREAL!
""",
"""Você ainda não foi lá? Eu quero minha loja de volta! Rápido!
""",
"""Obrigado, você salvou a minha loja! Eu não sabia que misturar
metanotiol, dimetil sulfeto e mercaptanas na minha querida empada
poderia resultar em algo tão assim... estranho.
""",
"""Gostaria de experimentar a mais nova sensação de empadas da vila?
É explosivo!
"""
)

q2 = Quest("A Lenda do Chapéu Falante", chapeuFalante, items.intPotion,
	"""Hey, stranger! Você já ouviu falar na Lenda do Chapéu Falante?
	Dizem que ele é capaz de te dar conhecimento INFINITO!
	Como eu sou um benfeitor, ofereço-te este mapa que te guiará até
	os cafund... quer dizer, até o ÚNICO Chapéu Falante.
	""",
	"""Vo-Você aqui? Não esperava te ver tão cedo. Já achou o Chapéu?
	""",
	"""Não, não. Tire esse Chapéu de perto de mim! Fique com ele!
	Não era para você trazê-lo aqui! Você nos destruirá! *corre*
	""",
	"""AAAHHHHH!!!!
	""")

quests = [q1, q2]