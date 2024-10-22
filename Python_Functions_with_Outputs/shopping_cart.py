# A program about the shopping cart exercise.

from typing import List


def discount_calculator(discount_percentage: float):
    shopping_mall = "Walmart"

    def discounted_cost(price_for_items: List):

        sum_of_costs = 0
        for i in price_for_items:
            sum_of_costs += i
        discounted_amount = sum_of_costs * discount_percentage / 100
        discounted_cost = sum_of_costs - discounted_amount
        return f" Your discount is {discounted_cost}, thank you for choosing {shopping_mall}"

    return discounted_cost


mangoes = 67.90
oranges = 678
apples = 450
tomatoes = 34

price_of_items = [mangoes, oranges, apples, tomatoes]
discount_percent = float(input("Enter the discount percentage: "))
calculated_discount = discount_calculator(discount_percent)
print(calculated_discount(price_of_items))
