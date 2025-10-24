from bubble_sort import numbers


outer_pass = 0
inner_pass = 0

n = len(numbers)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    min_value = numbers.pop(min_index)
    numbers.insert(i, min_value)

print(numbers)