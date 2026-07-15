class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
class ElectricCar:
    def __init__(self, battery, make, model):
        self.battery = battery
        self.make = make
        self.model = model
    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Battery Capacity:", self.battery.capacity)
b = Battery(75)
car = ElectricCar(b, "Tesla", "Model S")
car.display()