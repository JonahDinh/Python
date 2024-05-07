class Dog:
    """Simple Dog Class"""
    total_tricks_done = 0
    
    def __init__(self, name, age):
        """Initialize a new dog object"""
        self.name = name
        self.age = age
        #The convention fro making something as private is to start it with an underscore
        self._tricks_done = 0

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
        self._tricks_done += 1
        Dog.get_tricks_done += 1

    def shit(self):
        """Simulate a dog shitting in response to a command"""
        print(f"{self.name} is now shitting")
        self._tricks_done += 1
        Dog.get_tricks_done += 1

    def roll_over(self):
        """Simulates a dog rolling over"""
        print(f"{self.name} rolls over")
        self._tricks_done += 1
        Dog.get_tricks_done += 1
    
    def get_total_tricks_done(self):
        return Dog.get_total_tricks_done
    
    def get_tricks_done(self):
        return self._tricks_done


fido = Dog("Fido", 2)
print(fido)

print(f"Fido's name is {fido.name}")

fido.sit()
fido.shit()
fido.roll_over()

print(f"{fido.name} is {fido.age} years old")
fido.age += 1
print(f"{fido.name} is {fido.age} years old")

print(f"Fido has done {fido.get_tricks_done()} tricks.")

Sally = Dog("Sally", 3)
print(f"Fido has done {Dog.get_total_tricks_done()} tricks.")

del Dog.get_total_tricks_done
print(f"{Sally.get_tricks_done}")
if 3<6:
    pass

