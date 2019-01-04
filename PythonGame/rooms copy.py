# coding: utf-8

import menu

class Room(object):
		def __init__(self, name, treasure, next, exits, text):
			self.name = name
			self.hasTreasure = treasure
			self.nextRoom = next
			self.text = text
			self.numOfExits = exits

		def story(self):
			print """
			%s
			""" % self.text
			menu.menu(self)

		def walk(self):
			if self.numOfExits == 1:
				self.nextRoom.story()
			else:
				self.options()

		def options(self):
			print "Você tem %d opções." % self.numOfExits

sala_das_quatro_pontes = Room("Sala das Quatro Pontes", True, "sala_norte", 4,
"""
Ontem, fui pra casa
""")

sala_do_acordar = Room("Sala do Acordar", False, sala_das_quatro_pontes, 1,
"""
Era uma noite sombria,
quando ele apareceu
""")

sala_do_acordar.story()

