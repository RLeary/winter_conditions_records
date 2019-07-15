# Strip HTML tags from a line

# get freezing level line from mwis and print

from urllib.request import urlopen
from bs4 import BeautifulSoup

web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

line_with_tags = ''

try:
    response = urlopen(web_address)
except FileNotFoundError:
    print("Address not found")

response_soup = BeautifulSoup(response)
response.close()

print(response_soup.get_text())

#for line in response:
#   line = line.decode('utf-8')
#    if 'Freezing Level' in line:
#        freezing_level_raw = next(response)
#        line_with_tags = freezing_level_raw


