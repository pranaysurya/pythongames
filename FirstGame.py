#Pranays first python game work

def greet():
    greeting = "Hello "
    name = "Martian"
    message = greeting + name
    print(message)
    print("this message has " + str(len(message)) + " letters.")

def list():

   #Card_name = input("Name a card - Hearts, Diamonds, Spades or Clover:- ")
   #Card_number = input("Pick a number between 0 and 9:- ")
    Heart_cards = ["1 heart " , "2 hearts" , "3 hearts" , "4 hearts" , "5 hearts" , "6 hearts" , "7 hearts" , "8 hearts" , "9 hearts" , "10 hearts"]
    Diamond_cards = ["1 diamond ", "2 diamonds", "3 diamonds", "4 diamonds", "5 diamonds", "6 diamonds", "7 diamonds",
                   "8 diamonds", "9 diamonds", "10 diamonds"]
    Spade_cards = ["1 spade ", "2 spades", "3 spades", "4 spades", "5 spades", "6 spades", "7 spades",
                   "8 spades", "9 spades", "10 spades"]
    Clover_cards = ["1 heart ", "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts", "7 hearts", "8 hearts",
               "9 hearts", "10 hearts"]
    Card_name = input("Name a card - Hearts, Diamonds, Spades or Clover:- ")
    if Card_name == "Hearts":
       Card_number = input("Pick a number between 0 and 9:- ")
       if int(Card_number) in range(0,9):
           print(Card_number + " hearts.")
       else:
           print("Sorry, Not a valid number.")


def game():
    answer = input("Throw a water baloon? (y/n)")
    while answer == "y":
        print("Splash!!!")
        answer = input("Throw another water baloon? (y/n)")
    print("GoodBye!")

#greet()
#list()
#game()
#robo()


