# 32. Write a Python program to apply the map() function to square a list of numbers.

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
