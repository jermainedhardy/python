def make_album(artist_name, album_title, tracks=0):
    album_info = {
        "artist": artist_name,
        "title": album_title,
    }

    if tracks > 0:
        album_info["tracks"] = tracks

    return album_info

album_one = make_album("JAY-Z", "blueprint 3", 11)
album_two = make_album("Gunna", "wunna")
album_three = make_album("kodak black", "back for everything")

print("Album 1: " + str(album_one))
print("Album 2: " + str(album_two))
print("Album 3: " + str(album_three))