# python2
# coding: utf-8

import player
import console

def run(args=None):
	if args is "debug":
		player.debugMode()
	else:
		player.class_choice()
		
	for i in range(player.pl.startWith):
		player.pl.getNewSpell()

	import rooms
	import menu
	next = rooms.sala_do_acordar.story()

	while True:
		room = next.story()
		next = room.story()
		
run("debug")

