def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    "Jermaine",
    "Hardy",
    nationality="american",
    ethnicity="black",
    hair="black",
)

print(my_profile)