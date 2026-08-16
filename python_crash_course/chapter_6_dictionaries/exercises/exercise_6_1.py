from turtle import title


person = {
    "first_name": "willa",
    "last_name": "hardy", 
    "age": 31,
    "city": "memphis"
    }

print("I know this woman named " +
    person["first_name"].title() + " " +
    person["last_name"].title() + ". "  +
    "She is " + str(person["age"]) + " years old and she is from " +
    person["city"].title() + ".")