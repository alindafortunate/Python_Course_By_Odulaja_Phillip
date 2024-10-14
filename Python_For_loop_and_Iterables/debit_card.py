# A simple program tp hide the last digits for a debit card.
# Note that the debit card has 16 digits.

# Step1: Capture the card number from the user.
debit_card_number = input(
    "Enter the your 16 digits debit card number, every 4 digits separated by a space: "
)
# 1234 4567 8970 6779

# Step2: Print a the card number it being hidden
print(f"Your debit card number is ", end=" ")


# Step3: SPlit the card number to see how to access the last four digits.
splitted_card = debit_card_number.split(" ")

# Step4: Capture the last four digits in a variable.
last_four_digits = splitted_card[-1]

# Step5: Pop out the last digit to see how to hide the first digits in the list.
revome_last_four = splitted_card.pop()

# Step6: Begin hiding the last digits in the splitted card by looping through.
for digits in splitted_card:

    # Replaces the first items of the splitted list by "*" after poping out the last digits
    print(digits[0].replace(digits[0], "*"), end="")

    # Replaces the second items of the splitted list by "*" after poping out the last digits
    print(digits[1].replace(digits[1], "*"), end="")

    # Replaces the third items of the splitted list by "*" after poping out the last digits
    print(digits[2].replace(digits[2], "*"), end="")

    # Replaces the forth items of the splitted list by "*" after poping out the last digits
    print(digits[3].replace(digits[3], "*"), end="")


print(last_four_digits)

# * * * * * * * * * * * * 6779
