computer_science = {
    "Alinda": 4.46,
    "Aidah": 4.09,
    "James": 3.98,
}

information_technology = {
    "Kasita": 4.04,
    "Gloria": 3.98,
    "Jovile": 4.02,
}

# Merge the dictionary.

facualty_of_science = {**computer_science, **information_technology}
print(facualty_of_science)
