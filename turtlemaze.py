import turtle, random

while True:
    try:
        height = int(input("What is the height of the maze you want to solve(odd number)? "))
        break
    except:
        pass
while True:
    try:
        width = int(input("What is the width of the maze you want to solve (odd number)? "))
        break
    except:
        pass

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Register shapes
#turtle.shape("square")
#turtle.speed(100)
# Maze grid
# maze = [
#     "XXXXXXXXXXXXXXX",
#     "X   X         X",
#     "X XXXXX XXXXX X",
#     "X X     X     X",
#     "X X XXX X XXX X",
#     "X X   X X X   X",
#     "X XXX X X X XXX",
#     "X     X X X   X",
#     "XXXXX X X X XXX",
#     "X     X   X   X",
#     "X XXXXX XXXXX X",
#     "X             X",
#     "XXXXXXXXXXXXX F"
# ]

import random

def generate(height, width):
    
    maze = [['X' for _ in range(width)] for _ in range(height)]
    
    directions = [
        {'dx': 0, 'dy': -1},
        {'dx': -1, 'dy': 0},
        {'dx': 0, 'dy': 1},
        {'dx': 1, 'dy': 0}
    ]
    
    stack = []

    stack.append({'x': height - 1, 'y': width - 1})
    maze[height - 1][width - 1] = 'F'

    while stack:
        current = stack[-1]

        # Shuffle directions for randomness
        shuffled = random.sample(directions, len(directions))
        carved = False

        for d in shuffled:
            nx = current['x'] + d['dx'] * 2
            ny = current['y'] + d['dy'] * 2

            if (
                0 <= nx < height and
                0 <= ny < width and
                maze[nx][ny] == 'X'
            ):
                maze[current['x'] + d['dx']][current['y'] + d['dy']] = ' '
                maze[nx][ny] = ' '
                stack.append({'x': nx, 'y': ny})
                carved = True
                break

        if not carved:
            stack.pop()

    for i in maze:
        i.insert(0, "X")
        i.append("X")
    maze.insert(0, ["X"]*(width+2))
    maze.append(["X"]*(width+2))
    return maze


def place(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            char = maze[i][j]
            screenx = -288 + (j * 24)
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

def printmaze(maze):
    for i in range(len(maze)):
        print("".join(maze[i]))

maze = generate(height,width)
printmaze(maze)
place(maze)

# Turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(-264, 264)

screen.mainloop()