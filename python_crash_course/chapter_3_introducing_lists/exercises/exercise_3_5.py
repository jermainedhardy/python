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