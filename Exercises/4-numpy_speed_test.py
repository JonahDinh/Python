from pathlib import Path
from numpyhelpers import time_f
import numpy as np

def convert_to_ints(char_list):
    """Converts a list of chars into ints"""
    return [int(x) for x in char_list]

def np_convert_to_ints(char_array):
    """Converts an array of chars into ints"""
    return char_array.astype("int32")

def sum_digits(int_list):
    """Sums a list of ints"""
    sum = 0
    for x in int_list:
        sum += x
    return sum

def np_sum_digits(int_array):
    """Sums an array of ints"""
    return int_array.sum()

def sum_of_squares(int_list):
    """Sums up the squares of every int in a list"""
    sum = 0
    for x in int_list:
        sum += x**2
    return sum

def np_sum_of_squares(int_array):
    """Sums up the squares of every int in an int array"""
    return (int_array * int_array).sum()

def sum_special(int_list):
    """Takes the list of ints, and for each int if it is odd multiplies it by 1.3 but if it is even
    divides it by 2. Sums the results and returns it"""
    sum = 0
    for x in int_list:
        sum += deal_with_special(x)
    return sum
    

def np_sum_special(int_array):
    """Takes any array of ints, and for each int if it is odd multiplies it by 1.3 but if it is even
    divides it by 2. Sums the results and returns it"""
    vectorized_deal_with_special = np.vectorize(deal_with_special)
    return vectorized_deal_with_special(int_array).sum()


def deal_with_special(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 1.3
    

# Insert here any set up code you need like reading in the file and breaking it apart into characters
path = Path("./lotsofpi.txt")
contents = path.read_text().rstrip()

pi_char_list = list(contents)
pi_char_array = np.array(pi_char_list)

int_list = time_f(convert_to_ints, pi_char_list)
int_array = time_f(np_convert_to_ints, pi_char_array)

pi_sum = time_f(sum_digits, int_list)
np_pi_sum = time_f(np_sum_digits, int_array)
print(f"Python said {pi_sum} is the sum and numpy said it is {np_pi_sum}")

sq_sum = time_f(sum_of_squares, int_list)
np_sq_sum = time_f(np_sum_of_squares, int_array)
print(f"Python said {sq_sum} is the sum of square rootsand np said {np_sq_sum}")

# root_sum = time_f(sum_of_roots,int_list)
# np_sq_sum = time_f(np_sum_of_roots, int_array)
# print(f"Python gave us a sum of square roots of {root_sum} and numpy gave us {np_sq_sum}")

weird_sum = time_f(sum_special, int_list)
np_weird_sum = time_f(np_sum_special, int_array)
print(f"For that weird sum, Python gave us {weird_sum} and numpy gave us {np_weird_sum}")