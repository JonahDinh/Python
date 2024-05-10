import numpy as np
from numpyhelpers import printnp

# One-d arrays can be indexed, sliced, and iterated over just like Python lists.

# multidimensional arrays can have one index, or slice, per dimension - pass them in a tuple (seperated by ,s)
threed_nums = np.arange(3*4*3).reshape(3, 4 , 3)
printnp(threed_nums)
printnp(threed_nums[2, 3, 1])
print("Slice:")
printnp(threed_nums[:,1:3,:2])
# If you give fewer indexes than there are dimensions, the missing indixies are considered complete slices
printnp(threed_nums[1:2])
# You can also use negatives just like in regular python
printnp(threed_nums[-1])
printnp(threed_nums[-1, -1, -1])

# If you want to flatten it out into an iterator to just go over every item you can use flat
for element in threed_nums.flat:
    print(element)

# Use flatten to flatten array
printnp(threed_nums.flatten())

# If you just want a view of an array that's flat not copy it:
printnp(threed_nums.ravel())

one = np.arange(15)
two = one * 3
printnp(one)
printnp(two)
# vstack takes a tuple of arrays and stacks them vertically:
print("Vertical: ")
printnp(np.vstack((one, two)))

print("Horizontal: ")
printnp(np.hstack((one, two)))

print("Column: ")
printnp(np.column_stack((one, two)))

printnp(np.column_stack((one, two)).transpose())

first = np.arange(25).reshape(5, 5)
second = first
printnp(second)
printnp(first)
second[2, 3] = 1000
printnp(second)
printnp(first)

second = first.view()
second = second.reshape(25)
second[10] = 99999
printnp(first)
printnp(second)