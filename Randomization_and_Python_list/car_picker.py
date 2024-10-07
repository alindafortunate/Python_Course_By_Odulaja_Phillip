# A program to solve the car picker problem.
import random

# Step 1: Get a string of cars.
cars = input("Enter the names of a car separated by a comma and a space: ")

# Step 2: Split the string to get a list of cars.
list_of_cars = cars.split(", ")

# Step 3: Choose the random car using the choice function from the random module.
random_car = random.choice(list_of_cars)

# Step 4: Print the random car.
print("You should get a", random_car)
