from urllib.request import urlopen
from statistics import mean
from datetime import date
import re
import csv
import os

# Temperature at 900 can contain multiple temperatures, eg -2C rising to 1C
# I want average for the day, so use get ints_from_string() and get_average_int()
def get_ints_from_string(string):
    return [int(i) for i in re.findall(r'\d+|-\d+', string)]

# I only want the average temp for a given day
def get_average_int(ints):
    return int(mean(ints))

def strip_html_tags(line):
    html_tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    stripped_line = html_tag_re.sub('', line)
    stripped_line = stripped_line.strip() # re.sub leaving whitespace at start and end
    return stripped_line

def get_record(mwis_page):
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

    return [temp_at_900, freezing_level ,date_today, area_id]

def create_csv_file(filename):
    csv_headers = ['Temperature at 900m', 'Freezing Level', 'Date', 'Area']
    ouput_csv = open(filename, 'w')
    output = csv.writer(ouput_csv)
    output.writerow(csv_headers)
    ouput_csv.close()


mwis_pages = ['http://www.mwis.org.uk/scottish-forecast/WH/', 
            'http://www.mwis.org.uk/scottish-forecast/EH/',
            'http://www.mwis.org.uk/scottish-forecast/SH/',
            'http://www.mwis.org.uk/scottish-forecast/SU/',
            'http://www.mwis.org.uk/scottish-forecast/NW/'
            ]

csv_files = ['quick and dirty/wh_records.csv',
            'quick and dirty/eh_records.csv',
            'quick and dirty/sh_records.csv',
            'quick and dirty/su_records.csv',
            'quick and dirty/nw_records.csv'
            ]


for i in range(len(csv_files)):
    if not os.path.exists(csv_files[i]):
        create_csv_file(csv_files[i])
        #open(csv_files[i], 'w').close()


for x in range(len(mwis_pages)):
    test_record = get_record(mwis_pages[x])
    csv_writer_file = open(csv_files[x], 'a', newline='')
    csv_writer = csv.writer(csv_writer_file)
    csv_writer.writerow(test_record)
    csv_writer_file.close()
    print(test_record)