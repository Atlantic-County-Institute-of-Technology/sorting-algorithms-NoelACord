# Noel Cordero
# 9/30/2025

import random
#
numbers = [random.randint(1, 100) for i in range(10)]

print(numbers)
i_pass = 0
j_pass = 0

# j = len(numbers)
for i in range(len(numbers)):
    i_pass += 1
    for j in range(len(numbers) - i - 1):
        j_pass += 1
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
# for half the length of the list

