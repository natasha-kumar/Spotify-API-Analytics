import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas as pd

client_id = 'enter your client id'
client_secret = 'enter your client secret id'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_uri = ['spotify:artist:4nDoRrQiYLoBzwC5BhVJzF','spotify:artist:0C8ZW7ezQVs4URX5aX7Kqx','spotify:artist:4gzpq5DPGxSnKTe4SA8HAU','spotify:artist:4nDoRrQiYLoBzwC5BhVJzF','spotify:artist:31TPClRtHm23RisEBtV3X7','spotify:artist:06HL4z0CvFAxyc27GXpf02', 'spotify:artist:66CXWjxzNUsdJxJ2JdwvnR','spotify:artist:6eUKZXaKkcviH0Ku9w2n3V','spotify:artist:1uNFoZAHBGtllmzznpCI3s','spotify:artist:6jJ0s89eD6GaHleKKya26X']

def get_album_uris(artist_uri):
    albums_uris = [] 
    #looping through different artists
    for artist in artist_uri:
        results = sp.artist_albums(artist, album_type='album')
        # print(results)
        albums = results['items']
        # print(albums)
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])

        #getting and appending all the album uris
        for album in albums:
            print(album['name'])
            print(album['uri'])
            new_album_uri = album['uri']
            albums_uris.append(new_album_uri)

        # print(albums_uris)
    return albums_uris


albums = get_album_uris(artist_uri)

#gets all tracks for different albums
def get_track_uris(albums_uri):
    ids = []
    for album in albums_uri:
        # print(album)
        tracks = sp.album_tracks(album)
        # print(tracks)
        for item in tracks['items']:
            # print(item)
            track_ids = item['uri']
            ids.append(track_ids)

    return ids

ids = get_track_uris(albums)

# print(ids)

#gets all track features
def get_track_features(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = get_track_features(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("Artists_Tracks_Detailed.csv", sep = ',')


