from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# Load environment variables from .env file
load_dotenv()

# Fetch the client_id and client_secret from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Check if the environment variables are loaded successfully
if client_id is None or client_secret is None:
    raise ValueError("Please set CLIENT_ID and CLIENT_SECRET in your .env file.")

# Define a function to obtain the access token
def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Define a function to create the authorization header with the access token
def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

# Define a function to search for an artist by name
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result[0]

# Define a function to get the top tracks of an artist
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

# Obtain the access token
token = get_token()

# Prompt the user to input the artist's name
artist_name = input("Enter the name of the artist: ")

# Search for the artist
result = search_for_artist(token, artist_name)
if result:
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)

    # Display the top tracks of the artist
    for idx, song in enumerate(songs):
        print(f"{idx+1}. {song['name']}")
