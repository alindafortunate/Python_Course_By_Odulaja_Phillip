# Working with list comprehesion.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# To get the even numbers of the numbers using list comprehension.
even_numbers = [n for n in numbers if n % 2 == 0]

odd_numbers_from_3 = [n for n in numbers if n % 2 != 0 and n > 1]

print(numbers)
print(even_numbers)
print(odd_numbers_from_3)
