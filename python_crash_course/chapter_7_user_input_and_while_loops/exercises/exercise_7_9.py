sandwich_orders = ['Pastrami', 'Pepperoni', 'Meatball', 'Pastrami', 'Turkey', 'Ham', 'Pastrami']
finished_sandwiches = []

print("The deli has run out of Pastrami.")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\nHere are the finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)