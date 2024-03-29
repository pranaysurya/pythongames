# Purpose: To create a game with random coins and am actor , fox to collect
# author : Pranay

from random import randint

player1 = input("Enter player 1 name : ")
player2 = input("Enter player 2 name : ")
print(player1 + " is the fox : Use WASD to move.")
print(player2 + " is the wolf: Use ARROW keys to move.")
print("Press q to quit!")
print("-----------------------------------------------")

#moved this 2 imports here to avoid box popup before entering the names
import pgzrun
import pygame

WIDTH = 1366
HEIGHT = 768
score_player1 = 0
score_player2 = 0
game_over = False

fox2 = Actor("wolf")
fox2.pos = 100, 100
fox = Actor("fox")
fox.pos = 100, 250

coin = Actor("coin")
coin.pos = 200, 2

def draw():
   screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
   screen.fill("black")
   fox.draw()
   fox2.draw()
   coin.draw()
   screen.draw.text("Score of " + player1 + ": " + str(score_player1), color="white", topleft=(10, 10))
   screen.draw.text("Score of " + player2 + ": " + str(score_player2), color="white", topleft=(1110, 10))
   screen.draw.text("Press q to quit!",  color="white", topleft=( int(WIDTH/2), HEIGHT-50), fontsize=20)

   if game_over:
      screen.fill("blue")
      screen.draw.text("Final Score of " + player1 + ": " + str(score_player1), topleft=(10, 10), fontsize=60, color="orange")
      screen.draw.text("Final Score of " + player2 + ": " + str(score_player2), topleft=(745, 10), fontsize=60, color="orange")
      if score_player1 == score_player2:
         screen.draw.text("It's a draw!", topleft=(500, 250), fontsize=60, color="orange")
      elif score_player1 >= score_player2:
         screen.draw.text("Hooray! " + player1 + " WINS!", topleft=(400, 250), fontsize=60, color="orange")
      elif score_player2 >= score_player1:
         screen.draw.text("Hooray! " + player2 + " WINS!", topleft=(400, 250), fontsize=60, color="orange")

      screen.draw.text("Press q to Quit", topleft=(450, 300), fontsize=60, color="orange")

def place_coin():
   coin.x = randint(20, (WIDTH - 20))
   coin.y = randint(20, (HEIGHT - 20))


def time_up():
   global game_over
   game_over = True

def update():
   global score_player1
   global score_player2

   if keyboard.q:
      pygame.quit()
      quit()

   if keyboard.left:
      fox2.x = fox2.x - 4
   elif keyboard.right:
      fox2.x = fox2.x + 4
   elif keyboard.up:
      fox2.y = fox2.y - 4
   elif keyboard.down:
      fox2.y = fox2.y + 4
   if keyboard.left and keyboard.up:
      fox2.x = fox2.x - 2
      fox2.y = fox2.y - 2
   elif keyboard.right and keyboard.up:
      fox2.x = fox2.x + 2
      fox2.y = fox2.y - 2
   if keyboard.left and keyboard.down:
      fox2.x = fox2.x - 2
      fox2.y = fox2.y + 2
   elif keyboard.right and keyboard.down:
      fox2.x = fox2.x + 2
      fox2.y = fox2.y + 2


   if keyboard.a:
      fox.x = fox.x - 4
   elif keyboard.d:
      fox.x = fox.x + 4
   elif keyboard.w:
      fox.y = fox.y - 4
   elif keyboard.s:
      fox.y = fox.y + 4
   if keyboard.a and keyboard.w:
      fox.x = fox.x - 2
      fox.y = fox.y - 2
   elif keyboard.d and keyboard.w:
      fox.x = fox.x + 2
      fox.y = fox.y - 2
   if keyboard.a and keyboard.s:
      fox.x = fox.x - 2
      fox.y = fox.y + 2
   elif keyboard.d and keyboard.s:
      fox.x = fox.x + 2
      fox.y = fox.y + 2

   coin_collected_by_player1 = fox.colliderect(coin)
   coin_collected_by_player2 = fox2.colliderect(coin)

   if coin_collected_by_player1:
      score_player1 = score_player1 + 10
      place_coin()

   elif coin_collected_by_player2:
      score_player2 = score_player2 + 10
      place_coin()


clock.schedule(time_up, 30.0)
place_coin()


pgzrun.go()