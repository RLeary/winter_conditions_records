# Strip HTML tags from a line

# get freezing level line from mwis and print

from urllib.request import urlopen
from django.utils.html import strip_tags
import re

"""
# strip_tags From django/utils/html.py
def strip_tags(value):
    # Return the given HTML with all tags stripped
    # Note: in typical case this loop executes _strip_once once. Loop condition
    # is redundant, but helps to reduce number of executions of _strip_once.
    value = str(value)
    while '<' in value and '>' in value:
        new_value = _strip_once(value)
        if len(new_value) >= len(value):
            # _strip_once was not able to detect more tags
            break
        value = new_value
   return value
"""


web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

decoded_line = ''

try:
    response = urlopen(web_address)
except FileNotFoundError:
    print("Address not found")

for line in response:
    line = line.decode('utf-8')  # encoding while file in utf8
    if 'Freezing Level' in line:
        freezing_level_raw = next(response)
        decoded_line = freezing_level_raw.decode('utf-8')

response.close()

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
stripped_html_line = tag_re.sub('', decoded_line)
stripped_html_line = stripped_html_line.strip()
print(stripped_html_line)