# Task 2: Create a simple game function, that takes no parameter and initiates the guessing game
# 1. The game should generate a random number between 1 and 100.
# 2. The player should be prompted to guess the number.
# 3. The game should provide feedback to the player after each guess, indicating whether the guess was too high or too low.
# 4. The player has 5 chances to get it right and whenever they guess wrong they lose a chance.
# 5. If the player guesses the correct number within the given attempts, they should be declared the winner.
# 6. If the player runs out of attempts without guessing the correct number, they should be declared the loser.
# Hint : Learn about python break keyword

"""
This program seeks to explaing the concept of recursion,
With recursion, you have a function calling itself within the its own body

check line 64, the game() function is calling itself.
"""

import random

game_logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀.
█░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
█▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """

total_chances = ["💖", "💖", "💖", "💖", "💖"]
win_emoji = "🏆🎉"
lose_emoji = "💔😭"


def game():
    """
    A function for playing a game.

    """
    print(game_logo)
    total_chances = ["💖", "💖", "💖", "💖", "💖"]
    correct_number = random.randint(1, 100)
    print(correct_number)

    while total_chances.count("💖") > 0:
        guess_number = int(input("Guess a number between 1 and 100: "))
        if guess_number > correct_number:
            total_chances.remove("💖")
            total_chances.append("💔")
            print(
                f"Oh no, you your guess is too high and you have lost an attempt {total_chances}"
            )
        elif guess_number < correct_number:
            total_chances.remove("💖")
            total_chances.append("💔")
            print(
                f"Oh no, you your guess is too low and you have lost an attempt {total_chances}"
            )

        else:
            print(f"Congragulations you have won {win_emoji}")
            break
    if total_chances.count("💖") == 0:
        print(f"You are out of chances and you have lost the game {total_chances}")
    second_time = input("If you still want to play the game type 'y' otherwise 'n' ")
    if second_time == "YES":
        game()
    else:
        pass


game()
