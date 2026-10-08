active = True

while active:
    topping = input("Enter the toppings you want on your pizza: ")

    if topping == "nothing":
        active = False
    else:
        print("You're adding " + topping + " to your pizza.")
