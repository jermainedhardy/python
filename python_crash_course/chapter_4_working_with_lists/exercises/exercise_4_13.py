restaurant_menu = ('pizza', 'burgers', 'lamb', 'rice', 'spaghetti')

for food in restaurant_menu:
    print(food.title())

# Uncomment to see error. Python will reject this. Tuple items are immutable.
#restaurant_menu[0] = 'ham'

# Python does allow whole tuple changes though :)
restaurant_menu = ('pizza', 'burgers', 'lamb', 'ham', 'macaroni')

print()

for food in restaurant_menu:
    print(food.title())