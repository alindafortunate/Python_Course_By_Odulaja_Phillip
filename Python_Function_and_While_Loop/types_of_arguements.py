# A program to understand different types of arguements.

# 1. Positional Arguements.
"""
Here when the program is executing if work in the order of how
the formal parameters were defined in the declaration e.g 
"""

def age_calculator(name, birth_year):
    """
    A function to calculate age.
    """ 

    age = 2024 - birth_year
    print(f'Hello {name}, you are {age} years old.')
age_calculator("Alinda Fortunate", 1998)    
# On the above line you see that the arguements are in the exact order as the parameters thus positional arguements

# 2. Keyword Arguements
"""
Here when you supplying the arguements you can inter change the order of the arguements but give them values.
"""
def age_calculator(name, birth_year):
    """
    A function to calculate age.
    """ 
    age = 2024 - birth_year
    print(f'Hello {name}, you are {age} years old.')
age_calculator(birth_year=1998, name="Alinda Fortunate")

# 3. Default arguements
"""
Here while defining the parameters during function declaration, you supply them with values.
"""
def age_calculator(name, birth_year=1998): # Just like you see birth_year = 1998
    """
    A function to calculate age.
    """ 
    age = 2024 - birth_year
    print(f'Hello {name}, you are {age} years old.')
age_calculator('Alinda')


def modified_age_calculator(name, birth_year): # Just like you see birth_year = 1998
    """
    A function to calculate age.
    """ 
    
    age = 2024 - birth_year
    print(f'Hello {name}, you are {age} years old.')
modified_age_calculator(name=input('What is your name? '),birth_year=int(input('What is your birth year? ')))


