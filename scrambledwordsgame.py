import random

words = ["open", "enter", "hydroneer", "programming", "netherlands", "super", "high", "snake", "python", "java", "coding", "script"]
print("Welcome to the scramble words!")

def scrable(word):
    letters = list(word)
    random.shuffle(letters)
    result = "".join(letters)
    return result

def game():
    word = random.choice(words)
    scrambled = scrable(word)
    print("scrambled word: {}".format(scrambled))
    while True:
        guess = input("What is original word? ")
        if guess == word:
            print("congrats! you have guessed the word")
            break
        print("Incorrect word. Try again")

game()