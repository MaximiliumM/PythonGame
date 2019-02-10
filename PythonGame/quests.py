# coding: utf-8

class Quest(object):
	def __init__(self, name, item, reward, firstEncounter, afterFirstEncounter, acceptText, rejectText, afterReject, endTxt, doneTxt, playerDialogue):
		self.name = name
		self.quest_item = item
		self.reward = reward
		self.firstText = firstEncounter
		self.afterFirstEncounter = afterFirstEncounter
		self.acceptText = acceptText
		self.rejectText = rejectText
		self.afterReject = afterReject
		self.endTxt = endTxt
		self.doneTxt = doneTxt
		self.hasDone = False
		self.firstEncounter = True
		self.accepted = False
		self.dialogues = playerDialogue
		
	def getDialogue(self):
		result = "Escolha a resposta:\n"
		for index, dialogue in enumerate(self.dialogues):
			result += "\t%d. %s\n" % (index + 1, dialogue)
			
		print result
		
		choice = raw_input("> ")
		if choice.isdigit():
			if int(choice) == 1:
				return self.acceptQuest()
			elif int(choice) == 2:
				return self.rejectText

	def acceptQuest(self):
		self.accepted = True
		print "\t*** Você recebeu: %s ***\n" % self.name
		return self.acceptText

	def getReward(self):
		player.pl_inventory.questItems.remove(self.quest_item)
		player.pl_inventory.addItem(self.reward)
		return "\nVocê recebeu %s!\n" % self.reward.name 

	def getText(self):
		if self.firstEncounter == True:
			self.firstEncounter = False
			return self.firstText
		elif self.accepted == False:
			return self.afterReject
		else:
			return self.afterFirstEncounter

	def endQuest(self):
		return self.endTxt + self.getReward()

	def getDoneTxt(self):
		return self.doneTxt

	def checkEndQuest(self, inventory):
		if self.quest_item in inventory:
			self.hasDone = True
			return True
		else:
			return False

	def startQuest(self):
	
		if self.hasDone != True:
			if self.checkEndQuest(player.pl_inventory.questItems) != True:
				return self.getText()
			else:
				return self.endQuest()
		else:
			return self.getEndText()

class QuestItem(object):
	def __init__(self, name, info):
		self.name = name
		self.info = info

azeitona = QuestItem("Azeitona", "Uma azeitona encontrada em empadas.")
chapeuFalante = QuestItem("Chapéu Falante", "Um chapéu tagarela safado que quer testar seu conhecimento de Geografia.")

import menu
from items import itemManager
import player

# -- Quests --
# Quest(name, item, reward, firstEncounter, afterFirstEncounter, acceptText, rejectText, afterReject, endTxt, doneTxt, playerChoices)

q1 = Quest("A Azeitona da Empada", azeitona, itemManager.getItemByName("Lesser Healing Potion"),
	"""
	Você! Você tem que me ajudar! Tenho certeza que você pode me ajudar!
	Entre na minha loja agora! Você não vai acreditar! É SURREAL!
	""",
	"""
	Você ainda não foi lá? Eu quero minha loja de volta! Rápido!
	""",
	"""
	Obrigado! Vou destrancar a porta para você. Tome cuidado!
	""",
	"""
	Como assim?! Mas eu tinha certeza que você me ajudaria! Agora quem vai me ajudar a recuperar minha loja?
	""",
	"""
	Então você decidiu ajudar?
	""",
	"""
	Obrigado, você salvou a minha loja! Eu não sabia que misturar
	metanotiol, dimetil sulfeto e mercaptanas na minha querida empada
	poderia resultar em algo tão assim... estranho.
	""",
	"""
	Gostaria de experimentar a mais nova sensação de empadas da vila?
	É explosivo!
	""",
	[
	"""Ok... sempre estou preparado para qualquer coisa.""",
	"""Tá doido? Você parece apavorado. Esse surreal não parece significar boa coisa."""
	])

q2 = Quest("A Lenda do Chapéu Falante", chapeuFalante, itemManager.getItemByName("Poção do Conhecimento"),
	"""
	Hey, stranger! Você já ouviu falar na Lenda do Chapéu Falante?
	Dizem que ele é capaz de te dar conhecimento INFINITO!
	Como eu sou um benfeitor, ofereço-te este mapa que te guiará até
	os cafund... quer dizer, até o ÚNICO Chapéu Falante.
	""",
	"""
	Vo-Você aqui? Não esperava te ver tão cedo. Já achou o Chapéu?
	""",
	"""
	Certo. Aqui está o mapa. E cuidado para não se perder no caminho!
	""",
	"""
	Você acha que eu te enganaria assim?! Eu sou um BEMfeitor!
	""",
	"""
	Ah, então ainda está interessado no maravilhoso Chapéu Falante?
	""",
	"""
	Não, não. Tire esse Chapéu de perto de mim! Fique com ele!
	Não era para você trazê-lo aqui! Você nos destruirá! *corre*
	""",
	"""
	AAAHHHHH!!!!
	""",
	[
	"""Um pouco suspeito, mas vou ficar com o mapa.""",
	"""Parece bom de mais para ser verdade. Fique com o seu mapa e sua lenda."""
	])

allQuests = [q1, q2]
questItems = [azeitona, chapeuFalante]
