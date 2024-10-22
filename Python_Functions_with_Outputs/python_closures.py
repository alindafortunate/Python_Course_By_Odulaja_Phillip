# A program to teach us about the python closures

varible = 34


def pet_counter(pet_owner):
    pet_name = "Buddy"
    count = 0

    def counter():
        # enclosing scope
        nonlocal count
        count += 1
        global varible
        varible += count
        print(f"Hello {pet_owner}, {pet_name} has been called {count} time(s)")

    return counter


buddy_count = pet_counter("Fortunate")
# buddy_count()
# buddy_count()
for i in range(4):
    buddy_count()
