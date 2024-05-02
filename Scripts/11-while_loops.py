prompt = "Tell me something and i'll repeat it back to you"
message=""
# while message != "quit":
#     message = input(prompt)
#     print(f"You said {message}")

# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     print(f"This time you said {message}")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(f"{current_number} is odd")


# Most of the time we'll use for in loops to do things with lists
# But you shouldn't modify a list while inside a for in loop that is iterating over it
# So if you're modifying the list you probably want to use a while loop

potential_clients=['bob', 'alice', 'candice', 'donald', 'edgar']
confirmed_clients=[]

while potential_clients:
    current_client = potential_clients.pop()
    accept = input(f"Should we take {current_client} on as a client? (type y to accept)")
    if accept == 'y':
        confirmed_clients.append(current_client)

print("Our confirmed clients are:")
for confirmed_client in confirmed_clients:
    print(confirmed_client.title())

animals = ['dog', 'cat', 'parrot', 'cat', 'cat']
print(animals)

while 'cat' in animals:
    animals.remove('cat')
print(animals)