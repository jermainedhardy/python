favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "jermaine": "python",
    "louis": "react native",
    "larry": "c",
    }
people_who_should_take_poll = ["jen", "sarah", "jermaine", "vaughn", "cody"]

for person in people_who_should_take_poll:
    if person in favorite_languages.keys():
        print("Hey " + person.title() + ", thanks for letting me know you've already taken the poll!")
    elif person not in favorite_languages.keys():
        print("Hey " + person.title() + ", please take some time to take the poll.")
    else:
        print("Unexpected behavior.")