# Working with import statement only

# import bank
# name1 = "Solomon"
# print(bank.register_user(name1, 1))
# print(bank.total_user())

# Working with the from keyword

# from bank import *
# name1 = "Judith"
# name2 = "Prosper"

# register_user(name1, 1)
# register_user(name2, 2)

# delete_user(name1)

# print(all_users)
# print(total_user())

# working with importing specific functions and variables

# from bank import register_user, delete_user, all_users, total_user

# name3 = "Gloria"
# name4 = "Benson"
# name5 = "Desire"

# register_user(name3, 3)
# register_user(name4, 4)
# register_user(name5, 5)

# delete_user(name3)

# print(all_users)
# print(total_user())


# working with 'as' as a keyword
import bank

from bank import all_users as alu

all_users = ["Apple", "Mangoes", "Oranges", "Pawpaws"]
print(alu)
print(all_users)
