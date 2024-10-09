# Working with python tuples.

fruits = ("mangoes", "oranges", "apples", "mangoes")
# index = fruits.index("oranges")
# print(index)

# data_type_of_fruits = type(fruits)
# print(data_type_of_fruits)

# functions present in a tuple
tuple_functions = dir(fruits)
# print(tuple_functions) == count', 'index'

# working with count.
mango_item_count = fruits.count("mangoes")
# print(mango_item_count)

# Working with index
index_of_apples = fruits.index("apples")
print(index_of_apples)
