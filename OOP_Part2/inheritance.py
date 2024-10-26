# A program to demonstrate inheritance in python.


class Animal:
    def breath(self):
        print("Animal can breath.")

    def grow(self):
        print("Animal can grow.")

    def eat(self):
        print("Animal can eat.")


class Mamal(Animal):
    def walk(self):
        print("A mamal can walk.")

    def run(self):
        print("A mamal can run.")


cow = Mamal()
cow.breath()
cow.eat()
cow.run()

aquatic = Animal()
aquatic.grow()
