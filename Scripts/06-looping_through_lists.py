heros = ['thor', 'ironman', 'hulk', 'hotguy']

#Python has for each loops
for hero in heros:
    print(f"The next hero is: {hero}")
    print("Lets loop again")

print("Done looping")

# Python provides a lot of tools for making working with lists of numbers easier

# It is very easy to generate a list of numbers using the range class
for number in range(1, 5):
    print(number)

#Start at 0
for number in range(5):
    print(number)


# You can put in a third argument to skip some amount
print("Skipping 2")
for number in range(1, 10, 2):
    print(number)

# c- style loop
for index in range(len(heros)):
    print(f"Hello #{index} is {heros[index]}")

my_numbers = range(1, 5)
print(my_numbers)
my_numbers = list(range(1,5))
print(my_numbers)

#Python has a bunch of standard
print(f"Min: {min(my_numbers)}")
print(f"Max: {min(my_numbers)}")
print(f"Sum: {sum(my_numbers)}")

# Let's say I want to assemble a list of squares of numbers 1 to 10
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Easy but here more compact: list comprehensions
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# Work with parts of lists using slice
planets=['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
print(planets)

# Slice using a colon to speify the first and last indexes of elements you want to work with
print(planets[3:6])

print(planets[:3])

print(planets[4:])

print(planets[-3:])

print(planets[-3: -1])

print (planets[2:7:2])

print(planets[::-1])


print(planets[2: 7: 1])


#Loop through a splice
for planet in planets[3:]:
    print(planet)
