# load data from csv files, graph freezing levels etc.

import csv

csv_files = ['quick and dirty/wh_records.csv',
            'quick and dirty/eh_records.csv',
            'quick and dirty/sh_records.csv',
            'quick and dirty/su_records.csv',
            'quick and dirty/nw_records.csv'
            ]

## create dict of lists, so all area CSVs can be loaded into lists in a loop?
#from collections import defaultdict
#d = defaultdict(list)
#a = ['1', '2']
#for i in a:
#    for j in range(int(i), int(i) + 2):
#        d[j].append(i)
#print(d)
#print(d.items())

class Record:
    def __init__(self, temp_at_900, freezing_level, date, area):
        self.freezing_level = freezing_level
        self.temp_at_900 = temp_at_900
        self.date = date
        self.area = area

def read_csv_file(csv_file):
    csv_data = []
    read_file = open(csv_file, 'r')
    csv_reader = csv.reader(read_file)
    next(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        record = Record(row[0], row[1], row[2], row[3])
        csv_data.append(record)
    read_file.close()
    return csv_data

wh_record_list = read_csv_file(csv_files[0])
eh_record_list = read_csv_file(csv_files[1])
sh_record_list = read_csv_file(csv_files[2])
su_record_list = read_csv_file(csv_files[3])
nw_record_list = read_csv_file(csv_files[4])

print(nw_record_list)
print(nw_record_list[2].date)