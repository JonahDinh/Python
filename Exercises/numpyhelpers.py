from time import perf_counter_ns as timer

def printnp(array):
    print(array)
    print(f"Shape: {array.shape}, Dimensions: {array.ndim}")
    print(f"Datatype: {array.dtype}, item size: {array.itemsize}")

def time_f(function, args):
    '''Run function passing in args. Print how long the function took to run and return the return value of the function'''
    start_time = timer()
    ret_val = function(args)
    total_time = (timer() - start_time)/ 1000000
    print(f"{function.__name__} took {total_time} ms to complete")
    return ret_val