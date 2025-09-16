file = open("itismeyesbcyez.txt","w")
file.write("Yes, i am him the person\n\nyes\ni know its crazy")
file.close()

file = open("itismeyesbcyez.txt","r")
print(file.read())
file.close()

file = open("itismeyesbcyez.txt","a")
file.write("\nedit: I don't to autographs")
file.close()

with open("itismeyesbcyez.txt","r") as file:
    print(file.read())