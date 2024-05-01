# Python can do the usual operations
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2**3)

# Order of operations
print( 2 + 3 - 4 * 5 / 6 ** 7)

# You can mostly mix integers and floats together, you'll just get a float when you do 

my_int = 2
print (my_int)

my_float=3.0
print(my_float)

my_combined = my_int + my_float
print(my_combined)

# A nice little convenience feature, especially for large numbers, is that you can put
# big underscores in numbers and python ignores them
big_number = 99_234_865_324
print(big_number)

#python is strongly, dynamically typed
# Strongly in the sense that the type of a value (not a variable, but the value inside) doesn't change without explicit conversion
# Dynamically in that the runtime objects - values - have a type, but a variable does not

# You can put whatever you want inside a variable and the interpeter will not care.
# But, you can't for instance, treat a string as a number without explicitly saying so
my_string = "13"
my_number = my_string * 3
print(my_number)
my_string = 13
my_number = my_string * 3
print(my_number)