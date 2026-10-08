# The below line imports the entire module.
#import pizza_v2

# The below line only imports certain functions from module.
#from pizza_v2 import make_pizza

# The below line only imports certain functions and gives them an alias,
# just in case there is another function with the same name or the name is too long.
# from pizza_v2 import make_pizza as mp

# The below line allows use to import a module with an Alias.
import pizza_v2 as pv2

#pizza_v2.make_pizza(16, "pepperoni")
#pizza_v2.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# Becasue we are explicitly importing the make_pizza function, we don't need to use
# the dot notation when we call a function.
#make_pizza(16, "pepperoni")
#make_pizza(12, "mushrooms", "green peppers", "extra cheese")

# Because we are explicityly importin the make_pizza function, we don't need to use
# the dot notation when we call a function. We also will call the function by the alias
# we gave it in the import statement, since we used as in the import statement.
#mp(16, "pepperoni")
#mp(12, "mushrooms", "green peppers", "extra cheese")

# The below allows us to use the imported module, pizza_v2 by it's alias to call
# and use any of it's functions.
pv2.make_pizza(12, "Pepperoni, Ham, Bacon")
                                                                