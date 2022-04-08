import pgzrun


WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 240, 240)
timer_box = Rect(0, 0, 495, 495)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1_box.move_ip(50, 358)
answer_box2_box.move_ip(735, 358)
answer_box3_box.move_ip(50, 538)
answer_box4_box.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]


def draw():
    screen.draw.filled_rect(main_box, "sky blue")

def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down_():
    pass

def update_time_left():
    pass

pgzrun.go()