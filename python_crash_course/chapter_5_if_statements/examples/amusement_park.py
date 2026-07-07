age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# More efficient way to code the above
if age < 4:
    cost = 0
elif age < 18:
    cost = 5
else:
    cost = 10

print("Your admission cost is $" + str(cost) + ".")