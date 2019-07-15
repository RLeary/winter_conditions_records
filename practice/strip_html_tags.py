# Strip HTML tags from a line

# get freezing level line from mwis and print

from urllib.request import urlopen
import re

web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

try:
    response = urlopen(web_address)
except FileNotFoundError:
    print("Address not found")

for line in response:
    line = line.decode('utf-8')  # encoding while file in utf8
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