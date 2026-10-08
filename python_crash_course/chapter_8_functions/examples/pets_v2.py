# This version uses keyword arguments, instead of positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type="hamster", pet_name="harry")

# The following also works. Order doesn't matter, because Python knows where each
# value should go.
describe_pet(pet_name="harry", animal_type="hamster")