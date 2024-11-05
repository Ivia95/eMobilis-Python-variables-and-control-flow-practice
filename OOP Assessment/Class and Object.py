class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Car year: {self.year}")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_info() method
my_car.display_info()
