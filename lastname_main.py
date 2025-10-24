# Noel Cordero
# 10/24/2025

import random
import sys
import time


def print_hi(name):

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



print("Bubble sort - 1, Insertion sort - 2, Selection sort - 3")

swapcount = 0

SortInput = int(input("Select the sort type you wish to use: "))
if SortInput > 3 or SortInput < 1:
    print("--! Error, enter a number from 1-3 !--")
    sys.exit(1)
elif SortInput == str:
    print("--! Error, enter a number from 1-3 !--")
    sys.exit(1)


RangeNumbersMin = int(input("Select the minimum range of your list, type a number : "))

RangeNumbersMax = int(input("Select the maximum range of your list, type a number : "))

if RangeNumbersMax < RangeNumbersMin:
    print("--! Error, your maximum number must be greater than your minimum !--")
    sys.exit(2)

RangeInput = int(input("How long do you want your list to be, type a positive number that is greater than or equal to 5 : "))

if RangeInput < 5:
    print("--! Error, type a positive number greater than or equal to 5 !--")
    sys.exit(3)

numbersnew = [random.randint(RangeNumbersMin, RangeNumbersMax) for i in range(RangeInput)]

if SortInput == 1:
    start = time.perf_counter()
    for i in range(len(numbersnew)):
        for j in range(len(numbersnew) - i - 1):
            if numbersnew[j] > numbersnew[j + 1]:
                numbersnew[j], numbersnew[j + 1] = numbersnew[j + 1], numbersnew[j]
                swapcount += 1
    print(numbersnew)
    end = time.perf_counter()
    duration = end-start
    print("this sort took", round(duration, 5), "seconds")
    print(swapcount, "total actions occurred in this sort")


if SortInput == 2:
    start = time.perf_counter()
    n = len(numbersnew)
    for i in range(1, n):
        insert_index = i
        current_value = numbersnew.pop(i)
        for j in range(i - 1, -1, -1):
            if numbersnew[j] > current_value:
                insert_index = j
                swapcount += 1
        numbersnew.insert(insert_index, current_value)
    end = time.perf_counter()
    duration = end - start
    print(numbersnew)
    print("this sort took", round(duration, 5), "seconds")
    print(swapcount, "total actions occurred in this sort")

if SortInput == 3:
    start = time.perf_counter()
    n = len(numbersnew)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numbersnew[j] < numbersnew[min_index]:
                min_index = j
                swapcount += 1
        min_value = numbersnew.pop(min_index)
        numbersnew.insert(i, min_value)
    end = time.perf_counter()
    duration = end - start
    print(numbersnew)
    print("this sort took", round(duration, 5), "seconds")
    print(swapcount, "total actions occurred in this sort")



