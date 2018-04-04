# pylint: disable=maybe-no-member

""" Number Guessing Game by Darrell Pawson
The program will pick a number between
1 and 100 and the user will guess the
number. If the number is too low it
will trigger a light the same as guessing
high and correctly.  Also a buzzer will sound
after 10 incorrect guesses or if the user gets
the random number"""

# Import required modules
import os
import sys
import time
import random

# Import the GPIO module
import RPi.GPIO as GPIO

# Configure the Pi to use the BCM pin numbers
GPIO.setmode(GPIO.BCM)

# Configure Led and Buzzer GPIO pins
RED_LED = 23
YELLOW_LED = 24
GREEN_LED = 25
GAME_BUZZER = 21

LED_LIST = [RED_LED, YELLOW_LED, GREEN_LED]
GAME_WIN = [GREEN_LED, GAME_BUZZER]
GAME_LOST = [GREEN_LED, RED_LED, YELLOW_LED, GAME_BUZZER]

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(GAME_BUZZER, GPIO.OUT)

# Configure the random number
RANDOM_NUMBER = random.randint(1, 100)

# Remove warnings if script is terminated and GPIO pins are not cleaned up
GPIO.setwarnings(False)

# Get users name
USER_NAME = str(input("Hello, what is your name player?: "))

# Adding a delay print function to add more fluff to the game
def delay_print(string):
    """Delayed print function"""
    for char in string:
        sys.stdout.write(char)
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
        main()

def end_game():
    """This ends the game by calling sys.exit(0) and GPIO.cleanup()"""

    print("Thanks for playing! %s" %USER_NAME)
    GPIO.cleanup()
    sys.exit(0)

def start_game():
    """Core code for the game"""
    # Flash lights for the duration of the messages
    t_end = time.time() + 60 * 0.09
    while time.time() < t_end:
        on_time = random.uniform(0, .025)
        led = random.choice(LED_LIST)
        GPIO.output(led, True)
        time.sleep(on_time)
        GPIO.output(led, False)

    os.system('cls' if os.name == 'nt' else 'clear')
    delay_print("Well %s I'm glad you've decided to play!\n" %USER_NAME)
    time.sleep(0.75)
    delay_print("Here's how the game works...\n")
    time.sleep(0.75)
    delay_print("I am going to guess a number between 1 and 100...\n")
    time.sleep(0.75)
    delay_print("and you are going to guess that number.\n")
    time.sleep(0.75)
    delay_print("You have 10 tries to guess the correct number...\n")
    time.sleep(0.75)
    delay_print("If your guess is too high, the Red LED will light up...\n")
    time.sleep(0.75)
    delay_print("If your guess is too low, the Yellow LED will light up...\n")
    time.sleep(0.75)
    delay_print("If your guess is the same as my number, the Green LED will light...\n")
    time.sleep(0.75)
    delay_print("And the buzzer will go off!\n")
    time.sleep(0.75)
    delay_print("And remember... If you cannot guess my number within 10 tries...\n")
    time.sleep(0.75)
    delay_print("The game is over and all the lights will flash and the buzzer will sound.\n")
    time.sleep(0.75)
    delay_print("With that being said... Let's play %s\n" %USER_NAME)

    # Setup attempts | User gets 10 trys to guess the correct number
    user_tries = 0
    total_tries = 10

    while user_tries <= 10:
        tries_left = total_tries - user_tries
        player = int(input("%s please pick a number between 1 and 100: " %USER_NAME))
        if player < RANDOM_NUMBER:
            print("Your guess is too low %s" %USER_NAME)
            GPIO.output(YELLOW_LED, True)
            time.sleep(1)
            GPIO.output(YELLOW_LED, False)
            user_tries += 1
            print("You have %i trys left!" %tries_left)
        elif player > RANDOM_NUMBER:
            print("Your guess is too high %s" %USER_NAME)
            GPIO.output(RED_LED, True)
            time.sleep(1)
            GPIO.output(RED_LED, False)
            user_tries += 1
            print("You have %i trys left!" %tries_left)
        elif player == RANDOM_NUMBER:
            user_tries += 1
            print("YOU WIN!... You guessed the number in %i trys" %user_tries)
            GPIO.output(GAME_WIN, True)
            time.sleep(5)
            GPIO.output(GAME_WIN, False)
            break
        else:
            print("Enter a valid number!")

        if user_tries == total_tries:
            print("You lost, you didnt guess the number in time, the number was %i." %RANDOM_NUMBER)
            GPIO.output(GAME_LOST, True)
            time.sleep(5)
            GPIO.output(GAME_LOST, False)

if __name__ == "__main__":
    main()

GPIO.cleanup()
