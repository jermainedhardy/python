favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

#print("Sarah's favorite language is " +
#    favorite_languages["sarah"].title() +
#    ".")

#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " + language.title() + ".")

#for name in favorite_languages.keys():
#    print(name.title())

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(name.title())

#    if name in friends:
#        print(" Hi " + name.title() +
#            ", I see your favorite language is " +
#            favorite_languages[name].title() + "!")

#if 'erin' not in favorite_languages.keys():
#    print("Erin, please take our poll!")

#print(favorite_languages.keys())

#for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

# The below prints the languages (value) from the favorite_languages dictionary
#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

# If we want to print all of the values in the dictionary, but avoid printing the
# the duplicates we use the set function.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())