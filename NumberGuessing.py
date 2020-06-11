from random import randint

positiveFloorNumber = None
positiveCielingNumber = None
numberOfGuesses = None
guessCounter = None
randomNumber = None
print("Welcome to Alexander's Number Guessing Game!\n")

def getFloor():
  while True:
    positiveFloorNumber = input("Please enter a lower boundary (integer greater than zero and less than one million):")
    try:
      parseDataType = int(positiveFloorNumber)
      if parseDataType > 0 and parseDataType < 1000000 :
        break
      print("The lower boundary that you entered is out of range!")
    except ValueError:
      print("The lower boundary that you entered is not the correct data type!")
  return int(positiveFloorNumber)

def getCieling(currentPositiveFloor):
  while True:
    positiveCielingNumber = input("Please enter an upper boundary (integer greater than low bound and <= one million):")
    try:
      parseDataType = int(positiveCielingNumber)
      if parseDataType > currentPositiveFloor and parseDataType < 1000000 :
        break
      print("The upper boundary that you entered is out of range!")
    except ValueError:
      print("The upper boundary that you entered is not the correct data type!")
  return int(positiveCielingNumber)

def getNumberOfGuesses():
  while True:
    numberOfGuesses = input("Please enter the number of guesses that should be allowed (positive integer <= 20):")
    try:
      parseDataType = int(numberOfGuesses)
      if parseDataType > 0 and parseDataType <= 20 :
        break
      print("The guesses allowed that you entered is out of range!")
    except ValueError:
      print("The guesses allowed is not the correct data type!")
  return int(numberOfGuesses)

def generateRandomNumberToBeGuessed(currentPositiveFloor, currentPositiveCieling):
  return randint(currentPositiveFloor, currentPositiveCieling)

def gameLoop(guessCounter, currentPositiveFloor, currentPositiveCieling, currentRandomNumber):
  keepTrackOfGuessCounter = guessCounter
  storeCurrentPositiveFloor = currentPositiveFloor
  storeCurrentPositiveCieling = currentPositiveCieling
  storeCurrentRandomNumber = currentRandomNumber
  gameHasEnded = False
  outOfBoundsFlag = False
  while True:
    if outOfBoundsFlag == True :
      outOfBoundsFlag = False
    if gameHasEnded == True :
      while True:
        playAgain = input("Would you like to play again with the same parameters (y/n)?")
        if str(playAgain) == "y" or str(playAgain) == "n":
          break
        print("Please enter y or n")
      if str(playAgain) == "y" :
        storeCurrentRandomNumber = generateRandomNumberToBeGuessed(storeCurrentPositiveFloor, storeCurrentPositiveCieling)
        keepTrackOfGuessCounter = guessCounter
        gameHasEnded = False
      else:
        break
    print("You have " + str(keepTrackOfGuessCounter) + " guesses left.")
    userGuess = input("Please guess an integer from " + str(storeCurrentPositiveFloor)
    + " to " + str(storeCurrentPositiveCieling) + ": ")
    try:
      parseDataType = int(userGuess)
      if parseDataType < storeCurrentPositiveFloor or parseDataType > storeCurrentPositiveCieling :
        print("Your guess was out-of-bounds...try again.")
        outOfBoundsFlag = True
      if parseDataType < storeCurrentRandomNumber and outOfBoundsFlag == False:
        keepTrackOfGuessCounter -= 1
        print("Your guess was too low.")
      if parseDataType > storeCurrentRandomNumber and outOfBoundsFlag == False :
        keepTrackOfGuessCounter -= 1
        print("Your guess was too high.") 
      if parseDataType == storeCurrentRandomNumber and outOfBoundsFlag == False :
        keepTrackOfGuessCounter -= 1
        gameHasEnded = True
        print("Good job...you guessed the chosen number!")
      if keepTrackOfGuessCounter == 0 and gameHasEnded == False :
        print("The chosen number was " + str(storeCurrentRandomNumber) + ".")
        gameHasEnded = True  
    except ValueError:
      print("Your guess is not the correct data type!")
      

currentPositiveFloor = getFloor()
currentPositiveCieling = getCieling(currentPositiveFloor)
currentNumberOfGuesses = getNumberOfGuesses()
currentRandomNumber = generateRandomNumberToBeGuessed(currentPositiveFloor, currentPositiveCieling)
guessCounter = currentNumberOfGuesses
gameLoop(guessCounter, currentPositiveFloor, currentPositiveCieling, currentRandomNumber)
