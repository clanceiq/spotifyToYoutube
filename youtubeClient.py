import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from pyyoutube import Client
import time
from dotenv import load_dotenv

load_dotenv()

class Youtube():
    def __init__(self):
        pass

    def get_youtube_client(self):
        credentials = None

        #token.pickle stores the user's credentials from previously successful logins
        if os.path.exists("token.pickle"):
            print("Loading Credentials From File...")
            with open("token.pickle", "rb") as token:
                credentials = pickle.load(token)

        #If there are no valid credentials available, a refresh token is accessed, or the user goes through OAuth again     
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                print("Refreshing Access Token...")
                credentials.refresh(Request())
            else:
                print("Fetching New Tokens...")
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                    "youtube_secret.json", scopes=["https://www.googleapis.com/auth/youtube.force-ssl"]
                )
                flow.run_local_server(
                    port=8080, prompt="consent", authorization_prompt_message=""
                )
                credentials = flow.credentials

                #Credentials are saved for any future uses
                with open("token.pickle", "wb") as f:
                    print("Saving Credentials for Future Use...")
                    pickle.dump(credentials, f)

        api_service_name = "youtube"
        api_version = "v3"
        youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
        
        return youtube

    def create_playlist(self, youtube):
        playlistName = input("Enter the name of the playlist: ")
        playlistDescription = input("Give the playlist a description: ")
        request = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": str(playlistName),
                    "description": str(playlistDescription)
                },
                "status": {
                    "privacyStatus": "private"
                }
            }
        )
        response = request.execute()

    def get_youtube_song_id(self, youtube, song_name):
        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            q=song_name
        )
        response = request.execute()

        #Filters through the given data and returns the necessary information
        response = response.get("items")
        response = response[0]
        response = response.get("id")
        song_id = response.get("videoId")
        
        return song_id

    def add_song_to_playlist(self, youtube, video_id, playlist_id, song_name):
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )

        try:
            response = request.execute()
        except googleapiclient.errors.HttpError as e:
            print(e)
            print(f'Failed to add "{song_name}" to playlist. It has been skipped.')

    def get_yt_playlist_id(self, id):
        playlist_id = ""
        x = id.find("=")
        
        for i in range(x+1, len(id)):
            playlist_id += id[i]

        return playlist_id

