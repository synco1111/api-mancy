"""
This is a fibonacci Utility which contain many fibonacci methods
"""    
import math
import decimal
import pandas as pd
from tabulate import tabulate
from vortex_math_calculator import digit_root_sum

def getFiboAtIndexWithDecimal(n):
    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

def formulaFib(n):
    root_5 = 5 ** 0.5
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

def createFibonacciList(listLength):
    # Create list of {listLength} of fibonacci values 
    fib_list = []
    for i in range(listLength):
        fib_list.append(getFiboAtIndexWithDecimal(i))
    return fib_list

def fibo_list_generator(list_length, calculate_digital_root=True, show_steps=True):
    fibo_list = []
    fibo_dict = {}
    for i in range(list_length):
        fibo_number = getFiboAtIndexWithDecimal(i)
        fibo_dict['original_fibo_number'] = fibo_number
        if calculate_digital_root:
            fibo_dict['digital_root_fib'] = digit_root_sum(fibo_number)
            if show_steps:
                fibo_dict['calculation steps'] = show_digital_root_calculation(fibo_number)
        fibo_list.append(fibo_dict.copy())
    return fibo_list

    # Create list of digital root {list_length} of fibonacci values
    digital_root_fib_list = createFibonacciList(list_length)
    # https://realpython.com/python-map-function/
    gen_exp = (digit_root_sum(x) for x in digital_root_fib_list)
    digital_root_fib_list = list(gen_exp)
    return digital_root_fib_list

def is_fibonacci_pattern(numbers_list):

    # TODO: Implement is_fibonacci_pattern
    # Fibonacci

    # Get a list,pair or a single number and check if its based on fibonachi number
    pass

def show_digital_root_calculation(number):
    # DONE: Implement show_digital_root_calculation
    # I want to display in the dataframe a column of calculation or at least start and end of it..(for large numbers)
    num_as_str = str(number)
    calc_steps_string = ''
    for digit in num_as_str[:-1]:
        calc_steps_string += str(digit) + ' + '
    else:
        calc_steps_string += num_as_str[-1]
    return calc_steps_string

def tesla_numbers_df_filter(fib_df, nums_list = ['3', '6', '9']):
    tesla_fibo_df = fib_df[fib_df['digital_root_fib'].isin(nums_list)]
    return tesla_fibo_df
# fib_df = pd.
# print(tabulate(fib_df, headers='keys', tablefmt='psql'))

fib_list = fibo_list_generator(20, calculate_digital_root=True, show_steps=True)
fib_df = pd.DataFrame(fib_list)
print(tabulate(fib_df, headers='keys', tablefmt='psql'))
tesla_fib_df = tesla_numbers_df_filter(fib_df)
print(tesla_fib_df)
# tesla_list = [3, 6, 9]
# tesla_list_string = map(str, tesla_list)
# tesla_fibo_df = fib_df[fib_df['digital_root_fib'].isin(tesla_list_string)]