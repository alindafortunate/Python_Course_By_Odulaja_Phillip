# A program to help us understand local and global variables.

# global scope
# duel1 = "Gandalf vs Dumbledore"


# def magic_duel():
#   Local scope
#     duel = "Harry vs Voldemort"
#     print(f"The winner is {duel}")
#     print(f"I am a global variable {duel1} inside the function")


# magic_duel()
# print(f"The ultimate duel is {duel1}")

# x = 50


# def example():
#     # x = 100
#     global x
# x += 56
#     print(f"I am a x in the local scope {x} ")


# example()
# print(f"I am a x in the global scope  {x} ")


def superhero_name():
    print("I am a function in the global scope.")

    def get_specific_identity():
        print("I am a function in the local scope.")

    get_specific_identity()


superhero_name()
