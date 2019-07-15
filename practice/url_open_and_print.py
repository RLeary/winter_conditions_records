# open a website and print the html file to terminal
# get relevant lines from mwis and print

from urllib.request import urlopen
import re

web_address = 'http://www.mwis.org.uk/scottish-forecast/WH/'

try:
    with urlopen(web_address) as response:
        for line in response:
            line = line.decode('utf-8')
            if 'Freezing Level' in line:
                freezing_level_raw = next(response)
                print(line)
                print(freezing_level_raw)
            if 'How Cold' in line:
                temp_at_900_raw = next(response)
                print(line)
                print(temp_at_900_raw)
except FileNotFoundError:
    print("Address not found")

#response = urlopen(web_address)
#...
#response.close()