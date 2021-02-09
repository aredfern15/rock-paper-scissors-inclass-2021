# game.py
import os
import random
#from random import choice

from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

#from app.my_mod import to_usd

load_dotenv()
player_name = input("Hello, please enter your name: ")
print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print("Welcome", player_name, "to my Rock-Paper-Scissors game...")
print("-------------------")

#
#asking user for an input
#

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(f"You chose: {user_choice}")

#
# validate the user selection
#
# stop the program (not try to determine the winner)
#... if the user choice is invalid 

#user_choice.lower()

#if user_choice in options: 
 #   #print("GOOD")
 #   pass
#else: 
 #   print("OOPS, please choose a valid option and try again")
  #  exit()

options = ["rock", "paper", "scissors"]
if user_choice not in options: 
    print("OOPS, please choose a valid option and try again")
    exit()

#
#simulating a computer input 
#

#computer_choice = "paper"


#foo = ['a', 'b', 'c', 'd', 'e']
#computer_choice = random.choice(foo)


computer_choice = random.choice(options)
#computer_choice = choice(options)

print(f"The computer chose: {computer_choice}")

#
#determining who won
#

#accessed the below code from Professor Rossetti on Slack
if user_choice == "rock":
    if computer_choice == "rock":
        print("Oh, it's a tie.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")

elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Oh, it's a tie.")

else:
    print("OOPS SOMETHING WENT WRONG.")

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")







