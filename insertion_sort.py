
from bubble_sort import numbers


outer_pass = 0
inner_pass = 0

# sorted_list = bubble_sort(numbers)
# print(f"Sorted Values = {sorted_list}")

n = len(numbers)
for i in range(1,n):
  insert_index = i
  current_value = numbers.pop(i)
  for j in range(i-1, -1, -1):
    if numbers[j] > current_value:
      insert_index = j
  numbers.insert(insert_index, current_value)

print(numbers)