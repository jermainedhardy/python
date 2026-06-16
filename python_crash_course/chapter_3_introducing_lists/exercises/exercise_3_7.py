guest_list = ['Mansa Musa', 'Imhotep', 'Leonardo da Vinci', 'Nikola Tesla', 'Steve Jobs']

print("Hey " + guest_list[0] + ", I would like to invite you to dinner for a talk.")
print("Hey " + guest_list[1] + ", how did you come up with those pyramids? Let's discuss over dinner.")
print(guest_list[2] + "! My boy! How did you come up with all of your invnetions and ideas?! Let's talk over steaks.")
print(guest_list[3] + "! Do feel like you were the best in your time? Let's discuss over dinner at a nice steak house.")
print(guest_list[4] + " how do you feel about the new iPhones? Let's talk about it over dinner.")
print(guest_list[0] + " can't make the dinner.")

guest_list.remove("Mansa Musa")
guest_list.insert(0, "Malcolm X")

print("New list:")
print(guest_list)

print("Thanks for deciding to join me " + guest_list[0])
print("It's a honor to have you " + guest_list[1])
print("Glad you could make it " + guest_list[2])
print("Thanks for accepting the invite " + guest_list[3])
print("Thanks for coming out " + guest_list[4])
print("I found a a bigger dinner table, so I'm going to invite three more people!")

guest_list.insert(0, "Fred Hampton")
guest_list.insert(3, "Huey P. Newton")
guest_list.append("Jay-Z")

print("Come out for dinner with me " + guest_list[0])
print("Grab a bite to eat with me " + guest_list[1])
print("Get dinner with me " + guest_list[2])
print("Dinner would be cool if you have time " + guest_list[3])
print("Are you available to grab some dinner " + guest_list[4])
print("Dinner on me " + guest_list[5])
print("Dinner at 8 PM " + guest_list[6])
print("Let's get dinner at the steakhouse " + guest_list[7])

# Start of exercise 3-7
print("Sorry y'all, but I can only have two guests.")

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

latest_guest_removed = guest_list.pop()

print("Sorry I couldn't invite you to dinner " + latest_guest_removed)

print(guest_list)

print(guest_list[0] + " you're still invited to the dinner.")
print(guest_list[1] + " you're still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)