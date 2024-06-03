def sumOfDigits(num):
    sum=0
    while(num>0):
        rem = num%10
        num = num//10
        sum = sum+rem
    return sum

num = int(input("Enter number: "))
sum = sumOfDigits(num)
print(f"Sum of digits of {num}: {sum}")