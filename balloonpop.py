import turtle, random, time

balloons = []
balloonspeed = []
colors = ["white", "blue", "black", "pink", "orange", "grey", "green"]
def color() -> str:
        hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "b", "C", "D", "E", "F"]
        return "#" + random.choice(hex) + random.choice(hex) + random.choice(hex) + random.choice(hex) + random.choice(hex) + random.choice(hex)

def newballoon():
    balloon = turtle.Turtle()
    balloon.speed(0)
    balloon.up()
    balloon.shape("circle")
    balloon.color(random.color())
    balloon.goto(random.randint(-225, 225), 225)
    balloons.append(balloon)
    balloonspeed.append(random.randint(2, 7)/2)

def move(dx):
    dart.goto(dart.xcor()+dx, -225)

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("lightblue")
maxballoons = 15
dart = turtle.Turtle()
dart.speed(0)
dart.up()
dart.color("red")
dart.shape("triangle")
dart.left(90)
dart.goto(0, -225)

screen.listen()
screen.onkeypress(lambda: move(-15), "a")
screen.onkeypress(lambda: move(15), "d")
stats = {
    "hit": 0,
    "miss": 0,
    "total": 0
}
infot = turtle.Turtle()
infot.up()
infot.hideturtle()
infot.goto(-245, 205)
tps = 0
secstart = time.time()
score = 0
while True:
    for i in balloons:
        if i.ycor() < -220:
            if dart.distance(i) < 20:
                score += 2
                print("Balloon hit! (+2)")
                stats["hit"] += 1
            else:
                score -= 1
                print("Missed balloon. (-1)")
                stats["miss"] += 1
            print(f"Score: {score}")
            stats["total"] += 1
            i.hideturtle()
            balloons.remove(i)
        else:
            i.goto(i.xcor(), i.ycor() - balloonspeed[balloons.index(i)]*(len(balloons)/1.5))
    if len(balloons) == 0:
        newballoon()
    elif len(balloons) < maxballoons:
        chance = random.random()
        if chance < 0.02:
            newballoon()
    if score > 9:
        break
    if time.time() - secstart > 1:
        infot.clear()
        infot.write(f"Score: {score}\nTPS: {tps}\nTotal balloons: {len(balloons)}")
        tps = 0
        secstart = time.time()
    else:
        tps += 1
print("You win, stats:")
print(f" Hit balloons: {stats["hit"]}\n Missed balloons: {stats["miss"]}\n Total balloons: {stats["total"]}")