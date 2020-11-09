# python2
# coding: utf-8

import inventory
import party
import player
import items
import menu
import monsters
import npcs
import quests
import rooms
import shop
import spells
import console

def run(args=None):
	if args is "debug":
		player.debugMode()
	else:
		player.class_choice()
		
	for i in range(player.pl.startWith):
		player.pl.getNewSpell()

	next = rooms.sala_do_acordar.story()

	while True:
		room = next.story()
		next = room.story()
		
run("debug")

