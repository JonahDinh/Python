# Python doesn't have arrays, it has lists.
# A list is a collection of items in a particular order.

# pythonic code convention for lists is they should be plurals
colors = ['red', 'green', 'purple', 'blue']
print(colors)
# Access an individual list items with [l exeactly you'd expect
print(colors[2])

# Obviously you can chain this with methodss attached to the values
print(colors[2].title())

# Or put it in an fstring
print(f"The third color is {colors[2]}")

# You can reassign list elements:
colors[2] = "Yellow"
print(f"The third color is now {colors[2]}")

# Error, obviously
#print(colors[9])
#colors[7] = 'teal'
#colors[4] = 'teal'
 
# To add:
colors.append('teal')
print(colors)

#Insert
colors.insert(1, 'magenta')
print(colors)

# Delete - use del to undefine it
del colors[3]
print(colors)

my_name = 'wade'
print(my_name)
del my_name
#print(my_name)

#Sometimes instead of just deleting an item, you want to remove it but
#get the value
print("Pop demo:")
print(colors)
print(colors.pop())
print(colors)

#Weirdly you can supply an index to pop
print(colors.pop(1))
print(colors)

#Remove by value
colors.remove('blue')
print(colors)

colors.append('purple')
colors.append('purple')
colors.append('purple')
print(colors)
colors.remove('purple')
print(colors)