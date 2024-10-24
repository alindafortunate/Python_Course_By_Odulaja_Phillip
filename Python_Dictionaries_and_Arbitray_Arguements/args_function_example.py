# A sample function teaching us how to apply the *args concept.


def greetings(*args):

    for name in args:
        print(f"Hello, {name}")


greetings("Alinda Fortunate", "Mutesi Brendah Gloria", "Alinda Lucky", "Alija Jonan")


def average_calculator(*scores):

    sum_of_scores = 0
    for score in scores:
        sum_of_scores += score
    number_of_score = len(scores)
    average = sum_of_scores / number_of_score
    print(f"The average is {average}")


average_calculator(30, 31, 32, 35, 65, 78, 90)
