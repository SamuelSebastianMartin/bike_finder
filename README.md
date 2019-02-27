## Bike Finder
This program will return a list of *Transport for London* bicycle
docking stations near *St John's Wood*, including the number of
bicycles available.

It also lists docking stations in *Bloomsbury*, and the number of spaces available to park the bike.

The same functionality is provided for the return journey by pressing the 'Bike Home' button.

####It does in a few miliseconds what the official API needs several minutes to complete.

###Use:

`python3 bike_finder.py`

Alternatively, use the Linux Desktop icon `BikeFInder.desktop`. 
This will need to be executable: `chmod 744 BikeFInder.desktop`, and the link to the executable program and the image added to the code (currently there are placeholders only).

###Adapting for other journies
The code can easily be changed for other journeys. *Transport for London* use area names in their [API](https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml) and so these can be changed in the code to areas that suit other needs.

No provision is made for these changes in the interface, though such changes are on the cards.

###In case of failure

To provide ease of grouping by region, the docking stations are scraped and identified by area name, not id. Any changes in the website will spoil this.

Check the [API](https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml) for names.
