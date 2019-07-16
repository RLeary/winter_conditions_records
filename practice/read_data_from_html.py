# Practice for getting data from MWIS
# get freezing level line from mwis and print
# Strip HTML tags from a line

# 

from urllib.request import urlopen
import re

# Get a list of all ints in a string
def get_ints_from_string(string):
    # One line:
    #return [int(i) for i in re.findall(r'\d+', string)]
    string_list = re.findall(r'\d+', string)
    int_list = [int(i) for i in string_list]
    return int_list

def get_average_int(ints):
    if len(ints) == 1:
        return ints[0]
    else:
        return sum(ints)/len(ints)

web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

try:
    response = urlopen(web_address)
except FileNotFoundError:
    print("Address not found")

for line in response:
    line = line.decode('utf-8')
    if 'Freezing Level' in line:
        freezing_level_raw = next(response)
        decoded_line_freezing = freezing_level_raw.decode('utf-8')
    if 'How Cold' in line:
        temp_at_900_raw = next(response)
        decoded_line_temp = temp_at_900_raw.decode('utf-8')

response.close()

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

freezing_level = tag_re.sub('', decoded_line_freezing)
freezing_level = freezing_level.strip()

temp_at_900 = tag_re.sub('', decoded_line_temp)
temp_at_900 = temp_at_900.strip()

print(freezing_level)
print(temp_at_900)

area_id = web_address[-3:-1]
print(area_id)

freezing_level = '10c or 34c'
if freezing_level != 'Above the summits.':
    freezing_level_ints = get_ints_from_string(freezing_level)
    freezing_level_int = get_average_int(freezing_level_ints)
    print(freezing_level_int)
print(freezing_level)
