import random

words = ["open", "enter", "hydroneer", "programming", "netherlands", "super", "high", "snake", "python", "java", "coding", "script"]

word = list(random.choice(words))
guessed = []
stats = [0,0]
for i in word:
    guessed.append("_")
while True:
    print(guessed)
    letter = input("What letter do you choose ")
    if letter in word:
        stats[0] += 1
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        stats[1] += 1
        print("Wrong guess, try again")
    if word == guessed:
        print("Congrats, you win")
        break
print(f"you win, stats:\n -correct: {stats[0]}\n -incorrect: {stats[1]}")

