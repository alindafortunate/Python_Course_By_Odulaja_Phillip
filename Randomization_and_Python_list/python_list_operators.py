# Exploring the python list operators.

programming_languages = ["Java", "Python", "C#", "C++", "Javascript", "Flutter", "Dart"]

# list_functions = dir(programming_languages)
# print(list_functions)

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# 001_Exploring append

# x = programming_languages.append("Django")
# programming_languages.append("Django REST")
# print(programming_languages)

# 002_Exploring the clear function

cart = ["Macbook", "toilet paper", "airpode", "baking powder"]
# cart.append("oven")

# # cart.clear()

# # 003_Exploring the copy function
# cart_copy = cart.copy()
# print(cart)
# # print(cart_copy)

# # 004_Exploring the count function
# cart.append("baking powder")
# no_of_items = cart.count("baking powder")
# no_of_oven = cart.count("oven")
# print(no_of_items)
# print(no_of_oven)


# 005_Exploring the extend function

cart = ["Macbook", "toilet paper", "airpode", "baking powder"]
sub_cart = ["monitor", "computer"]

extended_cart = cart.extend(sub_cart)
# print(cart)

# 006_Exploring the index function

# index = cart.index("computer")
# print(index)

# 007_Exploring the insert function

# cart.insert(1, "Chromebook")
# cart.insert(-1, "keyboard")

# print(cart)

# 008_Exploring the pop function

cart = [
    "Macbook",
    "Chromebook",
    "toilet paper",
    "airpod",
    "baking powder",
    "monitor",
    "keyboard",
    "computer",
]
# cart.pop(0)

# print(cart)

# 009_Exploring the remove function
# cart.remove("airpod")
# print(cart)

# 011_Exploring the reverse function
# cart.reverse()
# print(cart)



# 010_Exploring the sort function
cart.sort()
print(cart)