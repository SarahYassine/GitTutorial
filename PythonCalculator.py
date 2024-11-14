# Python program for simple calculator

##Function to add two numbers
def add(a,b):
    return a+b

##Function to substract two numbers
def substract(a,b):
    return a-b

##Function to Multiply two numbers
def multiply (a,b):
    return a*b


print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" )

##Take input from the user
select =int(input("Select operations from 1,2,3 :"))
a = int(input("Enter first number: "))
b = int(input("Enter second number :"))
        
if select == 1:
    print(a, "+", b, "=",
                    add(a, b))

elif select == 2:
    print(a, "-", b, "=",
                    substract(a, b))

elif select == 3:
    print(a, "*", b, "=",
                    multiply(a, b))

else:
    print("Invalid input")
        