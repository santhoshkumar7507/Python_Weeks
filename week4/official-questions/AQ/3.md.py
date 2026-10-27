import math

moves = [
    "START",
    "UP",
    "RIGHT",
    "LEFT",
    "LEFT",
    "DOWN",
    "UP",
    "STOP"
]

x = 0
y = 0

for move in moves:
    if move == "UP":
        y += 1
    elif move == "DOWN":
        y -= 1
    elif move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1

distance = math.sqrt(x*x + y*y)

print("Final Position:", (x, y))
print("Distance from Origin:", distance)