# Bike Finder
==============

This program will return a list of *Transport for London* bicycle
docking stations near *St John's Wood*, including the number of
bicycles available.

It also lists docking stations in *Bloomsbury*, and the number of spaces available to park the bike.

The same functionality is provided for the return journey by pressing the 'Bike Home' button.

### It does in a few milliseconds what the official API needs several minutes to complete.

## Use:

`python3 bike_finder.py`

### Alternatively
Use the Linux Desktop icon `BikeFinderNew.desktop`.
This will need to be executable: `chmod 744 BikeFInder.desktop`, and the path to the executable program and the icon image set according to your directory structure.
On the desktop, there is a symbolic link to the `BikeFinderNew.desktop`, so the file can remain in situ in the git directory.

On Ubuntu, I had no trouble with the icon displaying, but it has not been so simple on Manjaro. To make it work, I had to make the *Unix Shared Resources* directory `~/.icons`, then copy the icon there. Only then was it displayed on the Desktop. I reduced the size to 48 x 48, and saved as a `.xcf` file. I am not sure how crucial this was, as I did not test the icon as a larger `.jpeg`. See [this](https://forum.manjaro.org/t/add-icon-to-local-application-desktop-file/27137/7) thread for details.

## Adapting for other journeys
If you are not going from my house to my work, the app man not be ideal! However, the code can be easily changed for other journeys. *Transport for London* use intuitive area names in their [API](https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml) and so these can be changed in the code to areas that suit other needs.

No provision is made for these changes in the interface, though such changes are on the cards.

## In case of failure

To provide ease of grouping by region, the docking stations are scraped and identified by area name, not id. Any changes in the website will spoil this.

Check the [API](https://tfl.gov.uk/syndication/feeds/cycle-hire/livecyclehireupdates.xml) for names.
