import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

class Spotify():
    def __init__(self):
        self.spotify_client_id = str(os.getenv("SPOTIPY_CLIENT_ID"))
        self.spotify_client_secret = str(os.getenv("SPOTIPY_CLIENT_SECRET"))

    def get_spotify_client(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.spotify_client_id, client_secret=self.spotify_client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        return sp
    
    def get_playlist_items(self, sp):
        spotify_playlist_id = self.get_sp_playlist_id(input("Enter link of Spotify playlist being transferred: "))
        playlist = sp.playlist_tracks(spotify_playlist_id)
        tracks = playlist["items"]

        # If playlist is > 100 songs, loop will extend the tracks variable
        while playlist['next']:
            playlist = sp.next(playlist)
            tracks.extend(playlist['items'])

        song_info = []
        for song in tracks:
            title = song["track"]["name"]
            artist = song["track"]["album"]["artists"][0]["name"]
            song_info.append(title + " " + artist)
        
        return song_info
    
    def get_sp_playlist_id(self, id):
        playlist_id = ""
        x = id.find("/playlist/")
        y = id.find("?")

        for i in range(x+10, y):
            playlist_id += id[i]
        
        return playlist_id
