# Creating a new dictionary.
# It's important to use this method dict()

bank_user = dict()
# print(bank_user)

# an example of a python dictionary

bank_users = {
    "Alinda": 20000,
    "Jonan": 2000,
    "Fortunate": 15000,
}

# print(bank_users)

# adding items to bank_user
# bank_user['key']='value'

bank_user["Amon"] = 1000
bank_user["Alex"] = 1500
bank_user["Odramadi"] = 2000
# print(bank_user)


# modfying the value for amon
amon_balance = bank_user["Amon"]
bank_user["Amon"] = amon_balance + 1000

# print(bank_user)

# deleting an item in the dictionary
# we use the del key word
# del bank_user["Odramadi"]

# print(bank_user)


"""
The following dataypes qualify to be dictionary keys

numerical values(integers and floats)
tuples and
strings.
"""
# e.g
colours = ("red", "blue", "yellow")
age = 26
name = "Alinda"

dictionary = dict()
# adding the above keys to the dictionary
dictionary[colours] = "RBY"
dictionary[age] = 1998
dictionary[name] = "Fortunate"
dictionary["list_data_type"] = ["oranges", "apples", "mangoes"]
dictionary["set_data_type"] = {"shirt", "blanket", "sweater"}
dictionary["tuple_data_type"] = ("desks", "pens", "books")

print(dictionary)
