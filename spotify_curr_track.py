import spotipy
import spotipy.util as util
from requests import post, get, put
from dotenv import load_dotenv
import os
import json
import keyboard
import serial
import time

#spotify setup

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
username = 'k2m6n7by28pglepu6b5kj8bhs'

# Scopes for Spotify API access
scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'

# Get user authorization
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


#spotify functions to get auth. headers and to get current song name
def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

def currently_playing_song(token):
    
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers  = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)
#     print(json_result)
    try: 
        artist_names = [artist['name'] for artist in json_result['item']['artists']]
     
        artist_name = ''
        for i in range(len(artist_names)):
               artist_name = artist_name + artist_names[i]
               if i < len(artist_names)-1:
                      artist_name = artist_name + ','
               
               
        song_name = json_result['item']['name']
        # print( song_name, artist_name)
        return  song_name , artist_name

    except Exception as e :
        print("ad")
        return "AD or error !"
    


def next_song():
        print("Next action")
        
        keyboard.press_and_release('ctrl+f10')
        time.sleep(0.3)
    
        curr_song = currently_playing_song(token)
        return curr_song
def prev_song():
        print("Previous action")
        
        keyboard.press_and_release('ctrl+f8')
        time.sleep(0.3)
        curr_song = currently_playing_song(token)
        return curr_song
        
def play():
        print("Play action")
        
        
        keyboard.press_and_release('ctrl+w')


# while  True:
#         op = input("Enter : ")
#         if op == "prev":
#                 prev_song()
#         elif op == "next" :
#                 next_song()
#         elif op == "play" : 
#                 play()
              

