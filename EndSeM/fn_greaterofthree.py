def maxofthree(a,b,c):
    if(a > (b and c)):
        return a
    elif( b > (a and c)):
        return b
    else:
        return c

print("Greatest of three: ", maxofthree(4,61,12))