current_users = ["jermaine", "richard", "mike", "admin", "drake"]
new_users = ["Jermaine", "thomas", "nancy", "dreko", "Richard"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("The username " + new_user + " is already in use. You will need to choose new username")
    else:
        print("The username " + new_user + " is available to use.")