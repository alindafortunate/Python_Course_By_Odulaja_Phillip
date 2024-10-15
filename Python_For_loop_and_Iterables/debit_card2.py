# A more simplified version of the debit card program.

debit_card_number = input(
    "Enter your 16 digit card number with each 4 digits separated by a space: "
).replace(
    " ", ""
)  # Here we are using the replace function to ensure that the loop through is easy and the spaces are neglected
# print(debit_card_number)

counter = 0  # We use a counter to number the number of iterations the loop iterates.
card_number = ""  # Here we to the first 12 "*" in card number for the first 12 digits.

for number in debit_card_number:
    counter += 1

    if counter <= 12:
        card_number += "*"
    else:
        card_number += number  # This is so because remember number is string not yet converted to an integer so no additional maths happens
# print(counter)
print(f"Your debit card number is {card_number}")
