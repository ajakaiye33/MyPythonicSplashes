

def consonant_vowel_game():
    while True:
        the_quest = input("Type a word and I will tell if it's a vowel or consonant (quit-to end) >")
        if the_quest == "quit":
            break
        elif the_quest[0] in "AEIOU":
            print(the_quest + " Is a vowel!")
        elif the_quest[0] in "BCDFGHJKLMNPQRSTVWXYZ":
            print(the_quest + " Is a consonant!")
        else:
            print(the_quest + "Is not a word!")
    print("Bye")
consonant_vowel_game()





