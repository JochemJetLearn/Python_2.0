num = int(input("Enter a number: "))
factors = []

for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)
length = len(factors)
print("{} has {} factor(s)".format(num,length))
for i in factors:
    print(i)
if length == 2:
    print("This is a prime number!")
elif length > 2:
    print("This is a Composite number!")
else:
    print("This number is neither a composite nor prime number! (1)")