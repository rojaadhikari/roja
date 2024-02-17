import random
import time

# Generate unique numbers
start = time.time_ns()
unique_numbers = set()
while len(unique_numbers) < 5000:
    unique_numbers.add(random.randint(0, 20000))
duration_ns = time.time_ns() - start
duration_ms = duration_ns /1_000_000
print(duration_ms,"ms")

# Convert set to list
#
a = list(unique_numbers)

# Selection sort
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print("After sorting:", a)
