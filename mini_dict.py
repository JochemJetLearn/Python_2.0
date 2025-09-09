dictionary = {}

while True:
    print("\nMini Dictionary App")
    print("1. Add/Update a word")
    print("2. Retrieve a word's definition")
    print("3. Delete a word")
    print("4. View all words")
    print("5. Exit")

    try:
        choice = int(input("Choose an option (1-5): "))
        print()
        if choice == 1:
            word = input("What word do you want to add/update? ").lower()
            meaning = input("What is the meaning of this word? ").lower()
            dictionary[word] = meaning
            print("Word '{}' added/updated successfully!".format(word))
        elif choice == 2:
            word = input("What word do you want to know? ").lower()
            if word in dictionary:
                print("The definition of {} is: \n{}".format(word,dictionary[word]))
            else:
                print("Word not in dictionary. Add a word with 1")
        # elif choice == 3:
        #     word = input("What word do you want to delete? ")
        #     if word in dictionary:
        #         confirm = input("Are you sure you want to delete {}, with meaning: \n{}\n(y/n): ".format(word,dictionary[word]))
        #         if confirm == "y":
        #             del(dictionary,word)
        #             print("Word '{}'deleted successfully!".format(word))
        #         else:
        #             print("stopped deleting {} from dictionary".format(word))
        #     else:
        #         print("Word not in dictionary.")

        elif choice == 3:
            word = input("What word do you want to delete? ").lower()
            if word in dictionary:
                del dictionary[word]
                print("Word '{}'deleted successfully!".format(word))
            else:
                print("Word '{}' does not exist in dictionary".format(word))


        elif choice == 4:
            if dictionary:
                print("\nWords in the dictionary:")
                for word in dictionary:
                    print("{}: {}".format(word, dictionary[word]))
            else:
                print("The dictionary is empty.")
        #elif choice == 4:
        #    print("full dictionary:")
        #    for i in dictionary:
        #        print("\n{}:\n{}".format(i,dictionary[i]))
        elif choice == 5:
            break
        else:
            print("Please choose a number between 1 and 5.")
    except ValueError:
        print("An error! :o\nSome things can't be converted to other things in this world. :O")

print("Exited out of application")


# Write a python program to check the factors of a given number