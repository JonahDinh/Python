# Python provides the pathlib modules that makes it easier to work with files and directories
# without needing to worry about the OS details
from pathlib import Path

print(Path().absolute())

# We're going to create a path object pointing to a file we want to read
path = Path("./requirements.txt")

# By default there is a blank line
# Rstrip removes the blank line
contents = path.read_text().rstrip()
print(contents)

#Sometimes, you'll want to deal with it line by line
lines = contents.splitlines()
lineno = 1
for line in lines:
    print(f"{lineno}. {line}")
    lineno += 1


# Use sequence methods like slicing [2:6]

# Maybe I want my requirements.txt with just the package names, no version numbers, all on one line, comma seperated
requirements_string = ""
for line in lines:
    if requirements_string:
        requirements_string += ", "
    requirements_string += line[:line.find('==')]
print(requirements_string)