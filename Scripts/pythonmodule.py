def greet_users(names):
    """Say hello to a list of users"""
    for name in names:
        print(f"Hello, {name}")

def delete_bob(names):
    """We don't like Bobs so we'll remove any that are present"""
    while 'Bob' in names:
        names.remove('Bob')
    print(f"The post-Bob list is {names}")

def change_name(name):
    """Changes the name to bob"""
    name = "Bob"
    print(f"The name is now {name}")


def display_users(*users):
    for user in users:
        print(f"User: {user}")
    print(users)


def create_pizza(size, *toppings):
    pizza_string = f"{size} pizza with:"
    for topping in toppings:
        pizza_string += f"\n{topping}"
    return pizza_string


def create_user_profile(first, last, **user_info):
    user_info['name'] = first + " " + last
    return user_info

print("The code in the module was run")
