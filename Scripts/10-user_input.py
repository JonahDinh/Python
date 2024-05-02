#message = input("Tell me something you want to print:")
#print(message)

# A lot of times you'll see programs build up a multi-line prompt string first
prompt = "If you give us your first name, we can customize it"
prompt+= '\nWhat is your first name?\n'
#name = input(prompt)
#print(f"Hello, {name}")


# Input will always return a string
birth_year = input("What year were you born?\n")
#age = 2024 - birth_year
#Can use int()
birth_year = int(birth_year)
age = 2024 - birth_year
print(f"You are {age} years old")

#There is also a float function