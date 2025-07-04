def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b
terms=int(input("Enter the number of terms of the Fibonacci series: "))
if terms<=0:
    print("Please enter a positive integer.")
else:print(fibonacci(terms))
