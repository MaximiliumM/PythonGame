# coding: utf-8

# --- Party System ---
# Party members can be a Player object or a Monster object

class Party(object):
	def __init__(self, members, type):
		from inventory import PartyInventory
		
		self.type = type
		self.maxMembers = 3
		self.members = members
		self.offMembers = []
		self.faintedMembers = []
		
		# -- Party Inventory --
		self.inventory = PartyInventory(self.type)
		
	
	def changeParty(self):
		print "\t*** Party Atual ***\n"
		
		members = ""
		
		for member in self.members:
			if member in self.faintedMembers:
				members += "- %s *DESMAIADO*\n"
			else:
				members += "- %s\n" % member.name
			
		print "O que você quer fazer?"
		print "1. Adicionar"
		print "2. Remover"
		print "3. Voltar"
		
		choice = raw_input("> ")
		
		if choice == "1":
			self.addMember(self)
		elif choice == "2":
			self.removeMember(self)
		elif choice == "3":
			return
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			self.changeParty()
			
	def addMember(self):
		print "\t*** Membros Guardados ***\n"
		
		members = ""
		count = 1
		
		for member in self.offMembers:
			members += "%d. %s\n" % (count, member.name)
			count += 1
			
		print "%s%d. Voltar\n" % (spells, count)
		print "Escolha qual membro você quer adicionar.\n"
		
		choice = raw_input("> ")
		
		if choice.isdigit():
			choice = int(choice) - 1

		if choice < len(player.pl.class_spells) and choice >= 0:
			self.members.append(self.offMembers.pop(choice))
			self.changeParty(self)
		elif choice == len(player.pl.class_spells):
			return
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			self.addMember()()
	
	def removeMember(self):
		print "\t*** Party Atual ***\n"
		
		members = ""
		count = 1

		for member in self.members:
			members += "%d. %s\n" % (count, member.name)
			count += 1

		print "%s%d. Voltar\n" % (spells, count)
		print "Escolha qual membro você quer remover.\n"

		choice = raw_input("> ")
		
		if choice.isdigit():
			choice = int(choice) - 1

		if choice < len(player.pl.class_spells) and choice >= 0:
			self.offMembers.append(self.members.pop(choice))
			self.changeParty(self)
		elif choice == len(player.pl.class_spells):
			return
		else:
			print "\t*** Escolha um dos números do menu ***\n"
			self.removeMember()
			

# This is the player party			
pl_party = Party([], "player")
