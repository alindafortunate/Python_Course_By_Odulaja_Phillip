# A program to guess the correct number

# Task 2: Create a simple game function, that takes no parameter and initiates the guessing game
# 1. The game should generate a random number between 1 and 100.
# 2. The player should be prompted to guess the number.
# 3. The game should provide feedback to the player after each guess, indicating whether the guess was too high or too low.
# 4. The player has 5 chances to get it right and whenever they guess wrong they lose a chance.
# 5. If the player guesses the correct number within the given attempts, they should be declared the winner.
# 6. If the player runs out of attempts without guessing the correct number, they should be declared the loser.
# Hint : Learn about python break keyword

import random


def game_function():
    game_logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀.
█░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
█▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """
    print(game_logo)
    # random.seed(1)
    random_number = random.randint(1, 100)
    print(random_number)

    total_chances = ["💖", "💖", "💖", "💖", "💖"]

    # chances = 1
    # guess = int(input("Guess a number between 1 and 100: "))
    # while chances <= 4:
    #     if guess == random_number:

    #         break

    #     else:
    #         if guess < random_number:
    #             print(
    #                 f"Your guess is too low, you have lost an attempt {total_chances}"
    #             )

    #         else:
    #             print(
    #                 f"Your guess is too high, you have lost an attempt {total_chances}"
    #             )

    #         chances += 1
    #         guess = int(input("Guess a number between 1 and 100: "))

    for i in total_chances:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == random_number:

            break

        else:
            if guess < random_number:
                total_chances.remove("💖")
                total_chances.append("💔")
                print(
                    f"Your guess is too low, you have lost an attempt {total_chances}"
                )

            else:
                total_chances.remove("💖")
                total_chances.append("💔")
                print(
                    f"Your guess is too high, you have lost an attempt {total_chances}"
                )

    if guess == random_number:
        win_emoji = "🏆🎉"
        print(f'"You won, congragulations {win_emoji}')
    else:
        print("Sorry you are out of guesses, you didn't win 💔😭")


game_function()
