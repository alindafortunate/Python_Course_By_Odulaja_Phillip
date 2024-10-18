# A program to demonstrate how type hinting works.


def display_info(name: str, age: int, height: float) -> str:
    """
    A function that displays the person's information.
    """
    return f"Name: {name}, Age: {age}, Height: {height}"


name = input("What is your name?: ")
age = int(input("What is your age?: "))
height = float(input("What is your height?: "))

print(display_info(name, age, height))
