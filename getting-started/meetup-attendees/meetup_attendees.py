# This is a simple script parsing a meetup event web page
# and printing the names of all known attendees

import requests
from bs4 import BeautifulSoup


response = requests.get('http://www.meetup.com/PyLadiesStockholm/events/122636662/')
page = BeautifulSoup(response.text)

attendees_info = page.find(id = 'rsvp-list').find_all('h5', {'class':'padding-none member-name'})

for attendee in attendees_info:
    print attendee.find('a').text
