message = "Hello python world!"
print(message)

message = "Hello again"
print(message)

# Varaible names in pyton can contain only letters, numbers and underscores. They annot start with a number.
# Good python variable name practive for local variables is all lowercase, use underscores to seperate words.

localVariable = "not a good python variable name"
local_variable = "a good python variable name"

# This will generate an error - but the interpreter will try to guess what you mean!
#print(massage)

# Anything you put inside quotes - whether single or double - is a string
name = 'wade lahoda'
# String is python have a bunch of built in methods
print(name.title())

#There's upper and lower
print(name.upper())
print(name.lower())

# You can use variable inside of a string by using an f-string - the f is for format
last = 'lahoda'
first = 'wade'
full_name = f'{first} {last}'
print (f"Hello, {full_name}")

# New lines
long_message = "Hello, welcome to \t\tIntro to Python\n\tHope it's useful!\n"
print(long_message)

#Frequently when we're parsing stuff we'll be concerned about cleaning up whitespace
# strings have an rstrip method that will return the string with extra spaces on the right removed
extra_spaces = "           This string      has some extra whitespace        "
print(f"The string rstripped is '{extra_spaces.rstrip()}'")
# Note that rstring does not modify the original
print(f"The original string is '{extra_spaces}'")
print(f"Lstripped it is '{extra_spaces.lstrip()}'")

# You can chain them together
print(f"lsripped and then rstripped: '{extra_spaces.lstrip().rstrip()}'")


# Remove prefix with removeprefix
my_url = "http://www.saskpolytech.ca"
print(f"{my_url.removeprefix('http://')}")

# Concatenation
first = "First"
second = "Second"
both = first + " " + second
print(both)
both += " Third"
print(both)