# Import libraries.
import requests
# import urllib2
import re
from bs4 import BeautifulSoup

# Identify the URL and response headers.
headers = {'Date': 'Mon, 02 Apr 2018'}
url = requests.get('http://xpn.org/playlists/xpn-playlist', headers = headers)
html = (url.text)
soup = BeautifulSoup(html, 'html.parser')

# Identifies a href URLs.
for link in soup.find_all('a'):
    print(link.get('href'))
