# A simple admission system

# fees = 5000

# student_payment = input("How much have you paid? ")

# if int(student_payment) >= fees:
#     print("Access granted")

# elif int(student_payment) >= 2000:
#     print("Limited access granted")

# else:
#     print("Acess denied")


# a market pricing application

# A farmer sells fruits like
# mangoes at 2000
# oranges at 3000
# apples at 1000
# others at 500
print("Note: Kindly be specific e.g mangoes instead of I want mangoes.")
fruit = input("Which fruits do you want, kindly be specific e.g apples, mangoes ? ")
if fruit == "mangoes":
    print(fruit, "cost 2000/=")
elif fruit == "oranges":
    print(fruit, "cost 3000/=")
elif fruit == "apples":
    print(fruit, "cost 1000/=")
else:
    print(fruit, "cost 500/=")
