import pythonmodule
new_user = pythonmodule.create_user_profile("Wade", "Lahoda", role="Instuructor")
print(new_user)

import pythonmodule as pm
pm.greet_users(['alice', 'bob'])

from pythonmodule import create_pizza
print(create_pizza("Large", "Pepperoni"))

# DONT DO THIS:
from pythonmodule import *