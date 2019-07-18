# Practice for getting data from MWIS
# iterate through WH, EH, NW, SH, SU

from read_data_from_html import *
from record_class import *


# using lists for testing
# use sql later
wh_records = []
eh_records = []
sh_records = []
nw_records = []
su_records = []

web_addresses = ['http://www.mwis.org.uk/scottish-forecast/WH/', 
    'http://www.mwis.org.uk/scottish-forecast/EH/', 
    'http://www.mwis.org.uk/scottish-forecast/SH/', 
    'http://www.mwis.org.uk/scottish-forecast/NW/', 
    'http://www.mwis.org.uk/scottish-forecast/SU/']

for i in range(len(web_addresses)):
    new_record = create_record(web_addresses[i])  

    print(new_record.temp_at_900)
    print(new_record.freezing_level)
    print(new_record.date_today)
    print(new_record.area_id)

    if new_record.area_id == 'WH':
        wh_records.append(new_record)

for i in range(4):
    nw_records.append(Record(10, i, date.today(), 'NW'))

print(wh_records)
print(eh_records)
print(sh_records)
print(nw_records)
print(su_records)
print(nw_records[2].temp_at_900)