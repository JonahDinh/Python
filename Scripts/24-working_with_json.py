from pathlib import Path
import json

path = Path("./my_setting.json")

# settings = {}
# settings['username'] = input("What is your username? ")
# content = json.dumps(settings)

# path.write_text(content)

# Read in json
try:
    settings = json.loads(path.read_text())
    print("We read: ")
    print(settings)
except FileNotFoundError:
    print("No setting exist yet. Creating settings for the first time.")
    settings = {}

# We could just check if the file exists
# if path.exists():
#     settings = json.loads(path.read_text())
#     print("We read: ")
#     print(settings)
# else:
#     print("No setting exist yet. Creating settings for the first time.")
#     settings = {}
if 'username' in settings:
    print(f"Your current username is {settings['username']}")
else:
    print("You currently have no username set")

new_username = input("Enter username to save: (press enter) ")
if new_username:
    settings['username'] = new_username

if 'language' in settings:
    print(f"Your current default language is {settings['language']}")
else:
    print("You currently have no default language.")

new_langauge = input("Enter default language to save: (press enter to leave unchanged) ")
if new_langauge:
    settings['language'] = new_langauge

print(settings)

path.write_text(json.dumps(settings))