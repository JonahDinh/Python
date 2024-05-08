from pathlib import Path

path = Path('python.txt')
path.write_text("We're learning Python!")

path.write_text("We're learning even more Python!")

text_to_write = "We're learning Python"

path.write_text(text_to_write)

path.write_text(str(3333))