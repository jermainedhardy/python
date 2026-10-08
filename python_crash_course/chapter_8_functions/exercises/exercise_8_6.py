def city_country(city, country):
    """Returns the name of a city and its country."""
    city_and_country = city + ", " + country
    return city_and_country.title()

city_country_one = city_country("memphis", "america")
city_country_two = city_country("montego bay", "jamaica")
city_country_three = city_country("kingston", "jamaica")

print(city_country_one)
print(city_country_two)
print(city_country_three)