#! /usr/bin/env python3

''' To display available 'velo-libre' cycles near home and work.
ie. St. John's Wood and Bloomsbury.
First it downloads the xml data from Transport for London.
Then parses it to recover only the Terminal Name & Number or Bikes.
If I feel good, it will be GUI.
'''

import requests  # For dealing with url.
import xml.etree.ElementTree as ET

###     Downloading     ###

url = 'https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml'
page = requests.get(url)
# Check that the data has arrived.
try:
    page.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

whole_xml = page.text  # This is the relevant .xml data.


###     Parsing     ###
root = ET.fromstring(whole_xml)
for station in root:
    if "St. John's Wood" in station[1].text:
        print()
        print(station[1].text)
        print(station[10].text)

    if "Bloomsbury" in station[1].text:
        print()
        print(station[1].text)
        print(station[10].text)

