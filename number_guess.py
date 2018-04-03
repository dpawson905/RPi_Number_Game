# pylint: disable=maybe-no-member

""" Number Guessing Game by Darrell Pawson
The program will pick a number between
1 and 100 and the user will guess the
number. If the number is too low it
will trigger a light the same as guessing
high and correctly.  Also a buzzer will sound
after 10 incorrect guesses or if the user gets
the random number"""
# Import the os module
import os
# Import the randint function from the random module
from random import randint
# Import the sys module for exiting the application
import sys
# Import the GPIO module
import RPi.GPIO as GPIO
# Import the time module
import time

# Configure the Pi to use the BCM pin numbers
GPIO.setmode(GPIO.BCM)

# Configure Led and Buzzer GPIO pins
RED_LED = 23
YELLOW_LED = 24
GREEN_LED = 25
GAME_BUZZER = 21
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(GAME_BUZZER, GPIO.OUT)

# Configure the random number
RANDOM_NUMBER = randint(1, 100)

# Setup attempts | User gets 10 trys to guess the correct number
USER_TRYS = 0

# Get users name
USER_NAME = str(input("Hello, what is your name player?: "))

# Adding a delay print function to add more fluff to the game
def delay_print(s):
    """Delayed print function"""
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def main():
    """This function starts the game and asks the player if they want to play.
    If the user types y or yes then the game calls the start_game function.
    If the user selects n or no then the game calles the end_game function"""

    # Ask the user if they want to play
    player = str(input("Hello %s would you like to play my number guess game? (y/n): "
                       %USER_NAME)).lower()

    if player == "n" or player == "no":
        end_game()
    elif player == "y" or player == "yes":
        start_game()
    else:
        print("Something went wrong, chances are you typed something other than y/n. Try again!")
        start_game()

def end_game():
    """This ends the game by calling sys.exit(0) and GPIO.cleanuo()"""

    print("Thanks for playing! %s" %USER_NAME)
    GPIO.cleanup()
    sys.exit(0)

def start_game():
    """Core code for the game"""
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("Well %s I'm glad you've decided to play!" %USER_NAME)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("Here's how the game works...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("I am going to guess a number between 1 and 100...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("and you are going to guess that number.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("You have 10 tries to guess the correct number...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("If your guess is too high, the Red LED will light up...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("If your guess is too low, the Yellow LED will light up...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("If your guess is the same as my number, the Green LED will light...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("And the buzzer will go off!")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("And remember... If you cannot guess my number within 10 tries...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("The game is over and all the lights will flash and the buzzer will sound.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("With that being said... Let's play %s" %USER_NAME)

if __name__ == "__main__":
    main()

GPIO.cleanup()
