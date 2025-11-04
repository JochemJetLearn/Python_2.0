import turtle, random

balloons = []
colors = ["white", "blue", "black", "pink", "orange", "grey", "green"]

def newballoon():
    balloon = turtle.Turtle()
    balloon.speed(0)
    balloon.up()
    balloon.shape("circle")
    balloon.color(random.choice(colors))
    balloon.goto(random.randint(-225, 225), 225)
    balloons.append(balloon)

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightblue")
dart = turtle.Turtle()
dart.speed(0)
dart.up()
dart.color("red")
dart.shape("triangle")
dart.left(90)
dart.goto(0, -225)

newballoon()
score = 0
while True:
    if balloon.ycor() < -210:
        if dart.distance(balloon) < 20:
            score += 
        balloon.hideturtle()
        newballoon()
    else:
        balloon.goto(balloon.xcor(), balloon.ycor() - 10)
