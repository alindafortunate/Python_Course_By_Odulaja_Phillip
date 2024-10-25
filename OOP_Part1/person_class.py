# Create a class called "Person" with the following properties:
# - name (string)
# - age (integer)
# - occupation (string)
# The class should have a constructor that initializes these properties.

# Create two methods within the class:
# - introduce(): prints a message introducing the person with their name, age, and occupation.
# - change_occupation(new_occupation): updates the occupation of the person.

# Create two objects of the Person class and test the methods.


class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print(f"{self.name} is {self.age} years old, and he is a {self.occupation}")

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        print(
            f"{self.name} is {self.age} years, has changed to being a {self.occupation}."
        )


alinda = Person("Ainda Fortanate", 26, "Fellow")
# alinda.introduce()
# alinda.change_occupation("Backend Engineer")

opio = Person("Opio Jack", 30, "teacher")
opio.introduce()
opio.change_occupation("Software Developer")
