numbers = [2, 5, 10, 6, 19]
max = numbers[0]

for number in numbers:
    if max < number:
        max = number
print(max)
