
def say_hello(name):
    """Says hello to name"""
    print(f"Hello, {name}")

def do_something(something):
    something("Something")

do_something(say_hello)

#Functions are objects- they just have a special "magic" or "dunder" method called call which
# gets created by the def statement (along with a bunch of other stuff), and gets catted when you
# invoke a function
say_hello.__call__("Call")

print(type("Hello"))
print(type(say_hello))