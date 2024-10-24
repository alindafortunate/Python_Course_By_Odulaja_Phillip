# A simple program that combines *args and **kwargs


def process_data(*args, **kwargs):

    for key, value in kwargs.items():
        print(f"{key} : {value}")

    sum_of_scores = 0
    for score in args:
        sum_of_scores += score
    average = sum_of_scores / len(args)
    print(f"The average score is: {average} ")


process_data(89, 90, 67, 78, 92, Name="Opio", Gender="Male", Age=27)
