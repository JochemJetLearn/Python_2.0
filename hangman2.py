import random

def hangman():
    words = ["open", "enter", "hydroneer", "programming", "netherlands", "super", "high", "snake", "python", "java", "coding", "script"]
    wordtoguess = random.choice(words)
    guessedword = ["_"] * len(wordtoguess)
    guessletters = []
    stats = [0, 0]
    print("welcome to hangman, you can only type 1 letter at a time")
    print(f"guess word: {guessedword}")
    while "_" in guessedword:
        guess = input("guess a letter: ")
        guessletters.append(guess)
        if guess in wordtoguess:
            stats[0] += 1
            print(f"good guess, the letter {guess} is in the word")
            length = len(wordtoguess)
            for i in range(length):
                if wordtoguess[i] == guess:
                    guessedword[i] = guess
        else:
            stats[1] += 1
            print("wrong guess, try again")
        print(guessedword)
    print("congratulations, you guessed the word")
    print(f"stats:\n -correct letters: {stats[0]}\n -incorrect letters {stats[1]}")

hangman()