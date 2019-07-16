# Practice for getting data from MWIS
# get freezing level line from mwis and print
# Strip HTML tags from a line

# 

from urllib.request import urlopen
import re

# Get a list of all ints in a string
def get_ints_from_string(string):
    return [int(i) for i in re.findall(r'\d+|-\d+', string)]

def get_average_int(ints):
    return int(sum(ints)/len(ints))

def strip_html_tags(line):
    html_tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    stripped_line = html_tag_re.sub('', line)
    stripped_line = stripped_line.strip() # re.sub leaving whitespace at start and end
    return stripped_line

# return freezing level and temp lines from mwis
# returns them as binary, needs converted to utf-8
def get_temp_and_freezing_level(mwis_page):
    try:
        response = urlopen(mwis_page)
    except FileNotFoundError:
        print("Address not found")
    
    for line in response:
        line = line.decode('utf-8')
        if 'Freezing Level' in line:
            freezing_level_raw = next(response)
            freezing_level = freezing_level_raw.decode('utf-8')
        if 'How Cold' in line:
            temp_at_900_raw = next(response)
            temp_at_900 = temp_at_900_raw.decode('utf-8')

    response.close()

    freezing_level = strip_html_tags(freezing_level)
    temp_at_900 = strip_html_tags(temp_at_900)
    
    if freezing_level != 'Above the summits.':
        freezing_level_ints = get_ints_from_string(freezing_level)
        freezing_level = get_average_int(freezing_level_ints)
    temp_at_900_ints = get_ints_from_string(temp_at_900)
    temp_at_900 = get_average_int(temp_at_900_ints)

    return freezing_level, temp_at_900

# Moving this into iterate_through_webpagespy
""" 
web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'
temp_at_900 = get_temp_and_freezing_level(web_address)

print(freezing_level)
print(temp_at_900)

area_id = web_address[-3:-1]
print(area_id)

freezing_level = '--10c or -12c'
if freezing_level != 'Above the summits.':
    freezing_level_ints = get_ints_from_string(freezing_level)
    freezing_level_int = get_average_int(freezing_level_ints)
    print(freezing_level_int)
print(freezing_level)
"""