# A program about nested dictionaries.
fruit_categories = {
    "fruits": {
        "apple": {
            "color": "red",
            "taste": "sweet",
        },
        "banana": {
            "color": "yellow",
            "taste": "sweet",
        },
    },
    "vegetables": {
        "carrot": {
            "color": "orange",
            "taste": "crunchy",
        },
        "spinach": {
            "color": "green",
            "taste": "bitter",
        },
    },
}


# Spinch is a vegetable it has a bitter taste and it's green in color.


def food_item_description(fruit_name: str, food_item: dict):

    for food_item_type, food_description in food_item.items():

        for fruit_type, fruit_properties in food_description.items():
            if fruit_name == fruit_type:
                color = fruit_properties.get("color")
                taste = fruit_properties.get("taste")

                # Spinch is a vegetable it has a bitter taste and it's green in color.
                print(
                    f"{fruit_name} is a {food_item_type}, it has a {taste} taste and it's {color} in color."
                )


food_item_description("carrot", fruit_categories)
