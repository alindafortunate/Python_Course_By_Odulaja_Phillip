# A grading system.

# Take an example
# 70 -> A
# 60 -> B
# 50 -> C
# 50 <  D

score = int(input("Enter your score: "))

if score >= 70:
    print("Your score is", score, "and your grade is A")
elif score >= 60:
    print("Your score is", score, "and your grade is B")
elif score >= 50:
    print("Your score is", score, "and your grade is C")
else:
    print("Your score is", score, "and your grade is D")
