programming_words = {
    "list": "a group of changeable values inside of square brackets",
    "tuple": "a group of unchangeable values inside of parenthesis",
    "dictionary": "a group of key-value values inside of curly brackets (braces)",
    "string": "more than one character together inside of quotation marks",
    "variable": "a placeholder for a value that can change",
    "key": "the item used to locate the value in a dictionary ",
    "value": "the item that contains the data that is connected to the key in a dictionary",
    "sorted": "a function used to put the items in a dictionary in alphabetical order",
    "keys()": "a method used to grab the keys in a dictionary",
    "items()": "a method used to grab all the key-value pairs in a dictionary",
}

for word, definition in programming_words.items():
    print(word.title() + ": " + definition.title() + ".")