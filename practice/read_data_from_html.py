# Practice for getting data from MWIS
# get freezing level line from mwis and print
# Strip HTML tags from a line

# 

from urllib.request import urlopen
from statistics import mean
from datetime import date
import re
from record_class import *

# Get a list of all ints in a string
def get_ints_from_string(string):
    return [int(i) for i in re.findall(r'\d+|-\d+', string)]

def get_average_int(ints):
    #return int(sum(ints)/len(ints))
    return int(mean(ints)) # use statistics standard lib mean()

def strip_html_tags(line):
    html_tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    stripped_line = html_tag_re.sub('', line)
    stripped_line = stripped_line.strip() # re.sub leaving whitespace at start and end
    return stripped_line

# Validate MWIS web address:
# mwis_re = re.compile('http://www.mwis.org.uk/scottish-forecast/'[SU]|[WH]|[EH][SU][SH][NW]/')
def validate_address(web_address):
    pass

# return freezing level and temp lines from mwis
# returns them as binary, needs converted to utf-8
def create_record(mwis_page):
    #validate_address(mwis_page)
    try:
        response = urlopen(mwis_page)
    except FileNotFoundError:
        print("Address not found")
    
    for line in response:
        line = line.decode('utf-8')
        if 'Freezing Level' in line:
            freezing_level_raw = next(response)  # decoded line, not next()
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
    date_today = date.today()
    area_id = mwis_page[-3:-1]

    new_record = Record(freezing_level, temp_at_900, date_today, area_id)
    return new_record