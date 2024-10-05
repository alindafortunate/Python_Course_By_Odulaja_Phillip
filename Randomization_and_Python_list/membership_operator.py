# Working with the membership operator 'in'
east_african_countries = [
    "Uganda",
    "Kenya",
    "Tanzania",
    "Rwanda",
    "Burundi",
    "South Sudan",
    "Somalia",
    "DRC",
]
# country = input("Name a country in East Africa: ")

name = "Alinda"
char_in_name = input("What character is in the name Alinda: ")

# if country in east_african_countries:
#     print(f"{country} is in East Africa.")
# else:
#     print(f"{country} is not in East Africa.")
if char_in_name not in name:
    print(f"{char_in_name} is not in the name {name}")
else:
    print(f"{char_in_name} is in the name {name}")
