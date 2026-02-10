from functools import reduce

# We want to make a program where by the user account is
# debited 5% for saving if it has been credited otherwise not debited if it has been debited.

bank_transaction = [23.45, 32.45, -23.345, 45.23, 567.3, -70, 45]
savings = list(
    map(
        lambda transaction: round(transaction * 5 / 100, 2) if transaction > 1.0 else 0,
        bank_transaction,
    )
)
print(savings)
# We now want to filter out 0 transactions.
filtered_savings = list(filter(lambda saving: saving != 0, savings))
print(filtered_savings)

# We want to get the total amount without using loops.
total_amount = reduce(lambda prev, next: prev + next, filtered_savings)
print(f"The total amount is {round(total_amount, 1)}")
