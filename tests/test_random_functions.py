from Utilities.qrng_wrapper import get_quantum_random_number
from Utilities import vortex_math_calculator as vortex_math

def test_randomness():
    for i in range(100):
        random_number = get_quantum_random_number()
        print(f"Asserting {random_number[0]}...")
        assert vortex_math.digit_root_sum(random_number[0])[0] == vortex_math.summing2(random_number[0])
        print(f"{random_number[0]} Passed..")