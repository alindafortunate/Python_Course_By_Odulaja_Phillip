# We want to make a program where by the user account is
# debited 5% for saving if it has been credited otherwise not debited if it has been debited.

bank_transaction = [23.45, 567.3, -70, 45]
savings = map(
    lambda transaction: round(transaction * 5 / 100, 2) if transaction > 1.0 else 0,
    bank_transaction,
)
print(list(savings))
