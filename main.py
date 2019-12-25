from colorama import init, Fore, Back, Style

init()
# Import of Random 
import random
#------ Global Variables ==----
correct_guess = False
tries = 0
play = True

# starts the game
def play_game():

  while play:
    # choose game mode
    game_mode()
    # ask to play again when game ended
    play_again()

  

def game_mode():
  print("\nSelect a mode")
  print("1. Easy")
  print("2. Medium")
  print("3. Hard")

  # make a chioice of mode 
  choice = input("Your Choice: ")

  f(int(choice))


def f(difficulty):
  global correct_guess
  global tries

  if difficulty == 1:
    tries = 3
    num = random.randrange(10)
  elif difficulty == 2:
    tries = 10
    num = random.randrange(100)
  else:
    tries = 15
    num = random.randrange(1000)

  while not correct_guess:
    limit = 10 ** difficulty

    while True:
      try:
        guess = int(input(f"Enter guess from 1-{limit}: "))
        break
      except ValueError:
        print("Your guess must be a number")

    if guess > num:
        print("Your guess is too high")
    elif guess < num:
        print("Your guess is too low")
    elif guess == num:
        print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        correct_guess = True
        break

    tries_left()


def tries_left():
  # global varibles
  global correct_guess
  global tries

  # decrease tries by 1
  tries -= 1
  print(str(tries) + " attempt left")

  #check if no tries left
  if tries == 0:
    print(Fore.RED + "Game OVER!" + Style.RESET_ALL)
    #end game if tries are equal to 0
    correct_guess = True
  return


def play_again():
  global correct_guess
  replay = input("Do you want to play again? (y/n)")

  if replay == "y":
    correct_guess = False
    play_game()
  else:
    exit()

play_game()


#randomise number
#input number
#check if numbeer correct
# output info in realtion 
# ask to play again