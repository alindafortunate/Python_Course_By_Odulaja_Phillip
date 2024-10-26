# A program about method overiding with the super()
class Vehicle:
    def __init__(self, max_speed, model):
        self.max_speed = max_speed
        self.model = model

    def accelerate(self):
        print(
            f"The car {self.model} is accelerating but can't go above {self.max_speed}"
        )


class FasterVehicle(Vehicle):
    def __init__(self, max_speed, model):
        super().__init__(max_speed, model)
        self.max_speed = max_speed

    # method overiding.
    def accelerate(self):
        print(
            f"The car {self.model} is accelerating and can't accelerate beyond {self.max_speed}"
        )


vehicle1 = Vehicle(70, "Benz")
vehicle1.accelerate()

fasterVehicle1 = FasterVehicle(90, "Toyota")
fasterVehicle1.accelerate()
