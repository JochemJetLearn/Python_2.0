import random

grid = []
def griddisign(x, y):
    for r in range(x):
        row = []
        for c in range(y):
            row.append("__")
        grid.append(row)
    return grid

def placetreasure(x, y):
    row = random.randint(0, y-1)
    col = random.randint(0, x-1)
    return row, col

def give_hint(gx, gy, tx, ty):
    if gy < ty:
        return "Move down"
    elif gy > ty:
        return "Move up"
    elif gx < tx:
        return "Move right"
    elif gx > tx:
        return "Move left"
    else:
        return "Congatulations! You have found the treasure! We're rich!"
    
def treasure_hunt():
    grid = griddisign(5, 5)
    ty, tx = placetreasure(5, 5)
    print("There is a treasure hidden here... Find it and you're RICH!")
    while True:
        for r in grid:
            print(" ".join(r))
        gy = int(input("Enter row number (0-4): "))
        gx = int(input("Enter col number (0-4): "))
        if (gx == tx) and (gy == ty):
            print("Congatulations! You have found the treasure! We're rich!")
            break
        else:
            hint = give_hint(gx, gy, tx, ty)
            print(hint)
        
treasure_hunt()