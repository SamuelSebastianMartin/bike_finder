#! /usr/bin/env python3

from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bike Finder")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Find Bikes", command=self.greet)
        self.greet_button.pack()

        self.find_button = Button(master, text="Bike Home", command=self.find)
        self.find_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


    def greet(self):

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


    def find(self):

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

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
