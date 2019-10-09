# for current days forecast:
# http://www.mwis.org.uk/scottish-forecast/WH/ 
#
# format for next 2 days:
# if today is 01/10/2019 then next days web page address is:
# http://www.mwis.org.uk/scottish-forecast.asp?fa=WH&d=2019-10-02


from datetime import date

# datetime.date values

current_date = date.today()
#print("Today's date =", current_date, ", text after var")
print("Today's date =", current_date, ", text after var")

print("Current Year = ", current_date.year)
print("Current Month = ", current_date.month)
print("Current Day = ", current_date.day)
if current_date.weekday() == 2:
    print("Wed")


# Build string - this probably works - could maybe have a problem with 1st 9 
# days of month/1st months of year - eg 02 becomes 2
# Using f_string
web_address = f'http://www.mwis.org.uk/scottish-forecast.asp?fa=WH&d={current_date.year}-{current_date.month}-{current_date.day}'
print(web_address)