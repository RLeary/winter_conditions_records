# Practice for getting data from MWIS
# iterate through WH, EH, NW, SH, SU

from read_data_from_html import *
from datetime import date
from record_class import *


web_addresses = ['http://www.mwis.org.uk/scottish-forecast/WH/', 
    'http://www.mwis.org.uk/scottish-forecast/EH/', 
    'http://www.mwis.org.uk/scottish-forecast/SH/', 
    'http://www.mwis.org.uk/scottish-forecast/NW/', 
    'http://www.mwis.org.uk/scottish-forecast/SU/']

for i in range(len(web_addresses)):
    record = []
    freezing_level, temp = get_temp_and_freezing_level(web_addresses[i])
    area_id = web_addresses[i][-3:-1]
    date_today = date.today()
    
    newRecord = Record(freezing_level, temp, area_id, date_today)
    print(newRecord.freezing_level)
    print(newRecord.date_today)
    
    #record.append(freezing_level)
    #record.append(temp)
    #record.append(date_today)
    #record.append(area_id)
    #print(record)
    #print(freezing_level, temp, area_id, date_today)

"""
    record.freezing_level = ..
    record.temp = .
    record.date_today
    record.area_id
    record_list.append(record)
"""