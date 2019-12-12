# load data from csv files, graph freezing levels etc.

import csv

csv_files = ['quick and dirty/wh_records.csv',
            'quick and dirty/eh_records.csv',
            'quick and dirty/sh_records.csv',
            'quick and dirty/su_records.csv',
            'quick and dirty/nw_records.csv'
            ]

class Record:
    def __init__(self, temp_at_900, freezing_level, date, area):
        self.freezing_level = freezing_level
        self.temp_at_900 = temp_at_900
        self.date = date
        self.area = area

    # Allow comparison of objects by their variables, fror finding any 
    # duplicates in lists
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.__dict__ == other.__dict__


# Return list of objects
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

# Return list of lists
def read_csv_file_return_list_of_lists(csv_file):
    csv_data = []
    read_file = open(csv_file, 'r')
    csv_reader = csv.reader(read_file)
    next(csv_reader)
    next(csv_reader)
    for row in csv_reader:
        csv_data.append(row)
    read_file.close()
    return csv_data

# delete duplicate dates in a list
def del_dup_dates(records_list):
    pass
#for i in range(len(records_list)-1):
#   if records_list[i].date == records_list[i+1].date:
#       del records_list[i]


wh_record_list = read_csv_file(csv_files[0])
eh_record_list = read_csv_file(csv_files[1])
sh_record_list = read_csv_file(csv_files[2])
su_record_list = read_csv_file(csv_files[3])
nw_record_list = read_csv_file(csv_files[4])

print(nw_record_list)
print(nw_record_list[2].date)