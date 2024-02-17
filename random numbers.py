import random

# Generate unique numbers
unique_numbers = set()
while len(unique_numbers) < 5000:
    unique_numbers.add(random.randint(0, 20000))

# Convert set to list
a = list(unique_numbers)

# Selection sort197
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("After sorting:", a)

n = int(input('Enter a random number: '))

start = 0
end = len(a) - 1  # corrected the typo here

found = -1
while start <= end:
    mid = (start + end) // 2
    if a[mid] == n:
        found = mid
        break
    if a[mid] > n:
        end = mid - 1
    else:
        start = mid + 1

if found == -1:
    print('Number not found.')
else:
    if found == 0:
        print(f'The number lies between {a[found]} and {a[found + 1]}')
    elif found == len(a) - 1:
        print(f'The number lies between {a[found - 1]} and {a[found]}')
    else:
        print(f'The number lies between {a[found - 1]} and {a[found + 1]}')