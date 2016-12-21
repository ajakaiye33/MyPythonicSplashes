# The function will accept arguement in string and output the number of vowels therein

def no_vowels(string):
    the_vowels = "aeiou"
    string = string.lower()
    # return the sum of the interation
    return sum(letters in the_vowels for letters in string)
print(no_vowels("yankees"))



