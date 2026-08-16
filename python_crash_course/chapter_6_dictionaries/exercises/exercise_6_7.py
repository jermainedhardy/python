from turtle import title


person_one = {
    "first_name": "willa",
    "last_name": "hardy", 
    "age": 31,
    "city": "memphis"
    }

person_two = {
    "first_name": "jermaine",
    "last_name": "hardy",
    "age": 24,
    "city": "memphis",
}

person_three = {
    "first_name": "germany",
    "last_name": "hardy",
    "age": 13,
    "city": "memphis",
}

people = [person_one, person_two, person_three]

for person in people:
    print("I know this person named " +
        person["first_name"].title() + " " + person["last_name"] +
        " who is " + str(person["age"]) + " years old and lives in the city of " +
        person["city"].title() + ".")