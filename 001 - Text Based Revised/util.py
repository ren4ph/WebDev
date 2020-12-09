import sys, time, os, math, random

global enemyNames
global bossNames
enemyNames = ("Lemurian", "Beetle", "Lesser Wisp", "Greater Wisp",
			  "Stone Golem", "Jellyfish", "Mini Mushroom", "Brass Contraption",
			  "Imp", "Hermit Crab", "Clay Templar", "Alloy Vulture",
			  "Beetle Guard")
bossNames = ("Elder Lemurian", "Parent", "Void Reaver", "Stone Titan",
			 "Clay Dunestrider", "Beetle Queen", "Scavenger",
			 "Wandering Vagrant", "Imp Overlord")


def rng(min, max):
	return random.randrange(min, max + 1)


def rngFlt(min, max, round):
	return round(random.uniform(min, max), round)


def delay_print(string="ERROR: EMPTY", delay=0.07):
	for char in str(string):
		sys.stdout.write(char[0])
		sys.stdout.flush()
		time.sleep(delay)
