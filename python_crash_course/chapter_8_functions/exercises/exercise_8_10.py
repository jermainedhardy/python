def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)

def make_great(magician_names):
    index = 0

    while index < len(magician_names):
        magician_names[index] = magician_names[index] + " the Great"

        index = index + 1

magician_names = ["Jermaine", "Ken", "John", "Kennedy"]
make_great(magician_names)
show_magicians(magician_names)
