favorite_pizzas = ['pepperoni', 'sausage', 'beef']
friends_pizzas = favorite_pizzas[:]

favorite_pizzas.append('cheese')
friends_pizzas.append('vegetable')

for favorite_pizza in favorite_pizzas:
    print("I like " + favorite_pizza + " pizza.")

print("\nI really like pizza. It's one of my favorite foods to eat! I'm sure I can eat it everyday.\n")
print("My friends's favorite pizzas are:")

for friend_pizza in friends_pizzas:
    print(friend_pizza.title())