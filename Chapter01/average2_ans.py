#!/usr/bin/env python3

numbers = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("numbers:", numbers)
if numbers:
    # Insertion sort, see e.g. section 2.1 of "Introduction to Algorithms"
    # by Cormen/Leiserson/Rivest/Stein.
    j = 1
    while j < len(numbers):
        key = numbers[j]
        i = j - 1
        while i >= 0 and numbers[i] > key:
            numbers[i + 1] = numbers[i]
            i -= 1
        numbers[i + 1] = key
        j += 1

    index = int(len(numbers) / 2)
    median = numbers[index]
    if index * 2 == len(numbers):
        median = (median + numbers[index - 1]) / 2

    print("count =", len(numbers), "sum =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(numbers), "median =", median)
