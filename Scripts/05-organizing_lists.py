languages = ['Python', 'Javascript', 'C', 'C#']
print(languages)
#Use a sort to sort a list - change the list
languages.sort()
print(languages)

# sort can take an optional argument to reverse
# Note: that the boolean values True and False are capitalized in Python
# All of Python 'S build in constants are PascalCased
# other examples are None (used to represent the absence of a value),
# Not Implemented, Ellipsisl
languages.sort(reverse=True)
print(languages)

# Just temporarily sort something, you can use sorted
print("With sorted instead")
print(sorted(languages))
print(languages)

# reverse a list
years = [2020, 1997, 1999, 1853, 2021]
print(years)
years.reverse
print(years)

# you can get the length of the a list with the len function
print (len(years))
# Why len() as a seperate function instead of doing like years. len()? That's just how they did it
print(years.__len__())

# -1 gets the end of the list
print(years[-1])
print(years[-2])