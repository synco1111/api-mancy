from hebrew_numbers import gematria_to_int, gematria_to_list_of_ints
from vortex_math_calculator import digit_root_sum, date_to_digit_root
import gematria_util as gu

if __name__ == '__main__':
    word = 'שלום רב מה נשמע'
    # There is a bug in the caluclation based on 
    # https://www.gimatria.co.il/?word=%D7%A9%D7%9C%D7%95%D7%9D
    # gematric_value = gematria_to_int(f'u{word}')
    gematric_value2 = gematria_to_list_of_ints(f'u{word}') 

    result = gu.nameToNumber(word, 'he')
    digi_root = digit_root_sum(gematric_value2) 
    # print(gematric_value)
