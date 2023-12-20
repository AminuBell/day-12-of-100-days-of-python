#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
from random import randint
from art import logo




easy_level = 10
hard_level = 5

#Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def CheckAnswer(guess,answer,turns):
  if guess > answer:
    print("too high")
    return turns - 1
  elif guess < answer:
    print("too low")
    return turns - 1 
 
  else:
    print("you have got it right!")

def DiffultyLevel():
  level = input("select a diffulty level 'easy' or 'hard':")
  if level == "easy":
    return easy_level
  elif level == "hard":
    return hard_level
def game():
  print(logo)
  print("Welcome to the number guessing game!")
  print("i'm thinking of a number between 1 to 100")
  
  answer = randint(1,100)
  print(f"pssst the correct answer is {answer}")
  
  turns = DiffultyLevel()
 
 
  
  
  
  guess = 0
  while guess != answer:
    print(f"you have {turns} number remaining")
    guess = int(input("guess a number between 1 to 100 "))
    turns = CheckAnswer(guess, answer,turns)
    if turns == 0:
      print("you have run out of guesses, you lose")  
      game()
    elif guess != answer:
      print("guess again")
game()
  
  
  
  
  



  
  

  
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

