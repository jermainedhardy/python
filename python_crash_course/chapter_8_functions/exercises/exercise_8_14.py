def make_car(manufacturer, model, **other_details):
    """Store information about a car."""
    car = {
        "manufacturer": manufacturer,
        "model": model,
    }

    for key, value in other_details.items():
        car[key] = value
    
    return car

car_one = make_car("Chevrolet", "Malibu", color="blue", motor="v4")
print(car_one)