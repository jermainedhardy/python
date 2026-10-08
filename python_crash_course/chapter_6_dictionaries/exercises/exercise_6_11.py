cities = {
    "memphis": {
        "country": "usa",
        "population": 610000,
        "fact": "majority black city",
    },

    "chicago": {
        "country": "usa",
        "population": 2720000,
        "fact": "cold city",
    },

    "bartlett": {
        "country": "usa",
        "population": 57000,
        "fact": "shelby county suburb"
    }
}

for city, attributes in cities.items():
    print("The city of " + city.title() + " is located in the country of " +
        attributes["country"].upper() + " with a population of " +
        str(attributes["population"]) + ". " +
        "A fun fact about this city is it is a " + attributes["fact"] + ".")