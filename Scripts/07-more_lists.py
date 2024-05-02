# What about copying lists?

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'teal']
print(colors)
new_colors = colors
print(new_colors)
new_colors[3] = 'orange'
print(new_colors)
print(colors)


# We didn't make a copy of a list, we made a copy of the reference!
# In python variables aren't labelsm they're labels for references that point to objects
#In python everything is an object

#Slice returns a copy
new_colors = colors[:]
new_colors[5] = "mauve"

print(colors)
print(new_colors)

# Sometimes you want a list that cannot change - that's what tuples are for.
# Python refers to values that cannot be changed as immutable - and an immutable list is a tuple
# They look exactly like lists, except you don't include the square brackets

instructors = "wade", "bryce" , "ernesto", "Jason"
print (instructors)
print (instructors[2])
#You can have a tuple with only one element - the comma makes it a tuple
tuple_of_one = "ernesto",
print(tuple_of_one)

#Type error
# instructors[1] = "ron"
instructors = ("wade", "ron", "ernesto", "jason")
print(instructors)