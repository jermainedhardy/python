players = ['charles', 'martina', 'michael', 'florence', 'eli']

# First to third item
print(players[0:3])

# First to 4th item
print(players[:4])

# Third item on
print(players[2:])

# Third to last onwards
print(players[-3:])

print('--------------------------------')
print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())