import random
def rollDice(sides):
  result = random.randint(1,sides)
  return result
def sidedRolls():
  roll6sideddice = rollDice(6)
  roll8sideddice = rollDice(8)
  health = roll6sideddice * roll8sideddice
  return health
print("CHARACTER STAT GENERATOR")
character = 'yes'
while character == "yes":
  othervariable = input("Name your warrior:")
  health = str(sidedRolls())
  print("Their health is","\033[35m",health,"\033[0m","hp")
  character = input("Want to create another character?")