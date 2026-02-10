bank_transaction = [23.45, 34.3, -45, 50]
# Here we want to code a functionality in that when the person is
# debited no savings happen but when credited then a deduction of 5% happens as savings.

savings = list(
    map(
        lambda transaction: round(transaction * 5 / 100, 2) if transaction > 1.0 else 0,
        bank_transaction,
    )
)

print(savings)
