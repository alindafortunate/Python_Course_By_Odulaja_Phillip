# Ploymorphism means taking many different forms on achieving something
# e.g the "+" operator works on both addition of numbers and concatinating strings.

# print(1 + 2)
# print("Alinda" + " " + "Fortunate")

# # Using a len function.
# print(len("Alinda Fortunate"))


# name = "Alinda Fortunate"
# print(name)
# print(len([1, 2, 3, 4, 5, 6]))

# print(
#     len(
#         {
#             "Alinda": 26,
#             "Brendah": 24,
#             "Lucky": 24,
#             "Jonan": 16,
#         }
#     )
# )
# print("The output below is for the for loop.")
# for i in (1, 4):
#     print(i)

# A polymorphism class


class Liquid:
    def __init__(self, name, formula):
        self.name = name
        self.formula = formula

    def info(self):
        print(f"I am a liquid form. I am {self.name} and my formula is {self.formula}")

    def property(self):
        print("I am clear and light form.")


class Solid:
    def __init__(self, name, formula):
        self.name = name
        self.formula = formula

    def info(self):
        print(f"I am a solid form. I am {self.name} and my formula is {self.formula} ")

    def property(self):
        print("I can be transparent or clear or completely opaque.")


liquid_1 = Liquid("Water", "H2O")
solid_1 = Solid("Ice", "H2O")

for material in (liquid_1, solid_1):
    material.info()
    material.property()
