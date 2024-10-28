# A progran to demonstrate the concept of encapsulation.
class BankAccount:
    def __init__(self, bak_name, account_no, balance, password):
        self.bank_name = bak_name  # Public attribute.
        self._account_no = account_no  # Protected attribute.
        self._balance = balance  # Protected attribute.
        self.__password = password

    def _withdraw(self, amount):  # protected method.
        self._balance -= amount
        return self._balance

    def deposit(self, amount):  # Public method.
        self._balance += amount
        return self._balance

    def __check_balance(self):  # Method made private.
        return self._balance


alinda = BankAccount("Stanbic", "123456789", 450000, "alinda@123")
alinda._withdraw(50000)
print(alinda._BankAccount__check_balance())
# print(alinda._balance)
print(alinda._BankAccount__password)

print(alinda.deposit(100_000))
