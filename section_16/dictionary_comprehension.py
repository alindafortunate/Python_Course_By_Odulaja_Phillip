# Working with dictionary comprehension.
# snytax

intended_dict = {"key": "value" for key in "value" if "pass"}
names = ["Ali", "Fortunate", "Mutesi"]

dict_of_names = {n: len(n) for n in names}
print(dict_of_names)
