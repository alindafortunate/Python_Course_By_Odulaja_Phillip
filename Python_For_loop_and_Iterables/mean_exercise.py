terms = [67, 43, 24, 45, 22]

# Finding the mean of the items

sum = 0
for num in terms:
    sum += num

    no_of_items = 0
    for num in terms:
        if num > 1:
            no_of_items += 1

mean = sum / no_of_items
print(f"The sum is {sum} and the terms are {no_of_items}")
print(f"The mean is {mean}")

# Ideally we can also use the len function to get the number of items.
number_of_items = len(terms)

mean = sum / number_of_items
print(f"The mean is {mean}")
