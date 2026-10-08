favorite_places = {
    "jermaine": ["home", "parents house", "movies"],
    "willa": ["home"],
    "germany": ["home", "starbucks"],
}

# Loop through and print the person and the places.
for person, places in favorite_places.items():
    if len(places) == 1:
        print(person.title() + "'s favorite place is " + places[0] + ".")
    elif len(places) > 1:
        print(person.title() + "'s favorite places are:")
        for place in places:
            print(place.title())
