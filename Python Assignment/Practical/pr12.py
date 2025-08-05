# 12. Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("Enter Your Age : "))
if age >= 18:
   weight = int(input("Enter Your Weight : "))
   if weight >= 50:
      print("You Are Eligible to Donate Blood")
   else:
      print("You Are Not Eligible To Donate Blood Because Your Weight Is Below 50 Kg.")
else:
   print("You Are Not Eligible To Donate Blood Because You Are Under 18.")

      


 