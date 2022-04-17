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

#Task: Keep questions in a file and read them and make questions array.
# step 1: create a text file with questions.txt , answers and correct answer 5 columns
# step 2: Read the file
# step 3: loop the file contents and create questions array. 2 dimensional array
# step 4: use that questions array in your program.
# Refer to https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_strings.asp
# hint: you might have to use forloop and string split and arrays

questions = []

def prep_questions(file_input):
    global questions
    f = open(file_input)
    for current_line in f:
        #print(current_line)
        #create a list of current question with current line
        q = current_line.replace('\n', '').split(",")
        #print(type(q))
        #creating a parent or global questions , list of lists
        questions.append(q)


prep_questions("Quiz.txt")

''' Comments
q1 = ["What  is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]

q2 = ["What  is the capital of Germany?",
      "Kyiv", "Washington D.C.", "Rome", "Berlin", 4]

q3 = ["What  is the capital of Australia?",
      "Canberra", "Sydney", "Kingston", "Havana", 1]

q4 = ["What  is the capital of the Netherlands?",
      "Warsaw", "Budapest", "Amsterdam", "Tirana", 3]

q5 = ["What is the capital Egypt?",
      "Cairo", "Alexandria", "Luxor", "Giza", 1]
questions2 = [q1, q2, q3, q4, q5]

print(questions)
current_question = questions.pop(0)
print(current_question)
print(current_question[0])
'''

current_question = questions.pop(0)
def draw():
    screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
    #screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.text("Press q to quit!", color="white", topleft=(int(WIDTH / 2 - 80), HEIGHT - 50), fontsize=30)

    screen.draw.textbox(str(time_left), timer_box, color="black" )
    screen.draw.textbox(current_question[0], main_box, color="black" )

    index = 1
    for box in answer_boxes:
        #strip remove spaces in answers and ends, just in case
        screen.draw.textbox( current_question[index].strip(), box, color="black" )
        index = index + 1



def game_over():
    global current_question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    current_question = [message, "-", "-", "-", "-", 5]
    time_left = 0



def correct_answer():
    global current_question,score, time_left

    score = score + 1
    if questions:
        current_question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

#pos is the coordinates or position x,y
#this method is an event called when user clicks mouse
#this is a mouse click event
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == int(current_question[5]):
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1


def update_time_left():
    global time_left

    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)

#pygame keeps callign this update continously
#there is no keyboard even

def update():
    if keyboard.q:
        pygame.quit()
        quit()

def time_up():
    pygame.quit()
    quit()

clock.schedule(time_up, 30.0)
pgzrun.go()
