numbers = [1,2,3,6,4,5,7,7,6,5,4,3,2,1]
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
