from functools import reduce

# For this assignment we want to get
# the total revenue for all the fruits except for grapes.
sales_data = [
    {"product": "Apple", "quantity": 5, "price": 2.5},
    {"product": "Banana", "quantity": 10, "price": 1.75},
    {"product": "Oranges", "quantity": 8, "price": 3.0},
    {"product": "Grapes", "quantity": 3, "price": 4.25},
    {"product": "Mango", "quantity": 6, "price": 2.0},
]
# Soln
# You realise that here we need to filter out the grapes,
# then multiply the rest where by we can use the map function
# and then add the result to get the total revenue where by we can use the reduce function.
# since we want to chain this, therefore it is
# filter -> map -> reduce to get the output.
total_revenue = reduce(
    lambda prev, next: prev + next,
    (
        list(
            map(
                lambda sales: sales["quantity"] * sales["price"],
                list(filter(lambda data: data["product"] != "Grapes", sales_data)),
            )
        )
    ),
)

print(total_revenue)
