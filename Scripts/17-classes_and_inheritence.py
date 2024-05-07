class Car:
    """A simple representation of a car"""
    def __init__(self, make, model, year):
        """Initialize a new car"""
        self.make = make
        self.model = model
        self.year = year
        self._miles = 0

    def get_descriptive_name(self):
        descriptive_name = f"{self.year} {self.make} {self.model}"
        return descriptive_name
    
    def read_odometer(self):
        """Prints the odometer's reading"""
        print(f"This car has {self._miles} miles on it.")
    
    def update_odometer(self, milage):
        """Updates miles"""
        if milage > self._miles:
            self._miles = milage
        else:
            print("You can't roll back an odomter. that's illegal!")
    
    def __str__(self):
        """Returns a string representaiton of a car"""
        return f"{self.get_descriptive_name()} ({self._miles} miles)"
    
    def __call__(self):
        """When a car instance is called, it describes itself"""
        print (f"Beep-boop, I'm a {self.get_descriptive_name()} and I have {self._miles} on me")

    # Most "automatic" things in Python are relying on dunder or "maqic" functions.
    # If you want to override equals, or less than, length, etc you' re probably
    # just changing dunder functions.
# class BatteryPoweredDevice:
#     def __init__(self) -> None:
#         self.charge = 100.0

#     def print_charge(self):
#         print(f"This device is at {self.charge}% charge.")


# Let's subclass car with an electric car
class ElectricCar(Car):
    """Represnets the subset of cars which are electric cars"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = self.Battery(40)
    
    def describe_battery(self):
        # print(f"This car has a {self.battery.size}kwh battery")
        self.battery.display_charge()

    def read_odometer(self):
        """Override methods"""
        kms = self._miles * 1.609344
        print(f"This car has {kms} km on it")

    # You can have inner classes just using indeentation
    class Battery:
        """Represents a car battery"""
        def __init__(self, size):
            """Constructor"""
            self.size = size
            self.charge = 100.0

        def display_charge(self):
            print(f"The battery is at {self.charge}%")



impala = Car("Chevy", "Impala", 2013)
print(impala.get_descriptive_name())

impala.update_odometer(3000)
impala.read_odometer()
impala.update_odometer(200)
print(impala)
impala()

leaf = ElectricCar("Nissan", "Leaf", 2023)
print(leaf)
leaf.describe_battery()
leaf.update_odometer(4000)
leaf.read_odometer()
leaf.battery.display_charge()