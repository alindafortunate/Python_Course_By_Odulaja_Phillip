fuzz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for number in fuzz:
    if number % 5 == 0:
        print(f"fizz")
    elif number % 3 == 0:
        print(f"buzz")
    else:
        print(f"{number}")
