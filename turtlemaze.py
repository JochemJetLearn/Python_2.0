import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Register shapes
turtle.shape("square")
turtle.speed(100)
# Maze grid
maze = [
    "XXXXXXXXXXXXXXX",
    "X   X         X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X XXX",
    "X     X X X   X",
    "XXXXX X X X XXX",
    "X     X   X   X",
    "X XXXXX XXXXX X",
    "X             X",
    "XXXXXXXXXXXXX F"
]
def generate():
    for i in range(len(maze)-1):
        for j in range(len(maze[i])):
            char = maze[i][j]
            screenx = -288 + (j * 22)
            screeny = 288 - (i * 24)
            if char == "X":
                box = turtle.Turtle()
                box.speed(100)
                box.up()
                box.shape("square")
                box.goto(screenx, screeny)
            elif char == "F":
                finish = turtle.Turtle()
                finish.speed(100)
                finish.up()
                finish.shape("circle")
                finish.color("green")
                finish.goto(screenx, screeny)

# Turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)