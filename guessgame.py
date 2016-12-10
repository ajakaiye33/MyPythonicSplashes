import random
def guess_the_number():
   while True:
       turn_the_wheel = str(random.randint(0, 100))
       ask_participant = input("Guess the number between 0 and 100 >")
       if ask_participant == "quit":
           break
       elif ask_participant > turn_the_wheel:
            print(" Not quite! {} is too high, the magic number was {}, try lower".format(ask_participant, turn_the_wheel))
            #return " Not quite! {} is too high, try lower".format(ask_participant)
       elif ask_participant < turn_the_wheel:
            print("Not quite! {} is too low, the magic number was {}, try higher".format(ask_participant, turn_the_wheel))
            #return "Not quite! {} is too low, try higher".format(ask_participant)
       elif ask_participant == turn_the_wheel:
            print("Correct {} is the magical number".format(turn_the_wheel))
            #return "Correct {} is the magical number".format(turn_the_wheel)
       else:
            print("Somethin is wrong with your input!")
            #return "Somethin is wrong with your input!"
   print("Game over")
   #return "Game Over!"

guess_the_number()

