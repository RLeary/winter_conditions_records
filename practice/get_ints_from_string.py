# Get a list of ints from an input string
# MWIS temp or freezing level example:
# 10 rising to 12C inland, but staying near 9C around the coast

import re

input_string = "10 rising to 12C inland, but staying near 9C around the coast"

def get_ints_from_string(string):
    return re.findall(r'\d+', string)

ints = get_ints_from_string(input_string)
print(ints)

int_list = ['10', '12']

def get_average_int(ints):
    if len(ints) == 1:
        return ints[0]
    else:
        return sum(ints)/len(ints)