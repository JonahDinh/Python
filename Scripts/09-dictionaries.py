# Python tends to use dictionaries a lot
# A list of key value pairs
pepperoni_pizza = {'name':'pepperoni', 'price': 12.50, 'sauce': 'red'}
print(pepperoni_pizza)
print(pepperoni_pizza['price'])

# Dictionaries can have anything as the key(as long as it's hashable) and anything for the value
# Dictionaries can have anything as the value.
# They can also have anything as the key, as long as it is hashable.
# In practice, you should probably keep to integers and strings for keys
# unless you have a good reason to do otherwise.

movies = {
    54: 'E.T',
    72: 'Short Circuit',
    65: 'The last starfighter'
}

print(movies[72])

#You can add keys
movies[12] = 'Hatchi'
print(movies)


canadian_pizza = {}
canadian_pizza['Sauce'] = 'red'


for key in movies:
    print(f"Key {key}, is {movies[key]}")

# What happens if you try to access a key that doesn't exist?
# This wilt generate a key error:
# print peperoni'[size]')

# If you' re worried about a key not existing, you can use get

pizza_size = canadian_pizza.get('Size')
if pizza_size:
    print(f"(Out pizza is {pizza_size})")
else:
    print("We dont know how big this pizza is")


print(pepperoni_pizza.items())
for key, value in pepperoni_pizza.items():
    print(f"Key is {key} and value is {value}")