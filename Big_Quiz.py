from random import randint
import pgzrun
import pygame

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["What  is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]

q2 = ["What  is the capital of Germany?",
      "London", "Washington D.C.", "Rome", "Berlin", 2]


def draw():
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
    #screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.text("Press q to quit!", color="white", topleft=(int(WIDTH / 2 - 80), HEIGHT - 50), fontsize=30)


def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down():
    pygame.quit()
    quit()


def update_time_left():
    pass

def update():
    if keyboard.q:
        pygame.quit()
        quit()

def time_up():
    pygame.quit()
    quit()

clock.schedule(time_up, 30.0)
pgzrun.go()