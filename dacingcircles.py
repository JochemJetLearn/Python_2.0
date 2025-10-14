import turtle, random, time

screen = turtle.Screen()
pen = turtle.Turtle()
screen.bgcolor("black")
pen.speed(0)
colours = ["red", "blue", "cyan", "pink", "orange", "purple", "green"]

def circle(speed):
    color = random.choice(colours)
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

starttime = time.time()

for i in range(50):
    pen.clear()
    circle(i*10)
    time.sleep(2/(i+1))

endtime = time.time()

anitime = round(endtime - starttime, 2)
pen.up()
pen.clear()
pen.color("white")
pen.goto(0, 0)
pen.write(f"Total animation time: {anitime} seconds", align="center", font=("arial", 50))

screen.mainloop()