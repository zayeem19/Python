numbers = [9, 9, 7, 8, 4, 1, 8]
count = []
for item in numbers:
    if item not in count:
        count.append(item)
print(count)
