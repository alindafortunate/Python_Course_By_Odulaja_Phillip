# String concatenation

# course_title = "Python Programming Mastery"
# title2 = "PPM"

# complete_course = course_title + " " + title2
# print(complete_course)

# # Printing a string on a new line.
# new_line = "I am text on an new line"
# complete_course = course_title + " " + title2 + "\n" + new_line
# print(complete_course)

# Working with f-string

name = "Alinda"
age = "26"
role = "Backend Engineer"

details = (
    "My name is"
    + " "
    + name
    + " I am "
    + age
    + " years old "
    + " my role is a  "
    + role
)
print(details)

details_with_f_string = f"My name is {name}, I am {age} years old and a {role}"
print(details + "\n" + details_with_f_string)
