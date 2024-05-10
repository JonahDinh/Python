import numpy as np
from numpyhelpers import printnp

# In addition to a I I the usual index inq tricks, of course we can slice and index pass inq in other arrays for indices
number = np.arange(25).reshape(5, 5)
indexes_horizontal = np.array([2, 3, 1])
printnp(number)
printnp(indexes_horizontal)
printnp(number[indexes_horizontal])
index_vertical = np.array([0, 2, 1])
printnp(index_vertical)
# Must be the same shap or be broadcastable
printnp(number[indexes_horizontal, index_vertical])
indexes = (indexes_horizontal, index_vertical)
number[indexes] = 9999
printnp(number)

#By itself when you' re typing these in by hand it is hard to see the utility, but it can start
#to save a tot of work when you Gata to select or create more data

catagories = np.array(['Alpha', 'Bravo', 'Delta'])
data = np.array([
    [75, 30, 78 , 50, 32],
    [12 , 44, 12, 40, 1],
    [99, 2, 12, 44, 29]
])
printnp(data)

printnp(data.argmax(axis=1))
printnp(catagories[data.argmax(axis=0)])


# We can also index with boolean arrays
bools = np.array([True, False, True])
printnp(data[bools])

# This gets more interesting once you relaize you can use conditional operators to generate arrays of booleans
over_40 = data > 40
printnp(over_40)
printnp(data[over_40])

# What if we want to not just only return the values where it is true, but instead return
# different things
# Lots of function - including all ufuncs - can also take a where optional parameter
multiples_of_five_are_zero = np.where(data % 5 == 0, 0, data)
printnp(multiples_of_five_are_zero)

# What if you want to reduce your array to include only values where the test passes?
# If you ' re removing values, you' re going to change the shape. Remember, we can 't have a jagged array!
# So often you'll flatten it first
flat_fives_are_zeros = multiples_of_five_are_zero.flatten()
printnp(flat_fives_are_zeros)

(where_there_are_no_zeros,) = np.where(flat_fives_are_zeros != 0)
printnp(where_there_are_no_zeros)

no_zero = flat_fives_are_zeros[where_there_are_no_zeros]
printnp(no_zero)


my_employee_data = [
    ('Brad', 23.5, 11.2),
    ('Candice', 40.50, 5.6),
    ('Donald', 55, 22),
    ('Edgar', 19.33, 4),
    ('Faith', 18.50, 2),
    ('Gernald', 22.30, 5.2)
]

employees_structured_array = np.array(my_employee_data, dtype=[
    ('name', '<U20'),
    ('wage', 'float64'),
    ('tenure', 'float32')
])

printnp(employees_structured_array)
printnp(employees_structured_array['name'])
print(employees_structured_array['wage'].sum())
longterm_employees = np.where(employees_structured_array['tenure'] >= 5)
print(longterm_employees)
printnp(employees_structured_array['name'][longterm_employees])
print(employees_structured_array['wage'][longterm_employees].mean())