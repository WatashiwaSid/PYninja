def checkPerfect(num):
    temp, sum = num, 0
    for i in range(1,num):
        if(num%i==0):
            sum = sum+i
    
    if(temp==sum):
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not perfect")

num = int(input("Enter a number: "))
checkPerfect(num)
