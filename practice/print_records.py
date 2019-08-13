# print out data stored by save_data.py

from save_data import *

# I know these lines are longer than 80 chars
titles = ["West Highlands", "East Highlands", "Northwest Highlands", "Southern Highlands", "Southern Uplands"]
record_files = ["record_list_wh_file", "record_list_eh_file", "record_list_nw_file", "record_list_sh_file", "record_list_su_file"]

for x in range(titles):
    print titles[x]
    open record_files[x]
    print record