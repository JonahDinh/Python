class Dog:
    """Simple Dog Class"""

    
    def __init__(self, name, age):
        """Initialize a new dog object"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def shit(self):
        """Simulate a dog shitting in response to a command"""
        print(f"{self.name} is now shitting")


fido = Dog("Fido", 2)
print(fido)

print(f"Fido's name is {fido.name}")

fido.sit()
fido.shit()