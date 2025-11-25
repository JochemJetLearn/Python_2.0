import turtle, random

screen = turtle.Screen()
screen.setup(600, 600)

boxes = []

def place_boxes():
    colors = ["red", "orange", "yellow", "blue", "green"]
    for i in range(5):
        for j in [-250, -125, 0, 125, 250]:
            box = turtle.Turtle()
            box.speed(0)
            box.shape("square")
            box.color(colors[i])
            box.up()
            box.goto(j, (-i+6)*40)
            boxes.append(box)

def left():
    if player.xcor() > -250:
        player.goto(player.xcor()-25, -250)

def right():
    if player.xcor() < 250:
        player.goto(player.xcor()+25, -250)

def startgame():
    points = 0
    while True:
        for i in boxes:
            if ball.distance(i) < 20:
                i.hideturtle()
                boxes.remove(i)
                balldirection[1] = -10
                points += 1

        ball.goto(ball.xcor()+balldirection[0], ball.ycor()+balldirection[1])

        if player.distance(ball) <= 20:
            balldirection[1] = 10

        if ball.xcor() >= 250:
            balldirection[0] = -10
        if ball.xcor() <= -250:
            balldirection[0] = 10

        if ball.ycor() < -250:
            ball.goto(random.randint(-150, 150), 0)
            balldirection[1] = -10
            points -= 1
        if ball.ycor() > 250:
            print(points)
            break

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.up()
ball.color("red")
ball.goto(random.randint(-150, 150), 0)

balldirection = [10, -10]

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.up()
player.goto(0, -250)

place_boxes()

screen.listen()
screen.onkey(left, "a")
screen.onkey(right, "d")

startgame()

screen.mainloop()