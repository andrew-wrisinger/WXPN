import requests
from bs4 import BeautifulSoup

tracklist = []
daterange = ['12-04-2018','12-05-2018','12-06-2018']

# Returns songs for a given date.
def get_day(playlistdate):
    url = requests.post('http://xpn.org/playlists/xpn-playlist', data = {'playlistdate': playlistdate})
    soup = BeautifulSoup(url.text, 'html.parser')
    songtext = soup.find(id= 'accordion').find_all('a', href=True)
    for track in songtext:
            date = [playlistdate]
            track = str(track)
            track = track.split('>',1)[1]
            track = track.split('<')[0]
            track = track.split(' ',2)
            time = [' '.join(track[:2])]
            artist_and_song = track[-1].split(' - ')
            final = date + time + artist_and_song
            tracklist.append(final)

def get_week():
    for date in daterange:
        get_day(date)
    print(tracklist)
    
get_week()
