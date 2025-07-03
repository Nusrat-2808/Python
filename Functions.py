# #Case 1
# def intro(name,age):
#     print("Hello! My name is ",name,".\nI am ",age," years old.")
# user_name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# intro(user_name,age)
# #Case 2
# def recur_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*recur_factorial(n-1)
# num=int(input("Enter the number: "))
# #Check if the number is negative
# if num<0:
#     print("Sorry no factorial exists for negative number.")
# elif num==0:
#     print("The factorial of 0 is 1.")
# else:
#     print("The factorial of ",num," is ", recur_factorial(num))
#Case 3
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2"))
print("Sum:",add(num1,num2))
print("Difference:",substract(num1,num2))
print("Product:",multiply(num1,num2))
print("Quotient:",divide(num1,num2))