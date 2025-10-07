import random

words = ["open", "enter", "hydroneer", "programming", "netherlands", "super", "high", "snake", "python", "java", "coding", "script"]

word = list(random.choice(words))
guessed = []
for i in word:
    guessed.append("_")
while True:
    print(guessed)
    letter = input("What letter do you choose ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        print("Wrong guess, try again")
    if word == guessed:
        print("Congrats, you win")
        break
print(f"you win, stats:\n -correct: {stats[0]}\n -incorrect: {stats[1]}")
