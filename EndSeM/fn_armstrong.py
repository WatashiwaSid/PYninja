def isArmstrong(num):
    temp=num
    sum=0
    while(num>0):
        rem = num%10
        num = num//10
        sum = sum + (rem ** 3)
    if(temp==sum):
        print("Sum of cube of digits: ", sum)
        print("Number is armstrong.")
    else:
        print("Sum of cube of digits: ", sum)
        print("Number is not armstrong.")

num = int(input("Enter number: "))
isArmstrong(num)