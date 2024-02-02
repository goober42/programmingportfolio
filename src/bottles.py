def sing(b):
  if (b == 1):
    objects = 'bottle'
    objectsMinusOne = 'bottles'
  elif (b == 2):
    objects = 'bottles'
    objectsMinusOne = 'bottle'
  else:
    objects = 'bottles'
    objectsMinusOne = 'bottles'

  if (b > 0):
    print(str(b) + " " + objects + " of rum on the wall, " + str(b) + " " + objects + " of rum.")
    print("Take one down and pass it around, " + str(b-1) + " " + objectsMinusOne + " of rum on the wall.")
    print(" ")
  elif (b == 0):
    print("No more bottles of rum on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of rum on the wall.")
  else:
    print("Error: Wheres the booze?")
beer = 99

while beer >= 0:
  sing(beer)
  beer -= 1