# A program to demonstrate the gettor and settor method.


class Car:
    def __init__(self, max_speed, model):
        self._max_speed = max_speed
        self._model = model

    # gettor method for max_speed
    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, new_speed):
        if new_speed > 100:
            print("The maximum speed can't be above 100")
        else:
            self._max_speed = new_speed

    def description(self):
        print(
            f"This car, model {self._model} has a maximum speed of {self.get_max_speed()}"
        )


prado = Car(80, "XYZ001")
prado.set_max_speed(101)
prado.description()
