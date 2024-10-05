# Working with string functions just like lists in python.

# capitalize, count, endswith, startswith, index, replace, title, upper, split, lower, islower, isupper


name = "philip"
# string_functions = dir(name)

# print(string_functions)

# capitalize_name = name.capitalize()

# index = name.index("p")
# print(index)
# print(capitalize_name)
# char_count = name.count("i")
# print(char_count)

# if name.endswith("p"):
#     print("The name ends with character P")
# else:
#     print("The name does not end with character P")

# if name.startswith("i"):
#     print("The name starts with character i")
# else:
#     print("The name does not start with character i")

# index
# index = name.index("l")
# print(index)

# name2 = "fortunate"
# # replace
# modified_name = name2.replace("f", "alinda")
# print(modified_name)

# title
# name2 = "fortunate"
# # title_function = name2.title()
# # print(title_function)

# # upper
# name2 = "fortunate"
# uppercase_name = name2.upper()
# # print(uppercase_name)

# name3 = "ALINDA"
# lowercase_name = name3.lower()
# # print(lowercase_name)

# if name3.isupper():
#     print("The name is in uppercase.")
# else:
#     print("The name is in lowercase.")

# if name2.islower():
#     print("The name is in lowercase.")
# else:
#     print("The name is in uppercase.")

# Working with the split function on strings.
class_names = "Alinda|Lucky|Jonan|Desire|Prosper"
splited_names = class_names.split("|")
print(splited_names)
