from random import randint
import pgzrun
from pgzero.actor import Actor

apple = Actor("mango")
def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Shot! Keep it up!")
        place_apple()
    else:
        print("You missed! Nice game!")
        quit()

pgzrun.go()