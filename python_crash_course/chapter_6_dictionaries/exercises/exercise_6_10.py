favorite_number = {
    "jermaine": [0,1,3],
    "germany": [4,3,12,444],
    "willa": [1,2,3,4,5],
    "patrick": [3,55,33,44],
    "renee": [22,11,56,43],
    }

for name, numbers in favorite_number.items():
    print(name.title() + "'s favorite numbers are:")

    for number in numbers:
        print(number)
    
    print()