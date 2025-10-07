import random

words = ["open", "enter", "hydroneer", "programming", "netherlands", "super", "high", "snake", "python", "java", "coding", "script"]
print("Welcome to the scramble words!")

def scrable(word):
    letters = list(word)
    random.shuffle(letters)
    result = "".join(letters)
    return result

def game():
    incorrect = [0,0,0,0,0,0]
    round = 0
    while round<5:
        round += 1
        print("Round {}, lets begin".format(round))
        word = random.choice(words)
        scrambled = scrable(word)
        print("scrambled word: {}".format(scrambled))
        while True:
            guess = input("What is original word? ")
            if guess == word:
                print(f"congrats! you have guessed the word, your correct amount of words is {round}")
                break
            else:
                incorrect[round] += 1
                incorrect[0] += 1
            print("Incorrect word. Try again")
    print("You have guessed all the words, you win")
    print(f"stats:\n -total incorrect: {incorrect[0]}\n -incorrect round 1: {incorrect[1]}\n -incorrect round 2: {incorrect[2]}\n -incorrect round 3: {incorrect[3]}\n -incorrect round 4: {incorrect[4]}\n -incorrect round 5: {incorrect[5]}\n -correct words: 5")
game()