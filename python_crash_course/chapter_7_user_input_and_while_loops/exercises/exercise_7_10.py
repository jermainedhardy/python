poll_active = True 
poll = {}

while poll_active:
    name = input("What is your name? ")
    place_to_visit = input("If you could visit one place in the world, where would you go? ")

    poll[name] = place_to_visit

    repeat = input("Would you like to ask another person? ")

    if repeat.lower() == "mo":
        poll_active = False

print("\n----- Poll Results -----")
for name, place_to_visit in poll.items():
    print(name + " would like to visit " + place_to_visit + ".")