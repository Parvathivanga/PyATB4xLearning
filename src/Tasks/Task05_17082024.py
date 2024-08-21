# Task #5
# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

num1=int(input("Enter the num1\n"))
num2=int(input("Enter the num2\n"))
if num1>num2:
          print(f"{num1} is greaterthan {num2}")
if num1<num2:
          print(f"{num1} is lessthan {num2}")
else:
          print(f"{num1} is equal to {num2}")