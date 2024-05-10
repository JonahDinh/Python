import numpy as np
from numpyhelpers import printnp
import matplotlib.pyplot as plt

# Let's load in some transistor data
raw_data = np.loadtxt("transistor_data.csv", delimiter=",", usecols=[1, 2], skiprows=1)
printnp(raw_data)

a_years = raw_data[:,1].astype('int32')
printnp(a_years)
a_trans = raw_data[:,0].astype('int64')
printnp(a_trans)

# plt.plot(a_years, a_trans, 'bo')

# There •s a convenience wrapper for matplotlib that'll plot things
# on a semilo scale for one axis
plt.semilogy(a_years, a_trans, 'bo', label="Transistor Count", alpha = 0.2)
#plt.show()

# Can we get the mean for each year?
year_range = np.atleast_2d(np.arange(1971, 2020)).transpose()
printnp(year_range)
year_mask = np.where(a_years == year_range, True, False)
printnp(year_mask)
transistors_for_each_year = np.where(year_mask, a_trans, 0)
printnp(transistors_for_each_year)
mean_trans_for_each_year = transistors_for_each_year.sum(axis=1)/np.count_nonzero(transistors_for_each_year, axis=1)
printnp(mean_trans_for_each_year)
plt.plot(year_range, mean_trans_for_each_year, "g+", markersize=14, mew = 2, label = "Average Transistor Count")


START_YEAR = 1971
START_TRANS = 2250

moores_law = lambda year : START_TRANS * 2 ** ((year - START_YEAR) / 2)

# Lets generate an array
a_moores_trans = moores_law(a_years)

plt.plot(a_years, a_moores_trans, label = "Moore's Law")
#plt.show()

# Let's make the assumption that the data grows exponentially as a funciton of the year
# Can we find the constants we need to make that true?

# I want to find the constants to do a lineear equation to get that value we're squaring
# Numpy has a funciton to find us the data for a best fit polynomial line!
model = np.polynomial.Polynomial.fit(a_years, np.log(a_trans), deg=1)
print(model)

model = model.convert()
print(model)
linear_constant, linear_coeffient = model
a_trans_best_fit = np.exp(linear_constant) * np.exp(linear_coeffient * a_years)
#Remember the equation for a line?
print(f"Transistors will be mutiplied every two years at a rate of {np.exp(linear_coeffient * 2)}")

plt.plot(a_years, a_trans_best_fit, label = "Linear Regression")
plt.legend(loc="upper left")
plt.show()