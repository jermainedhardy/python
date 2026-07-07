squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Written more concise
squares_v2 = []
for value_v2 in range(1,11):
    squares_v2.append(value_v2**2)

print(squares_v2)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)