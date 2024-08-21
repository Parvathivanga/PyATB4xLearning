# Task #4

# Write a Python program to calculate the area of a circle
# given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

radius=float(input("Enter the radius of the circle"))
Area=3.14*(radius**2) #A= Area of the circle
print(f"The area of the cirle with radius {radius} is {Area:.2f}square units.")