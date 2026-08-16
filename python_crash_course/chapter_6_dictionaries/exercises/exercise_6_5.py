major_rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'congo': 'africa',
    }

for river, country in major_rivers.items():
    print("The " + river.title() + " River runs through " + country.title())

for river in major_rivers.keys():
    print(river.title())

for country in major_rivers.values():
    if country == "usa":
        print(country.upper())
    else:
        print(country.title())