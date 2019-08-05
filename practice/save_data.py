# Practice for getting data from MWIS
# iterate through WH, EH, NW, SH, SU

from read_data_from_html import *
from record_class import *
import pickle


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

# populate lists with stored data - pickle cant append a single line
with open('record_list_nw_file', 'rb') as in_file_nw:
    wh_records = pickle.load(in_file_nw)
with open('record_list_eh_file', 'rb') as in_file_eh:
    wh_records = pickle.load(in_file_eh)
with open('record_list_sh_file', 'rb') as in_file_sh:
    wh_records = pickle.load(in_file_sh)
with open('record_list_wh_file', 'rb') as in_file_wh:
    wh_records = pickle.load(in_file_wh)
with open('record_list_su_file', 'rb') as in_file_su:
    wh_records = pickle.load(in_file_su)

# Create new Record and append to relevant list
for i in range(len(web_addresses)):
    new_record = create_record(web_addresses[i])  
    if new_record.area_id == 'WH':
        wh_records.append(new_record)
    elif new_record.area_id == 'EH':
        eh_records.append(new_record)
    elif new_record.area_id == 'SH':
        sh_records.append(new_record)
    elif new_record.area_id == 'NW':
        nw_records.append(new_record)
    elif new_record.area_id == 'SU':
        su_records.append(new_record)

#for i in range(4):
#    nw_records.append(Record(10, i, date.today(), 'NW'))
#
#print(wh_records)
#print(eh_records)
#print(sh_records)
#print(nw_records)
#print(su_records)
#print(nw_records[2].temp_at_900)
#
# does not work for objects - write() is for strings
#out_file = open('record-list_nw', 'w')
#for line in nw_records:
#    out_file.write(line)
#out_file.close()

# Write Record lists to relevant files
out_file_nw = open('record_list_nw_file', 'wb')
pickle.dump(nw_records, out_file_nw)
out_file_nw.close()

out_file_eh = open('record_list_eh_file', 'wb')
pickle.dump(eh_records, out_file_eh)
out_file_eh.close()

out_file_wh = open('record_list_wh_file', 'wb')
pickle.dump(wh_records, out_file_wh)
out_file_wh.close()

out_file_sh = open('record_list_sh_file', 'wb')
pickle.dump(sh_records, out_file_sh)
out_file_sh.close()

out_file_su = open('record_list_su_file', 'wb')
pickle.dump(su_records, out_file_su)
out_file_su.close()

in_file = open('record_list_nw_file', 'rb')
nw_list = pickle.load(in_file)
in_file.close()
print(nw_list)
print(nw_list[2].temp_at_900)