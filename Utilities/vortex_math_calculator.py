# The purpose of the following class is to validate numbers based on known sacred patterns

def summing2(number):
    if number == 0: return 0
    if len(str(number)) == 1:
        return number
    return abs(number) % 9 or 9

def digit_root_sum(number, show_sum_steps = True):
    number_length = len(str(number))
    sum_of_digits = number
    singularity_counter = 1
    calc_steps_string = ''
    while number_length > 1:
        sum_of_digits = 0
        for digit in str(number):
            sum_of_digits += int(digit)
        number_length = len(str(sum_of_digits))
        number = sum_of_digits
        singularity_counter += 1
    return str(sum_of_digits) #, singularity_counter

def three_six_nine_checker(number):
    result = digit_root_sum(number)
    # result, counter = digit_root_sum(number)
    vortex_dict = {
        "original_value": number,
        "summing_value": result,
        "pattern": 0,
        # "signulrity_counter": counter
    }
    if result == 9:
        vortex_dict["pattern"] = 9
        return vortex_dict
    elif result == 6:
        vortex_dict["pattern"] = 6
        return result
    elif result == 3:
        vortex_dict["pattern"] = 3
    return vortex_dict

# Todo:
"""
1. Add numerology checker
2. Add Gematria checker
3. Add Fibonacci checker
4. Add Kabala checker
"""