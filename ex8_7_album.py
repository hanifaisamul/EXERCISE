# 8-7. Album
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album
print(make_album("Coldplay", "Parachutes"))
print(make_album("Imagine Dragons", "Evolve", 11))
