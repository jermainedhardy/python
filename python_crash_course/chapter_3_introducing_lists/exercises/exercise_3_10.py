random_list = ['dog', 'cat', 'lion', 'sheep']

print(random_list[0].title())

random_list.append('giraffe')
print(random_list)

random_list.insert(0, 'lizard')
print(random_list)

del random_list[0]
print(random_list)

removed_animal = random_list.pop()
print(removed_animal)

old_animal = random_list.pop(0)
print(old_animal)
print(random_list)

random_list.remove('cat')
print(random_list)

random_list.append('rooster')
random_list.append('poodle')
print(random_list)

random_list.sort()
print(random_list)

random_list.sort(reverse=True)
print(random_list)

print(sorted(random_list))
print(random_list)

random_list.reverse()
print(random_list)
print(len(random_list))