# coding: utf-8

import menu
import battle
import monsters
import npcs

class Room(object):
	def __init__(self, name, treasure):
		self.name = name
		self.hasTreasure = treasure
		self.done = False

class Sala_acordar(Room):

	def story(self):
		if self.done == False:
			print """
	Você acorda com uma dor forte na cabeça.
	"O que aconteceu?" - pergunta pra si.
	A última coisa que você se lembra era de estar brincando com seus
	pássaros raivosos no espelho encantado.
	Mas o que aconteceu?
	"""
			return menu.menu(self)
		else:
			return menu.menu(self)

	def walk(self):
		if self.done == False:
			print """
	A sala é quadrada e só tem uma saída.
	Aparentemente é um corredor comprido que leva direto a uma outra sala.
	Enquanto caminhava com cuidado, sem saber o que te esperava,
	você vê algo brilhando perto da parede.
	"""

			choice = raw_input("1. Verificar\n2. Ignorar\n> ")
		
			if choice == "1":
				menu.search(True)
				self.done = True
				return sala_das_quatro_pontes
			elif choice == "2":
				self.done = True
				return sala_das_quatro_pontes
			else:
				print "\t*** Escolha um dos números do menu ***\n"
				return self.walk()
		else:
			return sala_das_quatro_pontes

class Sala_4_pontes(Room):
	def story(self):
		if self.done == False:
			self.done = True
			print """
	Você continua pelo corredor.
	Mais próximo da sala, você sente um fedor estranho.
	A sala, iluminada por duas tochas, não parecia muito grande.
	Mas havia algo estranho ali. Algo vivo. Seria outra pessoa?
	"""
			raw_input("Pressione ENTER para continuar.")


			print """
	Ao entrar, você vê quatro pontes de madeira
	que se ligam ao centro da sala.
	Embaixo de tudo, há uma gosma negra, borbulhando.
	Seu estômago embrulhado não te deixa perceber que algo se aproxima.
	"""
	
			raw_input("Pressione ENTER para continuar.")

			print """
	Uma sombra cobre sua visão e te joga para o meio da sala.
	Tirando a espada da bainha, você finalmente vê,
	mas ainda não consegue definir.
	Sombra, gosma? Será que é possível acertar algo assim?
	"""	

			raw_input("Pressione ENTER para continuar.")

			battle.attack(monsters.empada)
			
			battle.endBattle(monsters.empada)

			print """
	Cansado, você levanta os olhos e olha para a forma desforma
	no chão. Você ainda não entende o que era aquilo.
	Não importa. Agora está morto.
	"""

			return menu.menu(self)
		else:
			return menu.menu(self)

	def walk(self):
		print """
		1. Ponte Norte
		2. Ponte Sul
		3. Ponte Oeste
		4. Ponte Leste
		"""

		choice = raw_input("> ")

		if choice == "1":
			return sala_norte
		elif choice == "2":
			return sala_do_acordar
		elif choice == "3":
			return sala_oeste
		elif choice == "4":
			return sala_leste
		else:
			print "\t*** Escolha um dos números do menu ***\n"


sala_do_acordar = Sala_acordar("Sala do Acordar", True)
sala_das_quatro_pontes = Sala_4_pontes("Sala das Quatro Pontes", True)


