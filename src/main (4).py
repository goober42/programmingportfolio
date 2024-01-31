import random

play = False

win = False

attempts = 0

money = 0

num = random.randrange(1, 100)

print("Welcome to the Number Guessing Game!")
print("type ""start"" to start")
start = input("")
if(start == "start"):
  play = True

if(play == True):

  print("I am thinking of a number between 1 and 100")
  print("You have 10 guesses")
  for i in range(10):
    guess = int(input("What is your guess? "))
    if guess == num:
      print("Correct!")
      print("You correctly guessed the number in " + str(attempts) + " attempts")
      money += (100 - (attempts * 10))
      print("you have " + str(money) + " dollars")
      win = True
      if(win):
        num = random.randrange(1, 100)
        attempts = 0
    elif guess > num:
      print("Too high")
      attempts += 1
    else:
      print("Too low")
      attempts += 1
if win and money >= 100:
  print("would you like to buy an upgrade")
  upgrade = input("")
  if(upgrade == "yes"):
    print("Which upgrade would you like to buy?")
    print("1: 5 more guesses per game")
    print("2: Number limit increased to 200(for a more challenging game)")
    print("3: Number limit increased to 500(for a more challenging game)")
    print("please enter the number of the upgrade you would like to buy")
    number = input("")
    if(number == 1):
      money -=100
      i+=5
      print("you bought more guesses")
    if(input == 2):
      num = random.randrange(1,200)
      money -=100
      print("this seems fun")
    if(input == 3):
      num = random.randrange(1,500)
      money -=100
      print("good luck")
    print("enter leave to begin playing the game again")
    if(input == "leave"):
      play = True
  if(input == "no"):
    print("okay")
    print("would you like to play again?")
    if(input == "yes"):
      play = True

