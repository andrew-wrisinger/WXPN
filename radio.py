# Import libraries.
import requests
import urllib2
import re
from bs4 import BeautifulSoup

# Returns songs for a given date.
def get_text(date):
    url = requests.get('http://xpn.org/playlists/xpn-playlist', headers = {'Date': date})
    soup = BeautifulSoup(url.text, 'html.parser')
    songtext = soup.find(id= 'accordion').prettify()
    print songtext

# Testing
get_text('Mon, 02 Apr 2018')
