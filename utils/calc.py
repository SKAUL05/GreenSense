#where over here you are gonna write code for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#this is operation such as add, sub, div , mul 
operation = input("Enter the operation (+, -, *, /): ")

#this is the if statement where it is results based user in in operation as shown
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Invalid operation Wrong number buddy try again :) ")

#this is the print command to print results of calc in final 
print("Result: ", result)

#this is the end of the code & enjoy just my first project !