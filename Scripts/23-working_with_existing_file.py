from pathlib import Path


filename = input("What file would you like to add some content to? ")
path = Path(filename)

#Read in existing contnets
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"That file does not exist, so we'll create it.")
    contents = ""

contents += "\n" + input("Enter the text you want to add to the file:\n")
print("Writing:")
print(contents)
path.write_text(contents)