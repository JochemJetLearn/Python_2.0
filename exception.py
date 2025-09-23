while True:
    try:
        x = int(input("Num x: "))
        y = int(input("Num y: "))
        op = input("Operation or QUIT (+|-|*|/): ")
        if op == "+":
            print(x+y)
        elif op == "-":
            print(x-y)
        elif op == "*":
            print(x*y)
        elif op == "/":
            print(x/y)
        elif op == "QUIT":
            break
    except ValueError:
        print("Enter numbers only plz, im bad at letters")
    except ZeroDivisionError:
        print("Dont even try to devide by 0")