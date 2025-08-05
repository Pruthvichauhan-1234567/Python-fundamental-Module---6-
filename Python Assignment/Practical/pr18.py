# 18. Write a Python program that uses a custom iterator to iterate over a list of integers.

class IntegerListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0  # Start from the first element

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # Signals the end of iteration


# List of integers
numbers = [10, 20, 30, 40, 50]

# Create an iterator object
iterator = IntegerListIterator(numbers)

# Use the iterator in a for-loop
for num in iterator:
    print(num)
