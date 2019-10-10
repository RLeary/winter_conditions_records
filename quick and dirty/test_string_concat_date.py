# for current days forecast:
# http://www.mwis.org.uk/scottish-forecast/WH/ 
#
# format for next 2 days:
# if today is 01/10/2019 then next days web page address is:
# http://www.mwis.org.uk/scottish-forecast.asp?fa=WH&d=2019-10-02


from datetime import date, timedelta

# datetime.date values

current_date = date.today()
#print("Today's date =", current_date, ", text after var")
print("Today's date =", current_date, ", text after var")

print("Current Year = ", current_date.year)
print("Current Month = ", current_date.month)
print("Current Day = ", current_date.day)
if current_date.weekday() == 2:
    print("Wed")

#tomorrow date
tomorrow_date = current_date + timedelta(days=1)

# day after tomorrow date
next_again_day = current_date + timedelta(days=2)

area_ids = ['WH,',
            'EH',
            'SH',
            'SU',
            'NW'
            ]

pages = []
next_day_pages = []
next_again_day_pages = []

# Build string - this probably works - could maybe have a problem with 1st 9 
# days of month/1st months of year - eg 02 becomes 2
# Using f_string
# This is the current days date - need next 2 days
for i in range(len(area_ids)):
    web_address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa={area_ids[i]}&d={current_date.year}-{current_date.month}-{current_date.day}'
    pages.append(web_address)
#print(pages)

for i in range(len(area_ids)):
    web_address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa={area_ids[i]}&d={tomorrow_date.year}-{tomorrow_date.month}-{tomorrow_date.day}'
    next_day_pages.append(web_address)
#print(next_day_pages)

for i in range(len(area_ids)):
    web_address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa={area_ids[i]}&d={next_again_day.year}-{next_again_day.month}-{next_again_day.day}'
    next_again_day_pages.append(web_address)
#print(next_again_day_pages)

def build_web_addresses(date):
    addresses = []
    area_ids = ['WH,', 'EH', 'SH', 'SU', 'NW']
    for i in range(len(area_ids)):
        address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa={area_ids[i]}&d={date.year}-{date.month}-{date.day}'
        addresses.append(address)
    return addresses

#print(build_web_addresses(date.today()))