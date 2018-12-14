import os
import json
import spotipy
import spotipy.util as util

#Spotify username
username = ''

#Enter API credentials here
scope = 'user-read-recently-played user-top-read user-read-playback-state'
client_id = ''
client_secret = ''
redirect_uri = ''

try:
    token = util.prompt_for_user_token(
            username=username,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
            )
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(
            username=username,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
            )

spotifyObject = spotipy.Spotify(auth=token) # spotify object

user = spotifyObject.current_user()

displayName = user['display_name']
numFollowers = user['followers']['total']


print()
print('>>>> Welcome to Spotify Top Listens, ' + displayName + '!')
print('>>>> You have ' + str(numFollowers) + ' followers')
print()

ranges = ['short_term', 'medium_term', 'long_term']
limit = 10

def compile_list(**kwargs):
    if 'items' in kwargs:
        for index, currEntry in enumerate(kwargs['items']):
            print(str(index+1) + ": " + currEntry['name'])
        print()

for range in ranges:
    topArtists = spotifyObject.current_user_top_artists(limit,0,range)

    if range == 'short_term':
        print('Top ' + str(limit) + ' Artists (Short Term)')
    if range == 'medium_term':
        print('Top ' + str(limit) + ' Artists (Medium Term)')
    if range == 'long_term':
        print('Top ' + str(limit) + ' Artists (Long Terms)')
    compile_list(**topArtists)

for range in ranges:
    topTracks = spotifyObject.current_user_top_tracks(limit,0,range)

    if range == 'short_term':
        print('Top ' + str(limit) + ' Tracks (Short Term)')
    if range == 'medium_term':
        print('Top ' + str(limit) + ' Tracks (Medium Term)')
    if range == 'long_term':
        print('Top ' + str(limit) + ' Tracks (Long Terms)')
    compile_list(**topTracks)
