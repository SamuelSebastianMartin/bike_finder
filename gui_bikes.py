#! /usr/bin/env python3

from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bike Finder")

        self.label = Label(master, text="Bike Finder App")
        self.label.pack()

        self.bike_out_button = Button(master, text="Bike to SOAS", command=self.bike_out)
        self.bike_out_button.pack()

        self.bike_home_button = Button(master, text="Bike Home", command=self.bike_home)
        self.bike_home_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.whole_xml = self.get_xml()

    def get_xml(self):
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

    def bike_out(self):

        location = "St. John's Wood"
        data = self.parse_xml(self.whole_xml, location)
        print()
        print("Bikes available near St. John's Wood: ")
        print()
        for datum in data:
            print(datum[1], datum[0][:datum[0].index(',')])

        location = "Bloomsbury"
        data = self.parse_xml(self.whole_xml, location)
        print()
        print("Spaces near Bloomsbury")
        print()
        for datum in data:
            print(datum[2], datum[0][:datum[0].index(',')])


    def bike_home(self):

        location = "Bloomsbury"
        data = self.parse_xml(self.whole_xml, location)
        print()
        print("Bikes available near SOAS: ")
        print()
        for datum in data:
            print(datum[1], datum[0][:datum[0].index(',')])

        location = "St. John's Wood"
        data = self.parse_xml(self.whole_xml, location)
        print()
        print("Bikes available near home: ")
        print()
        for datum in data:
            print(datum[2], datum[0][:datum[0].index(',')])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
