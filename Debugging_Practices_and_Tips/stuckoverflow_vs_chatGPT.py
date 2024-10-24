# A program to help us understand how to debug using stackoverflow and chatGPT
def divide_numbers(a, b):
    result = a / b
    return result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = divide_numbers(num1, num2)
print("The result of the division is: " + str(result))
