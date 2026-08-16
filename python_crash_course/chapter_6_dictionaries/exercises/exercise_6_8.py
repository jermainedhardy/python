chi_chi = {
    "kind": "dog",
    "owners_name": "germany",
}

major = {
    "kind": "dog",
    "owners_name": "jermaine",
}

champ = {
    "kind": "dog",
    "owners_name": "jermaine",
}

pets = [chi_chi, major, champ]

for pet in pets:
    print("This pet is a " + pet["kind"] + " owned by " + pet["owners_name"].title())