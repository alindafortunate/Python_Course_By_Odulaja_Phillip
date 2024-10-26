# A program to understand multiple inheritance and method resolution order.
# Multiple inheritance here a classes inherites from more than one class.
# Method resolution order here the class inherites methods and attributes in order of left to right.
class Base:
    depth = 12

    def test(self):
        print("I am a Test method for the Base class.")


class Base2:
    depth = 13

    def test(self):
        print("I am a Test method for the Base2 class.")


class Base3(
    Base,
    Base2,
):
    pass
    # def test(self):
    #     print("I am a Test method in the Base3 class.")


base3 = Base3()
base3.test()
print(base3.depth)
