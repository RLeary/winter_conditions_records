# load data from csv files, graph freezing levels etc.

import csv

csv_files = ['quick and dirty/wh_records.csv',
            'quick and dirty/eh_records.csv',
            'quick and dirty/sh_records.csv',
            'quick and dirty/su_records.csv',
            'quick and dirty/nw_records.csv'
            ]

def read_csv_file(csv_file):
    csv_data = []
    read_file = open(csv_file, 'r')
    csv_reader = csv.reader(read_file)
    for row in csv_reader:
        csv_data.append(row)
    read_file.close()
    return csv_data

#csvfile = read_csv_file(csv_files[2])
#print(csvfile)

for i in range(len(csv_files)):
xxx = read_csv_file(csv_files[i])