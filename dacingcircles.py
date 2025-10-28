import turtle, random, time

while True:
    try:
        rounds = int(input("How many rounds do you want? "))
        break
    except:
        pass

screen = turtle.Screen()
screen.title("Shapes animates")
pen = turtle.Turtle()
screen.bgcolor("black")
pen.speed(0)
colours = ["red", "blue", "cyan", "pink", "orange", "purple", "green"]

def circle(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.hideturtle()

def square(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(100)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()

def triangle(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(100)
        pen.right(120)
    pen.end_fill()
    pen.hideturtle()

def pentagon(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(5):
        pen.forward(100)
        pen.right(72)
    pen.end_fill()
    pen.hideturtle()

def hexagon(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(6):
        pen.forward(100)
        pen.right(60)
    pen.end_fill()
    pen.hideturtle()

def septagon(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(7):
        pen.forward(100)
        pen.right(360/7)
    pen.end_fill()
    pen.hideturtle()

def octagon(speed):
    color = random.choice(colours)
    pen.right(random.randint(0, 360))
    pen.color(color)
    pen.speed(speed)
    pen.up()
    pen.goto(random.randint(-150, 150), random.randint(-150, 150))
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(8):
        pen.forward(100)
        pen.right(45)
    pen.end_fill()
    pen.hideturtle()

shapes = [circle, square, triangle, pentagon, hexagon, septagon, octagon]

starttime = time.time()

for i in range(rounds):
    pen.clear()
    print(f"Shape {i}/{rounds} at {round(time.time() - starttime, 2)}s")
    random.choice(shapes)(i*10)
    time.sleep(2/(i+1))
print(f"Shape {rounds}/{rounds} - Animation complete")

endtime = time.time()

anitime = round(endtime - starttime, 2)
pen.up()
pen.clear()
pen.color("white")
pen.goto(0, 0)
pen.write(f"Total animation time: {anitime} seconds", align="center", font=("arial", 50))

screen.mainloop()