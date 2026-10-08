def make_sandwich(*toppings):
    print("Sandwich being made:")
    for topping in toppings:
        print("- " + topping)

make_sandwich("Turkey", "Provolone Cheese", "Tomatoes", "White Bread")
print()
make_sandwich("Wheat Bread", "Pepper Jack Cheese", "Ham")
print()
make_sandwich("Ham")