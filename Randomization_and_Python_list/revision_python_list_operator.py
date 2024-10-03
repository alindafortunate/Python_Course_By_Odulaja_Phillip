# Revision for the python list operators.
fruits = ["apples", "mangoes", "pineapples", "oranges"]


# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
another_fruits = fruits.append("jackfruits")

# fruits.clear()
# print(fruits)

# fruits_copy = fruits.copy()
# print(fruits_copy)

another_fruit = fruits.append("oranges")


# no_of_oranges = fruits.count("oranges")
# print(no_of_oranges)

sub_fruits = ["pawapaw", "avocado", "passion fruits"]
# fruits.append(sub_fruits)
fruits.extend(sub_fruits)

fruits.insert(8, "yellows")

# fruits.pop(8)
# fruits.remove("apples")
# fruits.reverse()
fruits.sort()

# index = fruits.index("apples")


print(fruits)
print("Glory to God that it has worked out.")
