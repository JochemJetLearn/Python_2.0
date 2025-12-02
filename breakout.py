import turtle, random

screen = turtle.Screen()
screen.setup(625, 625)
canvas = turtle.getcanvas()

bounce = False
boxes = []

def place_boxes():
    colors = ["red", "orange", "yellow", "blue", "green"]
    for i in range(5):
        for j in range(-250, 250, 100):
            box = turtle.Turtle()
            box.speed(0)
            box.shape("square")
            box.color(colors[i])
            box.up()
            box.goto(j+25, (-i+6)*40)
            boxes.append(box)

def left():
    if player.xcor() > -250:
        player.goto(player.xcor()-25, -250)

def right():
    if player.xcor() < 250:
        player.goto(player.xcor()+25, -250)

def setpoints():
    global points
    while True:
        try:
            points = int(input("Please enter points wanted:\n"))
            break
        except:
            print("I'm bad at letters")
    print("Your points: " + str(points))

def deletebox(box):
    box.hideturtle()
    boxes.remove(box)

def delbox(box):
    box.onclick(lambda x, y: deletebox(box))

def deleteboxon():
    print("prepating for box deletion...")
    for i in boxes:
        delbox(i)
    print("Click on a box to delete it!")

def start():
    global bounce
    if not bounce:
        bounce = True

def startgame():
    global bounce, points
    points = 0
    bounce = False
    
    screen.onkey(start, "w")
    balldirection = [0, 0]
    while True:
        for i in boxes:
            if ball.distance(i) < 20:
                i.hideturtle()
                boxes.remove(i)
                balldirection[1] = -3.5
                points += 1

        if bounce:
            bounce = False
            balldirection = [3.5, -3.5]

        ball.goto(ball.xcor()+balldirection[0], ball.ycor()+balldirection[1])

        if player.distance(ball) <= 60:
            balldirection[1] = 3.5

        if ball.xcor() >= 250:
            balldirection[0] = -3.5
        if ball.xcor() <= -250:
            balldirection[0] = 3.5

        if ball.ycor() < -250:
            ball.goto(random.randint(-150, 150), 0)
            balldirection[1] = -3.5
            points -= 1
            balldirection = [0, 0]

        if ball.ycor() > 250:
            break

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.up()
ball.color("red")
ball.goto(random.randint(-150, 150), 0)

balldirection = [0, 0]

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.up()
player.goto(0, -250)

place_boxes()

screen.listen()
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkey(start, "w")
screen.onkey(setpoints, "F1")
screen.onkey(deleteboxon, "F2")

startgame()

print("You win! Points: " + str(points))