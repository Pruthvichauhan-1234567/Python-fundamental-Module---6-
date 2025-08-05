# 29. Write a Python program to stop the loop once 'banana' is found using the break statement.

fruits=['apple','mango','cherry','banana','grap']

for fruit in fruits:
    print(f"Checking : {fruit}")
    if fruit == 'banana':
        print("Found 'banana'! Stopping the loop.")
        break