import random, math, sys, time, os

global A0stack, A1stack, A2stack, A3stack, A4stack, A5stack, A6stack, A7stack, A8stack, A9stack, B0stack, B1stack, B2stack, B3stack
A0stack = 0
A1stack = 0
A2stack = 0
A3stack = 0
A4stack = 0
A5stack = 0
A6stack = 0
A7stack = 0
A8stack = 0
A9stack = 0
B0stack = 0
B1stack = 0
B2stack = 0
B3stack = 0

A0 = {
	"name":
	"Lens-Makers Glasses",
	"rarity":
	"Common",
	"description":
	"Add 10%(+10% per stack, linear) chance to critically strike, dealing double damage.",
	'code':
	"A0"
}
A1 = {
	"name":
	"Harvesters' Scythe",
	"rarity":
	"Rare",
	"description":
	"Adds 5%(+5% per stack, linear) chance to critically strike, and heal 16%(+8% per stack, linear) of your max health on critical strike.",
	'code':
	"A1"
}
A2 = {
	"name":
	"Rejuvination Rack",
	"rarity":
	"Legendary",
	"description":
	"Doubles healing(Times two per stack, exponential) from all sources.",
	'code':
	"A2"
}
A3 = {
	"name": "Teddy Bear",
	"rarity": "Common",
	"description":
	"Increases dodge chance by 15%(+10% per stack, logarithmic)",
	'code': "A3"
}
A4 = {
	"name":
	"Aegis",
	"rarity":
	"Legendary",
	"description":
	"Allows overhealing up to two times(Times two per stack, exponential) health",
	'code':
	"A4"
}
A5 = {
	"name": "Armor Plating",
	"rarity": "Common",
	"description": "Flat Damage Reduction of 2(+1 per stack, linear) damage",
	'code': "A5"
}
A6 = {
	"name":
	"Infusion",
	"rarity":
	"Rare",
	"description":
	"Increases health by 1 per kill, up to 10(+10 per stack) health.",
	'code':
	"A6"
}
A7 = {
	"name": "Soldiers Syringe",
	"rarity": "Common",
	"description": "Increase number of attacks by 1(+1 per stack, linear).",
	'code': "A7"
}
A8 = {
	"name":
	"Monster Tooth",
	"rarity":
	"Common",
	"description":
	"Heal for 1(+1 per stack, linear) health every time you kill an enemy",
	'code':
	"A8"
}
A9 = {
	"name": "Dip Styx",
	"rarity": "Legendary",
	"description": "Doubles current base health.",
	'code': "A9"
}
B0 = {
	"name": "Ace Bandage",
	"rarity": "Rare",
	"description": "Adds 5(+2 per stack, linear) base health.",
	'code': "B0"
}
B1 = {
	"name":
	"Shaped Glass",
	"rarity":
	"Lunar",
	"description":
	"Quadruples current base damage, but resets base health to 1% of its current value.",
	'code':
	"B1"
}
B2 = {
	"name": "Long Toss",
	"rarity": "Lunar",
	"description":
	"Doubles current item counts, but halves current base damage.",
	'code': "B2"
}
B3 = {
	"name": "Titanic Knurl",
	"rarity": "Boss",
	"description": "Quadruples current regen, doubles base health.",
	'code': "B3"
}
global itemDict
global items
itemDict = {
	"A0": A0,
	"A1": A1,
	"A2": A2,
	"A3": A3,
	"A4": A4,
	"A5": A5,
	"A6": A6,
	"A7": A7,
	"A8": A8,
	"A9": A9,
	"B0": B0,
	"B1": B1,
	"B2": B2,
	"B3": B3
}
items = [A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, B0, B1, B2, B3]


def itemRollBasic():
	itemWeights = []
	for item in itemDict:
		if itemDict[item]['rarity'] == "Common":
			itemWeights.append(66)

		elif itemDict[item]['rarity'] == "Rare":
			itemWeights.append(30)

		elif itemDict[item]['rarity'] == "Legendary":
			itemWeights.append(4)
		else:
			itemWeights.append(0)
	temp = random.choices(items, weights=itemWeights, cum_weights=None, k=1)
	rolledItem = temp[0]

	return rolledItem


def itemRollLarge():
	itemWeights = []
	for item in itemDict:
		if itemDict[item]['rarity'] == "Common":
			itemWeights.append(4)

		elif itemDict[item]['rarity'] == "Rare":
			itemWeights.append(66)

		elif itemDict[item]['rarity'] == "Legendary":
			itemWeights.append(30)
		else:
			itemWeights.append(0)

	temp = random.choices(items, weights=itemWeights, cum_weights=None, k=1)
	rolledItem = temp[0]

	return rolledItem


def itemRollLegen():
	itemWeights = []
	for item in itemDict:
		if itemDict[item]['rarity'] == "Common":
			itemWeights.append(1)

		elif itemDict[item]['rarity'] == "Rare":
			itemWeights.append(4)

		elif itemDict[item]['rarity'] == "Legendary":
			itemWeights.append(95)

		else:
			itemWeights.append(0)

	temp = random.choices(items, weights=itemWeights, cum_weights=None, k=1)
	rolledItem = temp[0]

	return rolledItem


def itemRollLunar():
	itemWeights = []
	for item in itemDict:
		if itemDict[item]['rarity'] == "Common":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Rare":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Legendary":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Lunar":
			itemWeights.append(100)

		else:
			itemWeights.append(0)

	temp = random.choices(items, weights=itemWeights, cum_weights=None, k=1)
	rolledItem = temp[0]

	return rolledItem


def itemRollBoss():
	itemWeights = []
	for item in itemDict:
		if itemDict[item]['rarity'] == "Common":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Rare":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Legendary":
			itemWeights.append(0)

		elif itemDict[item]['rarity'] == "Lunar":
			itemWeights.append(0)

		else:
			itemWeights.append(100)

	temp = random.choices(items, weights=itemWeights, cum_weights=None, k=1)
	rolledItem = temp[0]

	return rolledItem
