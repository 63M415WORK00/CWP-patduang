print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

cal = num1 * num2

if cal < 0:
    result = "The result is negative."
elif cal > 0:
    result = "The result is positive."
else:
    result = "The result is positive and negative."
    
print(num1, " X " , num2, " = ", cal)
print(result)