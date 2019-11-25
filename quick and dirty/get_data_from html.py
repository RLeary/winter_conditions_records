from urllib.request import urlopen
from statistics import mean
from datetime import date, timedelta
import re
import csv
import os

# Temperature at 900 can contain multiple temperatures, eg -2C rising to 1C
# I want average for the day, so use get ints_from_string() and get_average_int()
def get_ints_from_string(string):
    return [int(i) for i in re.findall(r'\d+|-\d+', string)]

# get_ints_from_string() returns negatives, was reading freezing level string 
# '1200-1300m, slowly litfing' returns [1200, -1300]
# Not matching '-' solves this for now
def get_ints_from_string_non_neg(string):
    return [int(i) for i in re.findall(r'\d+', string)]

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
    temp_at_900_string = strip_html_tags(temp_at_900)
    
    freezing_level_ints = get_ints_from_string_non_neg(freezing_level)
    if freezing_level_ints:
        freezing_level = get_average_int(freezing_level_ints)
    temp_at_900_ints = get_ints_from_string(temp_at_900_string)
    temp_at_900 = get_average_int(temp_at_900_ints)
    date_today = date.today()
    area_id = mwis_page[-3:-1]

    return [temp_at_900, freezing_level ,date_today, area_id, temp_at_900_string]

def create_csv_file(filename):
    csv_headers = ['Temperature at 900m', 'Freezing Level', 'Date', 'Area']
    ouput_csv = open(filename, 'w')
    output = csv.writer(ouput_csv)
    output.writerow(csv_headers)
    ouput_csv.close()

# For getting list of addresses for weekends
def build_mwis_weekend_pages(date):
    pages = []
    area_ids = ['WH', 'EH', 'SH', 'SU', 'NW']
    # Ensure that there is always 2 digits for the month and day
    month = f'{date:%m}'
    day = f'{date:%d}'
    for i in range(len(area_ids)):
        address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa={area_ids[i]}&d={date.year}-{month}-{day}'
        pages.append(address)
    return pages

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

for x in range(len(mwis_pages)):
    record = get_record(mwis_pages[x])
    csv_writer_file = open(csv_files[x], 'a', newline='')
    csv_writer = csv.writer(csv_writer_file)
    csv_writer.writerow(record)
    csv_writer_file.close()
    print(record)

# If day is friday, run for sat and sun as well
date_today = date.today()
sat_date = date_today + timedelta(days=1)
sun_date = date_today + timedelta(days=2)

if date_today.weekday() == 4:
    sat_mwis_pages = build_mwis_weekend_pages(sat_date)
    sun_mwis_pages = build_mwis_weekend_pages(sun_date)

    for i in range(len(mwis_pages)):
        sat_record = get_record(sat_mwis_pages[i])
        sun_record = get_record(sun_mwis_pages[i])
        # modify sat and sun records - get_record returns date.today()
        # and the last chars of the web address as the area id
        sat_record[2] = sat_date
        sun_record[2] = sun_date
        area_ids = ['WH', 'EH', 'SH', 'SU', 'NW']
        sat_record[3] = area_ids[i]
        sun_record[3] = area_ids[i]

        csv_writer_file = open(csv_files[i], 'a', newline='')
        csv_writer = csv.writer(csv_writer_file)
        csv_writer.writerow(sat_record)
        csv_writer.writerow(sun_record)
        csv_writer_file.close()

        print(sat_record)
        print(sun_record)