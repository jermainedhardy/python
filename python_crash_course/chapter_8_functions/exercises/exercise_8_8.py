def make_album(artist_name, album_title, tracks=0):
    album_info = {
        "artist": artist_name,
        "title": album_title,
    }

    if tracks > 0:
        album_info["tracks"] = tracks

    return album_info

# Beginning of exercise 8-8
quit = False

while quit != True:
    user_artist = input("Enter the name of an artist you like: ")

    if user_artist == "quit":
        quit = True
        break

    user_album = input("Enter the name of the album by the artist you like: ")

    if user_album == "quit":
        quit = True
        break

    user_choice = make_album(user_artist, user_album)

    print("User's choice: " + str(user_choice))