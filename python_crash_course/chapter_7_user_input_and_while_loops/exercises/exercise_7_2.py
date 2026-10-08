question = input("How many people are in your dining group? ")

if int(question) > 8:
    print("You all will need to wait a few minutes for a table.")
elif int(question) <= 8:
    print("Your table is ready.")