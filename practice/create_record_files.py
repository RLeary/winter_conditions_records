# Create some initial records in lists, so save_data works
from read_data_from_html import *
from record_class import *
import pickle

wh_records = []
eh_records = []
sh_records = []
nw_records = []
su_records = []

for i in range(4):
    wh_records.append(Record(10, i, date.today(), 'WH'))

for i in range(4):
    eh_records.append(Record(10, i, date.today(), 'EH'))

for i in range(4):
    sh_records.append(Record(10, i, date.today(), 'SH'))

for i in range(4):
    nw_records.append(Record(10, i, date.today(), 'NW'))

for i in range(4):
    su_records.append(Record(10, i, date.today(), 'SU'))



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