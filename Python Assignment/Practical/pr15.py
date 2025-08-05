# 15. Write a Python program to find a specific string in the list using a simple for loop and if condition.

fruits=['apple','banana','mango','orange']

search_item=input("Enter The Fruit To Search : ")
for  fruit in fruits:
    if fruit == search_item:
        print(f"{search_item} Found In The List")
        break
else:
    print(f"{search_item} Not Found In The List")