cars = ["audi", "bmw", "chevrolet", "ford", "subaru"]

print("Is car 1 == Audi? I predict False.")
print("Car 1 == Audi: " + str(cars[0] == "Audi"))
print()

print("Is car 1 == audi? I predict True.")
print("Car 1 == audi: " + str(cars[0] == "audi"))
print()

print("Is car == BMW? I predict False.")
print("Car 2 == BMW: " + str(cars[1].lower() == "BMW"))
print()

print("Is car 2 == bmw? I predict True.")
print("Car 2 == bmw: " + str(cars[1].lower() == "bmw"))
print()

print("Is 1 == 2? I predict False.")
print("1 == 2: " + str(1 == 2))
print()

print("Is 1 == 1? I predict True.")
print("1 == 1: " + str(1 == 1))
print()

print("Is 1 != 2? I predict True.")
print("1 != 2: " + str(1 != 2))
print()

print("Is 1 != 1? I predict False.")
print("1 != 1: " + str(1 != 1))
print()

print("Is 1 > 1? I predict False.")
print("1 > 1: " + str(1 > 1))
print()

print("Is 1 > 0? I predict True.")
print("1 > 0: " + str(1 > 1))
print()

print("Is 1 < 1? I predict False.")
print("1 < 1: " + str(1 < 1))
print()

print("Is 1 < 2? I predict True.")
print("1 < 2: " + str(1 < 2))
print()

print("Is 1 >= 1? I predict True.")
print("1 >= 1: " + str(1 >= 1))
print()

print("Is 1 >= 2? I predict False.")
print("1 >= 2: " + str(1 >= 2))
print()

print("Is 1 <= 1? I predict True.")
print("1 <= 1: " + str(1 <= 1))
print()

print("Is 1 <= 0? I predict False.")
print("1 <= 0: " + str(1 <= 0))
print("Test 'and' and 'or'")
print()

print("Is car 1 == audi and car 2 == bmw? I predict True.")
print("Car 1 == audi and car 2 == bmw: " + str(cars[0] == "audi" and cars[1] == "bmw"))
print()

print("Is car 1 == chevy and car 2 == bmw? I predict False.")
print("Car 1 == chevy and car 2 == bmw: " + str(cars[0] == "chevy" and cars[1] == "bmw"))
print()

print("Is car 1 == audi or car 2 == bmw? I predict True.")
print("Car 1 == audi or car 2 == bmw: " + str(cars[0] == "audi" or cars[1] == "bmw"))
print()

print("Is car 1 == chevy or car 2 == subaru? I predict False.")
print("Car 1 == chevy and car 2 == subaru: " + str(cars[0] == "chevy" and cars[1] == "subaru"))
print()

print("Is audi in the list? I predict True.")
print("audi is in the list: " + str("audi" in cars))
print()

print("Is maybach in the list? I predict False.")
print("maybach is in the list: " + str("maybach" in cars))
print()

print("Is audi not in the list? I predict False.")
print("audi is not in the list: " + str("audi" not in cars))
print()

print("Is maybach not in the list? I predict True.")
print("maybach is not in the list: " + str("maybach" not in cars))
print()