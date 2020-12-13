from lyrics_web import lyrics

ourSong = lyrics("symphony")

print(ourSong["content"][0]["title"])