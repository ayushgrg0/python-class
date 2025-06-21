# Advanced Inheritance

class Vehicle:
    def __init__(self, name) -> None:
        self.name = name

    def start(self):
        return f'{self.name} start bhayo!!'


class Car(Vehicle):
    def __init__(self, name, doors):
        super().__init__(name)
        self.doors = doors


mero_car = Car("Honda", "4")
print(mero_car.start())
