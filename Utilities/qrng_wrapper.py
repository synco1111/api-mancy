import quantumrand as qr

# NOTE https://github.com/identex/quantumrand
# rand_num = qr.get_data()
# print(type(rand_num) )
# print(rand_num)
def get_quantum_random_number():
    return qr.get_data(data_type="uint16", array_length=2)


# print(rand_num_uint16)
