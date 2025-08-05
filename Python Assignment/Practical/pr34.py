# 34. Write a Python program that filters out even numbers using the filter() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Original list:", numbers)
print("List after filtering out even numbers:", odd_numbers)