# A more simplified version of the debit card program.

debit_card_number = input(
    "Enter your 16 digit card number with each 4 digits separated by a space: "
).replace(" ", "")
print(debit_card_number)

counter = 0
card_number = ""
for number in debit_card_number:
    counter += 1

    if counter <= 12:
        card_number += "*"
    else:
        card_number += number
# print(counter)
print(card_number)
