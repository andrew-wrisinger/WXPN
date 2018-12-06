import requests
from bs4 import BeautifulSoup

# Returns songs for a given date.
def get_text(playlistdate):
    url = requests.post('http://xpn.org/playlists/xpn-playlist', data = {'playlistdate': playlistdate})
    soup = BeautifulSoup(url.text, 'html.parser')
    songtext = str(soup.find(id= 'accordion').find_all('a', href=True))
    songtext.split(">,")
    print(songtext)

get_text('12-03-2018')

if __name__ == '__main__'():
    print'z'
