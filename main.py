#Imports the spotifyClient.py and youtubeClient.py files
from spotifyClient import *
from youtubeClient import *

def main():
    spotify = Spotify()
    youtube = Youtube()

    spotify_login = spotify.get_spotify_client()
    youtube_login = youtube.get_youtube_client()

    #Calls the function which creates a list of all the songs in a playlist
    song_list = spotify.get_playlist_items(spotify_login)

    #Asks if user wants to create an entirely new playlist
    answer = input("Would you like to create a new playlist? (y/n) ")
    #Repeats until a valid answer is given
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
        answer = input("Would you like to create a new playlist? (y/n) ")
    
    if answer == "y" or answer == "Y":
        youtube.create_playlist(youtube_login)
        print("Playlist has been added to your YouTube account")

    playlist_id = youtube.get_yt_playlist_id(input("Enter link of YouTube playlist to add songs to: "))
    print(playlist_id)

    for song in song_list:
        video_id = youtube.get_youtube_song_id(youtube_login, song)
        youtube.add_song_to_playlist(youtube_login, video_id, playlist_id, song)

if __name__ == "__main__":
    main()
