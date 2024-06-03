def factorial(num):
    facto=1
    for i in range(1,num):
        facto = facto + (facto*i)
    
    return facto

num = int(input("Enter a number: "))
factorial = factorial(num)
print(f"Factorial {num} is {factorial}")