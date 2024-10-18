# A program that works with a return statement with multiple values.


def order_pizza():
    # Gather everyone's pizza preferences
    iron_man = "Pepperoni"
    captain_america = "Cheese"
    thor = "Meat Lovers"
    hulk = "Veggie Supreme"

    # Calculate the total number of pizzas needed.
    total_pizzas = 4
    # Calculate the size of each pizza based on the number of people.
    pizza_size = total_pizzas * 8

    # Assemble the team's preferences into a list
    team_preferences = [iron_man, captain_america, thor, hulk]

    return (
        pizza_size,
        team_preferences,
        "Successfuly delivered them all",
    )  # Note that the output here come into brackets thus becoming a tuple.

    # So accessing each result would call for unpacking for a tuple.


orders = order_pizza()
print(orders)

# Accessing each result now calls for unpacking the tuple in this way.
# pizzas, preferences = orders
# print(pizzas)
# print(preferences)

# When they are more value but you want to print few you assign others in an underscore e.g (_)
pizzas, preferences, _ = order_pizza()
print(pizzas)
print(preferences)
# print(message)
