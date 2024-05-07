def my_list(my_numbers): # takes the address
    my_numbers[0] = 10000 # complexe type
    return my_numbers
input_numbers = [1]
output_numbers = my_list(input_numbers)

def my_incrementer(my_number): # takes the value 1
    my_number = 10000 # basic type
    return my_number
input_number = 1
output_number = my_incrementer(input_number)


print('end')
# two categories of types in any languages
# 1. basic types: numbers, booleans, str
# 2. complexe types: list, dict, user defined classes
# in modern computers, your memory unit (box) size is usually 64 bits = 8 bytes
# basic types usually takes a single box to save the type
# complexe types, it can be as big as we want, so the box will contain only an address of it
# ASK YOURSELF, IS THE TYPE PASSED BY VALUE OR BY ADDRESS