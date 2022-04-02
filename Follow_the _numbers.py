from random import randint

from pgzero.actor import Actor

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

print("dots length: " + str(len(dots)))

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 100, 0))

def on_mouse_down(pos):
    global next_dot
    global lines
    print(pos)
    print(next_dot)
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0

