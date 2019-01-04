
x = random.randint(0, 10000)
itemSelector = []
allItems = items.allItems

if x == 1:
	player.pl_inventory.addWeapon(items.cheaterSword)
elif x > 1 and x <= 6: 
	for item in allItems:
		if item.percentage == 0.05:
			itemSelector.append(item)
		addItem()
elif x > 6 and x <= 16:
	for item in allItems:
		if item.percentage == 0.10:
			itemSelector.append(item)
	addItem()
elif x > 16 and x <= 36:
	for item in allItems:
		if item.percentage == 0.20:
			itemSelector.append(item)
	addItem()
elif x > 36 and x <= 86:
	for item in allItems:
		if item.percentage == 0.50:
			itemSelector.append(item)
	addItem()
elif x > 86 and x <= 186:
	for item in allItems:
		if item.percentage == 1.00:
			itemSelector.append(item)
	addItem()
elif x > 186 and x <= 686:
	for item in allItems:
		if item.percentage == 5.00:
			itemSelector.append(item)
	addItem()
elif x > 686 and x <= 1686:
	for item in allItems:
		if item.percentage == 10.0:
			itemSelector.append(item)
	addItem()
elif x > 1686 and x <= 3186:
	for item in allItems:
		if item.percentage == 15.0:
			itemSelector.append(item)
	addItem()
else:
	print "Você não encontrou nada."

for i in range(len(itemSelector)):
	itemSelector.pop()

def addItem():

	item_toAdd = random.choice(itemSelector)
	if isinstance(item_toAdd, items.Weapon):
		player.pl_inventory.addWeapon(item_toAdd)
	elif isinstance(item_toAdd, items.Armor):
		player.pl_inventory.addArmor(item_toAdd)
	elif isinstance(item_toAdd, items.Potion):
		player.pl_inventory.addPotion(item_toAdd) 
	print "Você pegou: %s" % item_toAdd.name