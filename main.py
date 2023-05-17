print("Welcome to the garage.")
class Vehicle:
    def __init__(self):
        self.make = None
        self.model = None

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_doors = None

    def set_num_doors(self, num_doors):
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.bed_length = None

    def set_bed_length(self, bed_length):
        self.bed_length = bed_length

    def get_bed_length(self):
        return self.bed_length

while True:
    print("Please select vehicle type:")
    print("1. Car")
    print("2. Truck")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        vehicle = Car()
        vehicle.set_make(input("Enter car make: "))
        vehicle.set_model(input("Enter car model: "))
        vehicle.set_num_doors(input("Enter number of doors: "))
    elif choice == "2":
        vehicle = Truck()
        vehicle.set_make(input("Enter truck make: "))
        vehicle.set_model(input("Enter truck model: "))
        vehicle.set_bed_length(input("Enter bed length: "))
    elif choice == "3":
        break
    else:
        print("Invalid choice")

    print(f"Vehicle make: {vehicle.get_make()}")
    print(f"Vehicle model: {vehicle.get_model()}")
 
    if isinstance(vehicle, Car):
        print(f"Number of doors: {vehicle.get_num_doors()}")
        print("Vehicle has been added to your garage.")
    elif isinstance(vehicle, Truck):
        print(f"Bed length: {vehicle.get_bed_length()}")
        print("Vehicle has been added to your garage.")