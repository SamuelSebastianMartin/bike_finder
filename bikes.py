#! /usr/bin/env python3

''' To display available 'velo-libre' cycles near home and work.
ie. St. John's Wood and Bloomsbury.
First it downloads the xml data from Transport for London.
Then parses it to recover only the Terminal Name & Number or Bikes.
If I feel good, it will be GUI.
'''


def main():
    whole_xml = get_xml()
    location = "St. John's Wood"
    data = parse_xml(whole_xml, location)
    print()
    print("Bikes available near St. John's Wood: ")
    print()
    for datum in data:
        print(datum[0], datum[1])

    location = "Bloomsbury"
    data = parse_xml(whole_xml, location)
    print()
    print("Bikes available near Bloomsbury: ")
    print()
    for datum in data:
        print(datum[0], datum[1])


def get_xml():
    import requests  # For dealing with url.
    url = 'https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml'
    page = requests.get(url)
    # Check that the data has arrived.
    try:
        page.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    whole_xml = page.text  # This is the relevant .xml data.
    return whole_xml


def parse_xml(whole_xml, location):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(whole_xml)

    data = []
    for station in root:
        if location in station[1].text:
            name = station[1].text
            bikes = station[10].text
            spaces = station[11].text
            datum = (name, bikes, spaces)
            data.append(datum)
    return data


if __name__ == '__main__':
    main()
