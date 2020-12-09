import random, math, items
from util import delay_print


class Player():
  def __init__(self, name, charType1):
    self.gold = 0
    self.level = 1
    self.name = name
    self.charType = charType1
    self.charSheet = self.__charSheetCreat()
    self.inventory = []
    self.baseStats = self.charSheet
    self._critChance = 0.00
    self._healOnCrit = 0.01
    self.currentHealth = 0
    self._damageRed = 0
    self._infusKills = 0
    self._runChance = 0.05

  def returnDamage(self):
    crit = random.random()
    if self.critChance >= crit:

      self.heal(0, round(self.healOnCrit * self.charSheet['bHp']))

      self.heal(self.charSheet['regen'], 0)

      return self.charSheet['bDmg'] * 2
    else:

      self.heal(self.charSheet['regen'], 0)

      return self.charSheet['bDmg']

  def heal(self, amount, percAmount):
    if items.A4stack:
      if items.A4stack == 1:
        if items.A2stack:
          if items.A2stack == 1:
            if amount:
              self.currentHealth += (amount * 2)
            elif percAmount:
              self.currentHealth += (math.ceil(
                percAmount * self.currentHealth)) * 2
            if self.currentHealth > self.charSheet['bHp'] * 2:
              self.currentHealth = self.charSheet['bHp']
          else:
            if amelay_ount:
              self.currentHealth += (
                amount * (pow(2, items.A2stack + 1)))
            elif percAmount:
              self.currentHealth += (math.ceil(
                percAmount * self.currentHealth)) * (pow(
                  2, items.A2stack + 1))
            if self.currentHealth > self.charSheet['bHp'] * 2:
              self.currentHealth = self.charSheet['bHp']
        else:
          if amount:
            self.currentHealth += (amount)
          elif percAmount:
            self.currentHealth += (math.ceil(
              percAmount * self.currentHealth))
          if self.currentHealth > self.charSheet['bHp'] * 2:
            self.currentHealth = self.charSheet['bHp']
      else:
        if items.A2stack:
          if items.A2stack == 1:
            if amount:
              self.currentHealth += (amount * 2)
            elif percAmount:
              self.currentHealth += (math.ceil(
                percAmount * self.currentHealth)) * 2
            if self.currentHealth > self.charSheet['bHp'] * (pow(
                2, items.A4stack)):
              self.currentHealth = self.charSheet['bHp']
          else:
            if amount:
              self.currentHealth += (
                amount * (pow(2, items.A2stack + 1)))
            elif percAmount:
              self.currentHealth += (math.ceil(
                percAmount * self.currentHealth)) * (pow(
                  2, items.A2stack + 1))
          if self.currentHealth > self.charSheet['bHp'] * (pow(
              2, items.A4stack)):
            self.currentHealth = self.charSheet['bHp']
        else:
          if amount:
            self.currentHealth += (amount)
          elif percAmount:
            self.currentHealth += (math.ceil(
              percAmount * self.currentHealth))
          if self.currentHealth > self.charSheet['bHp']:
            self.currentHealth = self.charSheet['bHp']
    else:
      if items.A2stack:
        if amount:
          self.currentHealth += (
            amount * (pow(2, items.A2stack + 1)))
      elif percAmount:
        self.currentHealth += (math.ceil(
          percAmount * self.currentHealth)) * (pow(
            2, items.A2stack + 1))
      else:
        if amount:
          self.currentHealth += amount
        elif percAmount:
          self.currentHealth += (math.ceil(
            percAmount * self.currentHealth))
        if self.currentHealth >= self.charSheet['bHp']:
          self.currentHealth = self.charSheet['bHp']

  def useItem(self, item):
    if item['code'] == "A0":
      items.A0stack += 1
      self.critChance += 0.1
    elif item['code'] == "A1":
      items.A1stack += 1
      self.critChance += 0.05
      if items.A1stack > 0:
        self.healOnCrit *= 1.08
      else:
        self.healOnCrit *= 1.16
    elif item['code'] == "A2":
      items.A2stack += 1
    elif item['code'] == "A3":
      items.A3stack += 1
      self.charSheet['bSpd'] += round(
        1 - (1 / ((0.15 * (items.A3stack)) + 1)), 2)
    elif item['code'] == "A4":
      items.A4stack += 1
    elif item['code'] == "A5":
      items.A5stack += 1
      if items.A5stack > 0:
        self.damageRed += 1
      else:
        self.healOnCrit += 2
    elif item['code'] == "A6":
      items.A6stack += 1
      self.infusKills += 10
    elif item['code'] == "A7":
      items.A7stack += 1
      self.charSheet['numAtt'] += 1
    elif item['code'] == "A8":
      items.A8stack += 1
    elif item['code'] == "A9":
      items.A9stack += 1
      self.charSheet['bHp'] *= 2
    elif item['code'] == "B1":
      items.B0stack += 1
      if items.B0stack == 1:
        self.charSheet['bHp'] += 5
      else:
        self.charSheet['bHp'] += 2
    elif item['code'] == "B2":
      items.B1stack += 1
      self.charSheet['bDmg'] *= 4
      self.charSheet['bHp'] *= 0.01
    elif item['code'] == "B3":
      for i in range(0, len(self.inventory)):
        try:
          if self.inventory[i]['code'] == "B3":
            continue
          else:
            self.useItem(self.inventory[i])
            invn = []
            invn.append(self.inventory[i])
        except:
          continue
      self.charSheet['bHp'] /= 2
      for i in range(0, len(invn)):
        self.inventory.append(invn[i])
      items.B2stack += 1
    elif item['code'] == "B4":
      self.charSheet['regen'] *= 4
      self.charSheet['bHp'] *= 2

  def __charSheetCreat(self):
    if self.charType == "mage":
      delay_print("\n\tMages hit hard, but slowly.")
      input("\t\t(Press Enter to continue): ")

      return {
        'bHp': 28,
        'bDmg': 47,
        'bSpd': 0.18,
        'numAtt': 1,
        'regen': 2
      }

    elif self.charType == "barbarian":
      delay_print("\n\tBarbarians are heavy and strong.")
      input("\t\t(Press Enter to continue): ")

      return {
        'bHp': 36,
        'bDmg': 20,
        'bSpd': 0.1,
        'numAtt': 2,
        'regen': 3
      }

    elif self.charType == "theif":
      delay_print("\n\tThe life of a thief is swift and light. ")
      input("\t\t(Press Enter to continue): ")

      return {
        'bHp': 15,
        'bDmg': 6,
        'bSpd': 0.25,
        'numAtt': 7,
        'regen': 4
      }

  def checkInven(self, itype="short"):

    stackCounts = [
      items.A0stack, items.A1stack, items.A2stack, items.A3stack,
      items.A4stack, items.A5stack, items.A6stack, items.A7stack,
      items.A8stack, items.A9stack, items.B0stack, items.B1stack,
      items.B2stack, items.B3stack
    ]

    if itype.lower() == "long":
      if self.inventory:
        '''print(
        f"\n\tYou have {len(self.inventory)} items, which are as follows:"
        )
        '''
        for item in self.inventory:
          '''
          print(
            f"\n\tYou have a(n) {item['name']}, which is a {item['rarity']} rarity. Here is its' description: {item['description']}"
          )
          '''
      else:
        delay_print("\tYour inventory is empty!")
        input("\t\t(Press enter to continue): ")
    else:
      for i in range(0, len(items.items)):
        '''
        print(
          f"\t\t\tYou have {stackCounts[i]} {items.items[i]['name']}s"
        )
        '''

  def correctStats(self):
    self.charSheet['bHp'] = math.ceil(self.charSheet['bHp'])
    self.charSheet['bDmg'] = math.ceil(self.charSheet['bDmg'])
    self.charSheet['bSpd'] = round(self.charSheet['bSpd'], 2)
