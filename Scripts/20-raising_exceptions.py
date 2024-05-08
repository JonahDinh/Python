def divide(first, second):
    return (int(first) / int(second))

divide(5, 10)
try:
    divide(10, 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    # Raise an exception to pass up
    #raise

# In Python not all exceptions are errors
# they' re just exceptions to the normal flow.
# Stoplteration, for instance, is an exception used to terminate iteration over iterators.
# If an exception is an Error, it ill end in Error.
# There also exceptions that end in Warning

#You can raise your own exceptions
raise Exception("There was a problem", 10, 5)