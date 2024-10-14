# Developing a program that calculates the bank balance of the user
transactions = [
    200,
    455.23,
    -306.5,
    2500,
    -642.21,
    -133.9,
    79.97,
    1300,
    5000,
    3400,
    -150,
    -790,
    -3210,
    -1000,
    8500,
    -30,
]

total = 0
for transaction in transactions:
    total += transaction

    if transaction > 0:
        print(f"User has been credited $ {transaction}")
    else:
        print(f"User has been debted $ {-1 * transaction}")


print(f"The User's total balance is $ {total}")

# sum = (
#     200
#     + 455.23
#     - 306.5
#     + 2500
#     - 642.21
#     - 133.9
#     + 79.97
#     + 1300
#     + 5000
#     + 3400
#     + -150
#     - 790
#     - 3210
#     - 1000
#     + 8500
#     + -30
# )
# print(sum)
