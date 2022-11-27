# The purpose of the following class is to validate numbers based on known sacred patterns

import math


def summing2(number):
    if number == 0: return 0
    if len(str(number)) == 1:
        return number
    return abs(number) % 9 or 9

def digit_root_sum(input_to_reduce, tesla_pattern = False):
    # handle as input as string and remove any non-digit charecter
    number_to_reduce = ''.join(filter(str.isdigit, str(input_to_reduce)))
    number_length = len(str(number_to_reduce))
    sum_of_digits = number_to_reduce
    singularity_counter = 1
    while number_length > 1:
        sum_of_digits = 0
        for digit in str(number_to_reduce):
            sum_of_digits += int(digit)
        number_length = len(str(sum_of_digits))
        number_to_reduce = sum_of_digits
        singularity_counter += 1
    if tesla_pattern:
        return three_six_nine_checker(sum_of_digits)

    return str(sum_of_digits) #, singularity_counter

def three_six_nine_checker(number, return_bool = True):
    result = digit_root_sum(number)
    tesla_arr = ['3', '6', '9']
    if return_bool:
        if result in tesla_arr:
            return True
    else:
        # result, counter = digit_root_sum(number)
        vortex_dict = {
            "original_value": number,
            "summing_value": result,
            "pattern": 0,
            # "signulrity_counter": counter
        }
        if result == '9':
            vortex_dict["pattern"] = 9
            return vortex_dict
        elif result == '6':
            vortex_dict["pattern"] = 6
            return result
        elif result == '3':
            vortex_dict["pattern"] = 3
        return vortex_dict

def date_to_digit_root(date):
    #  split and convert to int
    split_date = date.split('/')
    # Sum all nums
    summed_date = sum(list(map(int, split_date)))
    return digit_root_sum(summed_date)

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
    
def is_fibonacci_pattern(numbers_list):
    if type(numbers_list) is not list: numbers_list = [ numbers_list ]
    # if numbers_list is a single number (string or int):
    # if list contain strings convert to strings
    if isinstance(numbers_list[0], str):
        numbers_list = list(map(int, numbers_list))
    # n = int(numbers_list)
    # if is a list meaning is a sequence of number check rather they fibonacci or not
    isFibonacci = []
    for n in numbers_list:
        isFibonacci.append(isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4))
    isFibonacciDict = dict(zip(numbers_list, isFibonacci))
    return isFibonacciDict

if __name__ == '__main__':
    # sandbox:
    list_of_dates = ['05/02/2022', '05/05/1986', '12/03/1987'] # ==> [7+6,10+24,15+25] => [4,7,4] => [15] => [6]
    list_numbers_str = ['432', '528', '1111', '1234'] # => [9, 6, 4, 1] => [2]
    list_numbers_int = [432, 528, 1111, 1234] # => [9, 6, 4, 1] => [2]
    list_of_strings_english = ['Daniel', 'Danit', 'Zeev']
    list_of_strings_hebrew = ['דניאל', 'דנית', 'זאב']

    nine_root = digit_root_sum(list_numbers_str[0], True)
    print(nine_root)
    # print(date_to_digit_root(date))
    # Todo:
    """
    1. Add numerology checker
    2. Add Gematria checker
    3. Add Fibonacci checker
    4. Add Kabala checker
    """