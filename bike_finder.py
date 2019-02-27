#! /usr/bin/env python3

"""Provide information about the number of TFL bikes available in the areas
relvant to my work commute: Bloomsbury, and St. John's Wood.
The gui provides a button to give the nearby stations and lists their
respective number of bikes plus the number of spaces at stations near SOAS.
There is also a button to show the same data for the reverse journey.
"""
from tkinter import Tk, Label, Button


class BikeFinderGui:
    def __init__(self, master):
        self.master = master
        master.title("Bike Finder")

        self.label = Label(master, text="Bike Finder App")
        self.label.pack()

        self.bike_out_button = Button(master, text="Bike to SOAS",
                                      command=self.bike_out)
        self.bike_out_button.pack()

        self.bike_home_button = Button(master, text="Bike Home",
                                       command=self.bike_home)
        self.bike_home_button.pack()

        self.close_button = Button(master, text="Close",
                                   command=master.quit)
        self.close_button.pack()

        self.whole_xml = self.get_xml()

    def get_xml(self):
        """Downloads live data from all London bicyle docking stations.
        Returns TFL's .xml data as a text object."""
        import requests  # For dealing with url
        url = 'https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml'
        page = requests.get(url)
        # Check that the data has arrived.
        try:
            page.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))

        whole_xml = page.text  # This is the relevant .xml data.
        return whole_xml

    def parse_xml(self, whole_xml, location):
        """Parses the TFL xml information. It returns a list of 3-place tuples
        containing only the <name>, <nbBikes> & <nbEmtyDocs> tags.
        The tags are found by index, not name, so a change in the website
        will ruin the program."""
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

    def present_results(self, whole_xml, location, number):
        """Prints relvant data to terminal. The complex second argument to
        the print() call is to only print the Station name up to the
        first comma, eliminating the area name: eg. 'Bloomsbury'. """
        data = self.parse_xml(self.whole_xml, location)
        if number == 1:
            category = 'Bikes'
        else:
            category = 'Spaces'
        print()
        print("{} available near {}: ".format(category, location))
        print()
        for datum in data:
            print(datum[number], datum[0][:datum[0].index(',')])

    def bike_out(self):
        """To print the bikes near home and the spaces near soas."""
        location = "St. John's Wood"
        number = 1
        self.present_results(self.whole_xml, location, number)

        location = "Bloomsbury"
        number = 2
        self.present_results(self.whole_xml, location, number)

    def bike_home(self):
        """To print the bikes near soas and the spaces near home."""
        location = "Bloomsbury"
        number = 1
        self.present_results(self.whole_xml, location, number)

        location = "St. John's Wood"
        number = 2
        self.present_results(self.whole_xml, location, number)


root = Tk()
gui_window = BikeFinderGui(root)
root.mainloop()
