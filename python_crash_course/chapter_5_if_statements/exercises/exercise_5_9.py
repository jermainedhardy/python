#user_names = ["admin", "jerm", "dk", "marchin", "elbo"]

# Testing the blank list. else statement should print.
user_names = []

if user_names:
    for user_name in user_names:
        if user_name == "admin":
            print("Hello " + user_name + ", would you like to view the status report?")
        else:
            print("Hey " + user_name + ", welcome to Hardy Technology.")
else:
    print("We need to find some users!")