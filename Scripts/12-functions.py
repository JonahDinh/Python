def say_hello():
    """Say Hello."""
    print("Hello!")

say_hello()


def say_hello_name(name):
    """Say hello to a named person"""
    print(f"Hello, {name}")

say_hello_name("Wade")

def say_hello_with_title(title, name):
    """Say hello to a named person"""
    print(f"Hello, {title.title()} {name.title()}")

say_hello_with_title("Mr.", "Wade")


# You can have optional params 
def greet(name, greeting="Hello"):
    """Greets someone by name with optional greeting"""
    print(f"{greeting}, {name}")

greet("Wade", "Wassup")
greet("Wade")

# Return
def get_polite_greeting(name, title, greetings="Hello"):
    """Returns a polite greeting"""
    polite_greeting = f"{greetings}, {title.title()}. {name}"
    return polite_greeting


my_greeting = get_polite_greeting("Wade", "Mr", "Bonjour")
print(my_greeting)

# If you want an optional argument, it is fine to make the default be "" or None
def get_optionally_polite_greeting(name, title="", greeting="Hi"):
    """Generates an optionally polite greeting"""
    if title:
        polite_greeting = f"{greeting}, {title.title()}. {name}"
    else:
        polite_greeting = f"{greeting}, {name}"
    return polite_greeting

my_greeting = get_optionally_polite_greeting("Wade", "Mr", "Sup")
print(my_greeting)

my_greeting = get_optionally_polite_greeting("Wade")
print(my_greeting)

my_greeting = get_optionally_polite_greeting("Wade", greeting="Howdy")
print(my_greeting)


my_greeting = get_optionally_polite_greeting(name = "Wade", greeting="Greetings")
print(my_greeting)

def get_greeting_with_bill(name, total=None):
    if total:
        greeting = f"Hello {name}, you owe us ${total} dollars"
    else:
        greeting = f"Hello {name}, you don't appear to have an account with us"
    return greeting

print(get_greeting_with_bill("Wade"))
print(get_greeting_with_bill("Bryce", 50))
print(get_greeting_with_bill("Ron", 0))

# The following values are falsy in Python:
# - The number 0
# -The number O
# -The boolean value False
# -The empty string
# -None
# -An empty list
# -An empty tuple
# -An empty dictionary

if None == False:
    print("None is equal to false")
else:
    print("None is not equal to false")

if None:
    print("None is not falsey")
else:
    print("None is falsey")


