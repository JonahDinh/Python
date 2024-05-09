# NumPY is the package for scientific computing in python
# Its main feature is a multidimensional homogenous array object,
# assorted dervied objects (like masked arrays and matrices), and
# a while bunch of routines for fast operations on arrays including
# math, logic, sorting, basic linear algebra, statistics, simulations, and more

# the ndarray object is the hear of NUmpy. It encapsulates a n-dimensional
#array of homogenous data types .
#Differences between np arrays and python lists:
# - fixed size creation - changing the size involves deleting and remaking
# - All elements must be of the same types, which means they'll be the same size
#   Note that these types could be python objects
# - Nurnpy optimizes for doing advanced mathematical operations on large amounts of dataT

# NumPy is fast because you write "vectorized" code with it - that is, you avoid
# explcit looping, indexing, etc and let numpy do that for you.

import numpy as np
from numpyhelpers import printnp

# Createing an array of the range of numbers from 0 to 15 (non-inclusive), reshape them into a 2d 3 by 5 array
my_np_array = np.arange(15).reshape(3, 5)
print(my_np_array)

# What traits do numpy arrays have?
# - ndmin - the number of dimensions or aces
print(my_np_array.ndim)
# The shape - dimesnsions of the array
print(my_np_array.shape)
# - dtype - the data type
print(my_np_array.dtype)
# - itemsize
print(my_np_array.itemsize)
# -data - reference to the data
print(my_np_array.data)
print(my_np_array.data.tolist())

printnp(my_np_array)
# creating Numpy arrays
# Lots of different ways you can do it
# You can pass in a list or tuple into the array function of numpy
# numpy will figure the type and size from
# to create a numpy array
#what you pass in
# REMEMBER: numpy arrays must be homogenous in type, and not be jagged

string_list = [["hi", "how", "are", "you"], ["goodbye", "see", "you", "later"]]
# specify the dtype
string_array = np.array(string_list, dtype="<U20")
printnp(string_array)


print(string_array[1][2])

string_array[1][2] = 'Mike'
printnp(string_array)

string_array[1][2] = 'the greatest show'
printnp(string_array)

# Often you'll know the size but not the contents
# (if you don't know the size you can't create it!)
# Growing arrays is expensive, so if you the final size best to allocate
# It all at once instead of copying a bunch of times
zeros = np.zeros((3, 4), dtype="int32")
printnp(zeros)
ones = np.ones((2, 2, 2))
printnp(ones)
empty = np.empty((20))
printnp(empty)

#often peoiple will arange, often reshaping it to a sspecific shape
arange = np.arange(10, 100, 5)
printnp(arange)
reshaped = arange.reshape(2, 3, 3)
printnp(reshaped)

# You can make any sequence into an array
# Want to tranform a string into an array of characters?
# Just make the string into a list, and then use that to create the array
my_greeting = "Hi how are doing?"
my_list = list(my_greeting)
print(my_list)
char_array = np.array(my_list)
printnp(char_array)