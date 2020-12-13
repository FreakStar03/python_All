import lyricsgenius

genius = lyricsgenius.Genius("6s_LlC9GaEn6_aJlkBI65s_mKIeScjiqd_H_FIo5PuPx6A1JlLxKK2QitmwrLznb")

#artist = genius.search_artist("Clean Bandit", max_songs=0, sort="title")

# print(artist.songs)

song = genius.search_song("Symphony", "Clean Bandit")
print(song.lyrics)