import numpy as np
from numpyhelpers import printnp
import matplotlib.pyplot as plt

my_data = np.array([33,2,3,14,61,22])

plt.plot(my_data)

evenly_spaced_numbers = np.linspace(50, 1000, 20)
more_numbers = np.linspace(0,100,20)
plt.plot(evenly_spaced_numbers)
#plt.show()
plt.plot(evenly_spaced_numbers, more_numbers)
# you can clear the plot with
#plt.clf()
plt.show()

