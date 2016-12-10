import random
print('-----------------------------')
print(  'GUESS THE NUMBER APP')
print('-----------------------------')
print('')
def guessTheNumGame():
    while True:
        randomGenerator = random.randint(0, 100)
        guessInput = input('Guess a number between 0 and 100 >')
        guessInt = int(guessInput)
        if guessInt == randomGenerator:
            break
        elif guessInt > randomGenerator:
            print(str(guessInt) + ' Is too high, try something lower')
        elif guessInt < randomGenerator and randomGenerator != 0:
            print(str(guessInt) + ' Is too low, try something higher')
    print('Great! ' + str(guessInt) + ' Is it!' + '\n' + 'Game over!')
guessTheNumGame()


