
#Lyrics Finder AI

from musixmatch_api import *
import requests
import json
import urllib.parse
import lyricsgenius

#tts
# from gtts import gTTS
# import os

language = 'en'

#https://api.musixmatch.com/ws/1.1/track.search?format=jsonp&callback=callback&q_track=the%20man&q_artist=talyor%20swift&quorum_factor=1&apikey=2dc50fdf7aa422d60551c130d39eff35 

# example call: base_url + lyrics_matcher + format_url + artist_search_parameter + artist_variable + track_search_parameter + track_variable + api_key
# example json print: print(json.dumps(api_call, sort_keys=True, indent=2))

while True:
    print()
    print("Welcome to the Musixmatch API explorer!")
    print()
    print("MENU OPTIONS")

    print("0 - Exit")
    print("1 - Search for 30% lyrics of a song with authur and track name.")
    print("2 - Search for the lyrics of a song with track and authur name.")
    print("3 - Random song suggestion using authur name?")
    print()

    choice = input("> ")
    print()

    if choice == "0":
        break
    
    elif choice == "1":

        print("\nWhats's the name of the artist?")
        artist_name = input("> ")

        print("\nWhat's the name of the track?")
        track_name = input("> ")
        print()
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)

        data = request.json()

        data = data['message']['body']
        print()
        print(data['lyrics']['lyrics_body'])

    elif choice == "2":
        print("\nWhats's the name of the artist?")
        artist_name = input("> ")

        print("\nWhat's the name of the track?")
        track_name = input("> ")
        print()

        genius = lyricsgenius.Genius("6s_LlC9GaEn6_aJlkBI65s_mKIeScjiqd_H_FIo5PuPx6A1JlLxKK2QitmwrLznb")

        #artist = genius.search_artist("Clean Bandit", max_songs=0, sort="title")

        # print(artist.songs)

        song = genius.search_song(track_name, artist_name )

        print(song.lyrics)
        # Lyrics_body = song.lyrics

        # TTS = gTTS(text=Lyrics_body, lang=language, slow=False)

        # TTS.save("welcome.mp3")
        # os.system("mpg321 welcome.mp3")
        # os.remove('welcome.mp3')
        # #TTS.remove("welcome.mp3")


    elif choice == "3":
        print("\nWhats's the name of the artist?")
        artist_name = input("> ")

        print()

        print("\n Maximum number of songs?")
        max_no = input("> ")

        print()

        genius = lyricsgenius.Genius("6s_LlC9GaEn6_aJlkBI65s_mKIeScjiqd_H_FIo5PuPx6A1JlLxKK2QitmwrLznb")
        genius.verbose = False
        genius.remove_section_headers = True

        #artist = genius.search_artist("Clean Bandit", max_songs=0, sort="title")

        

        artist = genius.search_artist(artist_name, max_songs= int(max_no))
        artist_song = artist.songs

        for number in range(int(max_no)):  
            print(artist_song[number])
            print()

        # for index in range(len(artist_song)):
        #     print('Random:', artist_song[index] + '\n')

    else:
        break

    # check if the user wants to go again
    print()

    restarted = False


#rewind or break out method
    while True:
        print("Again? (y/n)")
        again = input("> ")
        print()
        if again == "n":
            restarted = true
        elif again == "y":
            break
        else:
            print("recheck the value")


    if restarted == "True":
        break

    restarted = True


    # have a high speed 