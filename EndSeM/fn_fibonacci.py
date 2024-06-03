def fibonacci(terms):
    a,b=0,1
    for i in range(1,terms+1):
        print(a, end=" ")
        a,b = b,a+b

terms = int(input("Enter number of terms in fibonacci series: "))
fibonacci(terms)