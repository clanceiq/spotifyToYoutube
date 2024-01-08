# Spotify to YouTube Playlist Converter
A Python script which allows users to enter a link to a Spotify playlist and transfer the songs onto a new or existing YouTube playlist.  
This project makes use of the Spotify API via the Spotipy library. This allows the program to access the contents of the **public** Spotify playlist.  
The project also uses the YouTube Data v3 API and Google OAuth 2.0 Authentication. This gives the project access to your YouTube account to both create a new playlist and add content to that playlist.

## Extra Information
- Meant for Python 3.10
- A requirements.txt file is provided. Type in the command line "pip install requirements.txt" for Windows. Or the equivalent command for other Operating Systems.
- The user will have to follow a couple of steps to create the ".env" and "youtube_secrets.json" files required for this script.
- Only **public** Spotify playlists can be transferred into a YouTube playlist.
- ~100 songs can be transferred per day due to the limit of the YouTube Data v3 API.
- Run the project by navigating to the spotifyToYoutube directory and typing "python main.py" in the terminal for Windows. Or the equivalent command for other Operating Systems.

### Making the ".env" file
1. In the same directory, create a file and name it ".env"
2. Create the variables in the image below:
![image](https://github.com/clanceiq/spotifyToYoutube/assets/142943141/4d4fdfee-2961-4ef5-a1f7-9c909c731e38)
#### Spotify API
1. Browse to https://developer.spotify.com/dashboard/applications and log into your Spotify account.
2. Click on "Create App". (For App name and App description it is recommended to give it a useful name, ie. one where you know what the app does)
3. Copy the client ID and client secret into their respective variables.
#### YouTube Data v3 API
1. Navigate to https://console.developers.google.com/project and log into a Google Account.
2. Create a new project. (For the project name it is recommended to give it a useful name)
3. Navigate to the Credentials tab. Click on Create Credentials and select API key.
4. Copy and paste the API key into the .env file.

### Creating the "youtube_secrets.json" file
1. Navigate to the Credentials tab. Click on Create Credentials and select OAuth client ID.
2. Set the application type as web application
3. Add an authorized redirect URI. Copy and paste "http://localhost:8080/"
4. Click Create
5. Download the JSON file and add it to your working directory
6. Rename the JSON file "youtube_secrets.json"

## Future Plans
- Turn project into a full-stack web application by creating a front-end in HTML, CSS, JavaScript, or with Reactjs
