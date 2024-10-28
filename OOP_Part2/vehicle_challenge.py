# A program to demonstrate the vehicle Hierarchy


class Vehicle:
    def __init__(self, manufacture: str, model: str, year: int):
        self.manufacture = manufacture
        self.model = model
        self.year = year

    def get_details(self):
        print(
            f"This {self.model} was manufactured by {self.manufacture} in {self.year}"
        )


class Car(Vehicle):
    def __init__(self, manufacture, model, year, num_doors: int):
        super().__init__(manufacture, model, year)
        self.num_doors = num_doors

    def get_details(self):
        print(
            f"This {self.model} was manufactured by {self.manufacture} in {self.year} and has {self.num_doors} doors."
        )


class Motorcycle(Vehicle):
    def __init__(self, manufacture, model, year, top_speed: float):
        super().__init__(manufacture, model, year)
        self.top_speed = top_speed

    def get_details(self):
        print(
            f"This {self.model} was manufactured by {self.manufacture} in {self.year} and has a top speed of {self.top_speed}."
        )


class Truck(Car, Vehicle):
    def __init__(self, manufacture, model, year, num_doors, cargo_capacity: float):
        super().__init__(manufacture, model, year, num_doors)
        self.cargo_capacity = cargo_capacity

    def get_details(self):
        print(
            f"This {self.model} was manufactured by {self.manufacture} in {self.year}, has {self.num_doors} doors and can carry a maximum of {self.cargo_capacity} tonnes."
        )


car = Car("Toyota", "Nissan", 2000, 4)
car.get_details()

motorcycle = Motorcycle("Toyota", "Suzuki", 2009, 120)
motorcycle.get_details()

truck = Truck("Toyota", "SinoTruck", 2013, 4, 1000)
truck.get_details()
