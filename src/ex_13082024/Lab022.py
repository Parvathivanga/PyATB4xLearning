# Take a user inputs a,b and calculate the sum, mul, sub ,div
#cal

#num1=input("Enter te num 1")
#num2=input("Enter te num 2")
#89+89=178 ideally
#print("sum is", num1+num2) - 8989 because input is the string
#print("sub is", num1-num2) -invalid as string cannot perform this action
#print("mul is", num1*num2)-invalid as string cannot perform this action
#print("Div is", num1/num2)-invalid as string cannot perform this action

# inorder to perform th above actions first convert the string into integer

num1=int(input("Enter the num 1"))
num2=int(input("Enter the num 2"))

print("sum is", num1+num2)
print("sub is", num1-num2)
print("mul is", num1*num2)
print("Div is", num1/num2)

print(type(num1))
print(type(num2))