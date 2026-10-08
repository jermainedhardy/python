sandwich_orders = ['Pepperoni', 'Meatball', 'Turkey', 'Ham']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print("I made your " + current_sandwich + " sandwich.")

    finished_sandwiches.append(current_sandwich) 

print("\nThese are all of the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")