import random, os, time

word = list(input("1 player must enter a secret word "))
time.sleep(2.5)
os.system("clear")
guessed = ["_"] * len(word)
stats = [0,0]
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
