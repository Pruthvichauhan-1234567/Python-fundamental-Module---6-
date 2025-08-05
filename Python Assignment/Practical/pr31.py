# 31. Write a Python program that manipulates and prints strings using various string methods.

text = " Pruthvi Chauhan "

print("Original string:", repr(text))

string = text.strip()
print("After strip():", repr(string))

uppercase = string.upper()
print("After upper():", uppercase)

lowercase = string.lower()
print("After lower():", lowercase)

replaced = string.replace("Chauhan", "Darji")
print("After replace():", replaced)

words = string.split()
print("After split():", words)

position = string.find("Chauhan")
print("Position of 'Python':", position)

starts = string.startswith("Pruthvi")
print("Starts with 'hello':", starts)

ends = string.endswith("Chauhan")
print("Ends with 'world!':", ends)

count_o = string.count('u')
print("Count of 'o':", count_o)
