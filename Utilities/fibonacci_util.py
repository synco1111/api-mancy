from tokenize import String
from dotenv import load_dotenv
from sympy import true

"""
This is a fibonacci Utility which contain many fibonacci methods
"""
import math
import decimal
import pandas as pd
import numpy as np
from tabulate import tabulate
from vortex_math_calculator import digit_root_sum

load_dotenv("authentication_utils/.env")


def getFiboAtIndexWithDecimal(n):
    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = (1 + root_5) / 2

    a = ((phi**n) - ((-phi) ** -n)) / root_5

    return round(a)


def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


def formulaFib(n):
    root_5 = 5**0.5
    phi = (1 + root_5) / 2

    a = ((phi**n) - ((-phi) ** -n)) / root_5

    return round(a)


def createFibonacciList(listLength):
    # Create list of {listLength} of fibonacci values
    fib_list = []
    for i in range(listLength):
        fib_list.append(getFiboAtIndexWithDecimal(i))
    return fib_list


def fibo_list_generator(fibo_cycles=1, calculate_digital_root=True, show_steps=True):
    list_length = (
        fibo_cycles * 23
    )  # based on the idea that the sum of every 24 digits in the fibo sequence return 108
    fibo_list = []
    fibo_dict = {}
    for i in range(list_length):
        fibo_number = getFiboAtIndexWithDecimal(i)
        fibo_dict["original_fibo_number"] = fibo_number
        if calculate_digital_root:
            fibo_dict["digital_root_fib"] = digit_root_sum(fibo_number)
            if show_steps:
                fibo_dict["calculation steps"] = show_digital_root_calculation(fibo_number)
        fibo_list.append(fibo_dict.copy())
    return fibo_list


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def is_fibonacci_pattern(numbers_list):
    if type(numbers_list) is not list:
        numbers_list = [numbers_list]
    # if numbers_list is a single number (string or int):
    # n = int(numbers_list)
    # if is a list meaning is a sequence of number check rather they fibonacci or not
    isFibonacci = []
    for n in numbers_list:
        isFibonacci.append(isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4))
    isFibonacciDict = dict(zip(numbers_list, isFibonacci))
    return isFibonacciDict
    # https://www.geeksforgeeks.org/python-program-for-how-to-check-if-a-given-number-is-fibonacci-number/
    # for n in numbers_list
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square


def show_digital_root_calculation(number):
    # I want to display in the dataframe a column of calculation or at least start and end of it..(for large numbers)
    num_as_str = str(number)
    calc_steps_string = ""
    for digit in num_as_str[:-1]:
        calc_steps_string += str(digit) + " + "
    else:
        calc_steps_string += num_as_str[-1]
    return calc_steps_string


def tesla_numbers_df_filter(fib_df, nums_list=["3", "6", "9"]):
    tesla_fibo_df = fib_df[fib_df["digital_root_fib"].isin(nums_list)]
    return tesla_fibo_df


# 108 validation functions
def sum_fib_list_root(list):
    new_list = []
    for i in range(1, (len(list)), 24):
        new_list.append(sum(list[i : i + 23]))
    if len(list) % 2 == 0:
        new_list.pop()
    return new_list


def special_number_validator(list_sequence, special_num=108, is_fibo_sequence=True):
    # Handle both list or single integer as input
    if type(list_sequence) is not list:
        list_sequence = [list_sequence]
    #  Check if sequence/number sum to special_num (108):
    if sum(list_sequence) == special_num:
        return True
    else:
        return False


def sum_fib_list_root(list):
    result_list = []
    for i in range(1, len(list), 23):
        result_list.append(sum(list[i : i + 23]))
    return result_list
    # [sum(root_fib_list[i:i+24]) for i in range(0,3*(len(root_fib_list)//3),24)]
    # sum(root_fib_list[24*2+1:0+24*3]) # i = 25-24*2


# Run the function
if __name__ == "__main__":
    fibonacci__cycle_length = 1  # 1 each cycle generates 23 fibonacci sequence
    full_fib_list = fibo_list_generator(
        fibonacci__cycle_length, calculate_digital_root=True, show_steps=True
    )
    # extract only the fibonacci values from list of dicts:
    fib_list = [sub["original_fibo_number"] for sub in full_fib_list]
    # Check if values are fibonacci
    print(is_fibonacci_pattern(fib_list))

    # Add invalid values and check if fibonacci

    fib_df = pd.DataFrame(fib_list)
    # Convert the fibonacci root column to int
    fib_df["digital_root_fib"] = fib_df["digital_root_fib"].astype(int)

    first_nth_digits_in_sequence = fib_df["digital_root_fib"].tolist()
    is_108 = special_number_validator()
    print(is_108)
    result_list = sum_fib_list_root(fib_df["digital_root_fib"].tolist())
    print(tabulate(fib_df, headers="keys", tablefmt="psql"))
    [sum(fib_df["digital_root_fib"][i::2]) for i in range(len(fib_df["digital_root_fib"]))]
    # tesla_fib_df = tesla_numbers_df_filter(fib_df)
    # print(tabulate(tesla_fib_df, headers='keys', tablefmt='psql'))

    # tesla_list_string = map(str, tesla_list)
    # tesla_fibo_df = fib_df[fib_df['digital_root_fib'].isin(tesla_list_string)]
