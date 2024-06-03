def checkPrime(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
        else:
            continue
    
    if(flag):
        print(f"{num} is composite")
    else:
        print(f"{num} is prime")

num = int(input("Enter a number: "))
checkPrime(num)