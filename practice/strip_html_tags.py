# Strip HTML tags from a line

# get freezing level line from mwis and print

from urllib.request import urlopen
import re

web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

line_with_tags = ''

try:
    response = urlopen(web_address)
    for line in response:
        line = line.decode('utf-8')
        if 'Freezing Level' in line:
            freezing_level_raw = next(response)
            print(line)
            print(freezing_level_raw)    
            line_with_tags = freezing_level_raw      
except FileNotFoundError:
    print("Address not found")
response.close()

print(line_with_tags)