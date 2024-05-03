#Pass lists to functions
def greet_users(names):
    """Say hello to a list of users"""
    for name in names:
        print(f"Hello, {name}")

my_users = ['Alice', 'Bob', 'Candice', 'Donald', 'Edgar']
greet_users(my_users)

# Keep in mind a function gets the same reference to a list

def delete_bob(names):
    """We don't like Bobs so we'll remove any that are present"""
    while 'Bob' in names:
        names.remove('Bob')
    print(f"The post-Bob list is {names}")

delete_bob(my_users)
print(my_users)

def change_name(name):
    """Changes the name to bob"""
    name = "Bob"
    print(f"The name is now {name}")

my_name = "Wade"
print(my_name)
change_name(my_name)
print(f"My name is {my_name}")

def display_users(*users):
    for user in users:
        print(f"User: {user}")
    print(users)

display_users("Wade", "Bryce", "Ron")
#Sometimes you want to pass in arbriary number of arguments, but not in a list
#you can make an parametr a tuple with *

#If you mix positional arguments with arbitrary ones, the arbitrary ones have to come last
#Often, people will call this last "collector" argument *args
def create_pizza(size, *toppings):
    pizza_string = f"{size} pizza with:"
    for topping in toppings:
        pizza_string += f"\n{topping}"
    return pizza_string

print(create_pizza("Large", "Bacon", "Chicken", "Peppers"))

#Instead of accepting an arbitrary tuple, you can instead accept
#a arbitrary set of key value pairs as a dictionary:
#you use for that
#often you'll see **kwargs used to collect nonspecific arguments

def create_user_profile(first, last, **user_info):
    user_info['name'] = first + " " + last
    return user_info

user = create_user_profile("Wade", "Lahodea", role = "Instructor", program = "CST")
print(user)


stuff = "foo"

def do_stuff():
    """Does stuff"""
    print(f"Stuff is {stuff}")
    my_stuff = "more stuff"

do_stuff()
stuff = "bar"
do_stuff()
# print(my_stuff)
