# A system to check various conditions
# Assuming we have orange and other fruits
# Assume we have Ugandan Oranges at 7000/= and Kenyan Oranges at 5000/=
# Then other fruits at 3000/=

fruit = input("What fruit do you want? ")


if fruit == "oranges":
    orange_type = input(
        "What orange type do you want? Uganda Oranges, Rwandan Oranges or Kenyan Oranges. "
    )

    if orange_type == "Ugandan Oranges":
        print("Uganda oranges cost 7000/=")

    elif orange_type == "Rwandan Oranges":
        print("Rwandan oranges cost 6000/=")

    else:
        print("Kenyan oranges cost 5000/=")
else:
    print("Other fruits cost 3000/=")
