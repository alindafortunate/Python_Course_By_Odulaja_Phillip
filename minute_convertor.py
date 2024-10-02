#  A program to convert minutes to hours.

minutes = float(input("How many minutes would you like to convert to hours? "))

hours = minutes // 60
remaining_minutes = minutes % 60

response = f"{hours} hours {remaining_minutes} minutes"

print(response)
