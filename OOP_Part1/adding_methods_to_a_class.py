# A program that has  class methods.


class Human:
    def __init__(self, gender, skin_color, weight):
        # These are class attributes.
        self.gender = gender
        self.skin_color = skin_color
        self.weight = weight

        # adding more methods to a class.

    def display_information(self):
        print(
            f"This human is {self.gender}, {self.skin_color} and has {self.weight} kg"
        )

        # using the built in str method

    def __str__(self):
        # String representation of a class.
        return f"Human(gender, skin_color, weight)"


# applying the methods of the class on the object.
alinda = Human("male", "black", 67.5)
alinda.display_information()
print(alinda.__str__())

opio = Human("male", "brown", 70)
print(opio.__str__())
# opio.display_information()
