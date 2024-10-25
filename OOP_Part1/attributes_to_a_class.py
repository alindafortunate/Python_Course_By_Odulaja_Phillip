# A program that has a class with attributes.


class Human:
    def __init__(self, gender, skin_color, weight):
        # These are class attributes.
        self.gender = gender
        self.skin_color = skin_color
        self.weight = weight


# creating objects.
alinda = Human("Male", "black", 67.5)
opio = Human("male", "brown", 70)


# To access the weight of opio we use
weight_for_opio = opio.weight
weight_for_alinda = alinda.weight
print(f"Opio's weight: {weight_for_opio}")
print(f"Alinda's weight: {weight_for_alinda}")
