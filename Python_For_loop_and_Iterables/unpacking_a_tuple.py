# A program that unpacks a tuple.

best_athletes = ("Lebron", "Kobe", "Jordan")

# unpacking
# first, second, third = best_athletes
# print(f"The first item is {first}")
# print(f"The second item is {second}")
# print(f"The third item is {third}")

# databases = ("MySQL", "PostgreSQL", "Cassandra", "sqlite", "MS access", "Oracle")
# # unpacking many items.
# firstDB, secondDB, *otherDB = databases
# print(otherDB)

careers = ("DevOps", "Software Developer", "Teacher")
first_tech_career, second_tech_career, non_tech_career = careers

print(first_tech_career)
print(second_tech_career)
print(non_tech_career)

continents = (
    "Africa",
    "Europe",
    "Asia",
    "North America",
    "South America",
    "Antarctica",
)
first_continent, second_continent, *other_continents = continents
print(first_continent)
print(second_continent)
print(other_continents)

country = "Uganda"
added_country = other_continents.append(country)
print(other_continents)
print(continents)
